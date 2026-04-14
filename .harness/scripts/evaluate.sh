#!/usr/bin/env bash
# ============================================================
# pyecharts — Sprint Evaluation Script
#
# Usage: bash .harness/scripts/evaluate.sh <sprint-number>
#
# Output:
#   .harness/sprints/sprint-N-qa-report.md   (human-readable)
#   .harness/sprints/sprint-N-failures.json   (machine-readable)
# ============================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/../config.env"

if [ $# -lt 1 ]; then
    echo "Usage: bash $0 <sprint-number>"
    exit 1
fi

SPRINT_NUM="$1"
CONTRACT_FILE="${SPRINT_DIR}/sprint-${SPRINT_NUM}-contract.md"
REPORT_FILE="${SPRINT_DIR}/sprint-${SPRINT_NUM}-qa-report.md"
FAILURES_FILE="${SPRINT_DIR}/sprint-${SPRINT_NUM}-failures.json"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SCORE_BUILD_ACTUAL=0
SCORE_FUNCTION_ACTUAL=0
SCORE_TEST_ACTUAL=0
SCORE_ARCH_ACTUAL=0
SCORE_QUALITY_ACTUAL=0
TOTAL_SCORE=0
OVERALL_RESULT="PASS"
FAILURES="[]"

add_failure() {
    local dimension="$1"
    local description="$2"
    local points_lost="$3"
    FAILURES=$(echo "$FAILURES" | python3 -c "
import sys, json
failures = json.load(sys.stdin)
failures.append({'dimension': '$dimension', 'description': '''$description''', 'points_lost': $points_lost})
print(json.dumps(failures))
")
}

echo "============================================================"
echo "  pyecharts — Sprint $SPRINT_NUM Evaluation"
echo "  $(date '+%Y-%m-%d %H:%M:%S')"
echo "============================================================"
echo ""

# ── Verify contract exists ───────────────────────────────────
if [ ! -f "$CONTRACT_FILE" ]; then
    echo -e "${RED}ERROR: Contract file not found: $CONTRACT_FILE${NC}"
    exit 1
fi
echo -e "${BLUE}Contract: $CONTRACT_FILE${NC}"
echo ""

# ── Step 1: Build Verification (20 points) ───────────────────
echo "── Step 1: Build Verification ($SCORE_BUILD pts) ──"
if $BUILD_CMD 2>/dev/null; then
    SCORE_BUILD_ACTUAL=$SCORE_BUILD
    echo -e "${GREEN}✅ Build: PASS ($SCORE_BUILD/$SCORE_BUILD)${NC}"
else
    SCORE_BUILD_ACTUAL=0
    OVERALL_RESULT="FAIL"
    add_failure "build" "uv build failed" "$SCORE_BUILD"
    echo -e "${RED}❌ Build: FAIL (0/$SCORE_BUILD) — STOPPING${NC}"
    TOTAL_SCORE=0
    echo "$FAILURES" > "$FAILURES_FILE"
    cat > "$REPORT_FILE" <<EOF
## Sprint $SPRINT_NUM QA Report

### 总分: $TOTAL_SCORE / $SCORE_TOTAL

### 判定: FAIL — Build failed, evaluation stopped.
EOF
    exit 1
fi
echo ""

# ── Step 1.5: Regression Test (MANDATORY) ────────────────────
echo "── Step 1.5: Regression Test (MANDATORY) ──"
if uv run pytest -v --cov-config=pyproject.toml --cov=./ test/ -q 2>/dev/null; then
    echo -e "${GREEN}✅ Regression: PASS${NC}"
else
    OVERALL_RESULT="FAIL"
    add_failure "regression" "Unit test regression failed" "0"
    echo -e "${RED}❌ Regression: FAIL — STOPPING${NC}"
    TOTAL_SCORE=$SCORE_BUILD_ACTUAL
    echo "$FAILURES" > "$FAILURES_FILE"
    cat > "$REPORT_FILE" <<EOF
## Sprint $SPRINT_NUM QA Report

### 总分: $TOTAL_SCORE / $SCORE_TOTAL

### 判定: FAIL — Regression tests failed, evaluation stopped.
EOF
    exit 1
fi
echo ""

# ── Step 2: Functionality (30 points) ────────────────────────
echo "── Step 2: Functionality ($SCORE_FUNCTION pts) ──"
echo "  (Evaluated by Evaluator Agent against contract acceptance criteria)"
SCORE_FUNCTION_ACTUAL=$SCORE_FUNCTION
echo -e "${BLUE}ℹ️  Function score set to full — Evaluator Agent will adjust based on contract.${NC}"
echo ""

# ── Step 2.5: Test Sufficiency (20 points) ───────────────────
echo "── Step 2.5: Test Sufficiency ($SCORE_TEST pts) ──"

# Sub-score 1: New function test coverage (8 pts)
echo "  Checking new function test coverage..."
NEW_FUNC_SCORE=8
echo -e "  ${GREEN}✅ New function coverage: $NEW_FUNC_SCORE/8${NC} (Evaluator Agent verifies)"

# Sub-score 2: Incremental coverage >= 70% (7 pts)
COV_OUTPUT=$(uv run pytest -v --cov-config=pyproject.toml --cov=./ --cov-report=term test/ 2>&1) || true
TOTAL_COV=$(echo "$COV_OUTPUT" | grep "^TOTAL" | awk '{print $NF}' | tr -d '%' || echo "0")
INC_COV_SCORE=0
if [ -n "$TOTAL_COV" ] && [ "$TOTAL_COV" -ge "$INCREMENTAL_COVERAGE_MIN" ]; then
    INC_COV_SCORE=7
    echo -e "  ${GREEN}✅ Coverage ${TOTAL_COV}% >= ${INCREMENTAL_COVERAGE_MIN}%: $INC_COV_SCORE/7${NC}"
else
    add_failure "test" "Coverage ${TOTAL_COV}% < ${INCREMENTAL_COVERAGE_MIN}%" "7"
    echo -e "  ${RED}❌ Coverage ${TOTAL_COV}% < ${INCREMENTAL_COVERAGE_MIN}%: 0/7${NC}"
fi

# Sub-score 3: Render verification (5 pts)
RENDER_SCORE=0
RENDER_TESTS=$(uv run pytest test/ -v -k "render" --co -q 2>/dev/null | wc -l | tr -d ' ')
if [ "$RENDER_TESTS" -gt 0 ]; then
    RENDER_SCORE=5
    echo -e "  ${GREEN}✅ Render tests exist ($RENDER_TESTS tests): $RENDER_SCORE/5${NC}"
else
    echo -e "  ${YELLOW}⚠️  No render-specific tests found: 0/5${NC}"
fi

SCORE_TEST_ACTUAL=$((NEW_FUNC_SCORE + INC_COV_SCORE + RENDER_SCORE))
echo -e "  Test sufficiency: $SCORE_TEST_ACTUAL/$SCORE_TEST"
echo ""

# ── Step 3: Architecture Consistency (20 points) ─────────────
echo "── Step 3: Architecture Consistency ($SCORE_ARCH pts) ──"
ARCH_DEDUCTIONS=0

# Check for missing type hints on public functions
MISSING_HINTS=$(grep -rn "def [a-z]" "$SRC_DIR" --include="*.py" 2>/dev/null | grep -v "def _" | grep -v "-> " | wc -l | tr -d ' ')
if [ "$MISSING_HINTS" -gt 10 ]; then
    ARCH_DEDUCTIONS=$((ARCH_DEDUCTIONS + 5))
    add_failure "arch" "Found $MISSING_HINTS public functions without return type hints" "5"
    echo -e "  ${YELLOW}⚠️  $MISSING_HINTS public functions missing return type hints${NC}"
fi

# Check for methods that don't return self (method chain violation)
NO_RETURN_SELF=$(grep -rn "def add_\|def set_" "$SRC_DIR/charts" --include="*.py" 2>/dev/null | wc -l | tr -d ' ')
RETURN_SELF=$(grep -rn "return self" "$SRC_DIR/charts" --include="*.py" 2>/dev/null | wc -l | tr -d ' ')
if [ "$NO_RETURN_SELF" -gt 0 ] && [ "$RETURN_SELF" -eq 0 ]; then
    ARCH_DEDUCTIONS=$((ARCH_DEDUCTIONS + 5))
    add_failure "arch" "Method chain pattern violation: add_/set_ methods without return self" "5"
    echo -e "  ${YELLOW}⚠️  Method chain pattern violation detected${NC}"
fi

SCORE_ARCH_ACTUAL=$((SCORE_ARCH - ARCH_DEDUCTIONS))
if [ "$SCORE_ARCH_ACTUAL" -lt 0 ]; then SCORE_ARCH_ACTUAL=0; fi
echo -e "  Architecture: $SCORE_ARCH_ACTUAL/$SCORE_ARCH"
echo ""

# ── Step 4: Code Quality (10 points) ─────────────────────────
echo "── Step 4: Code Quality ($SCORE_QUALITY pts) ──"
QUALITY_DEDUCTIONS=0

# Check lint
LINT_OUTPUT=$($LINT_CMD 2>&1) || true
if [ -z "$LINT_OUTPUT" ]; then
    echo -e "  ${GREEN}✅ Lint: clean${NC}"
else
    QUALITY_DEDUCTIONS=$((QUALITY_DEDUCTIONS + 3))
    LINT_ERRORS=$(echo "$LINT_OUTPUT" | wc -l | tr -d ' ')
    add_failure "quality" "Lint: $LINT_ERRORS issue(s) found" "3"
    echo -e "  ${YELLOW}⚠️  Lint: $LINT_ERRORS issue(s) found (-3)${NC}"
fi

# Check file sizes
OVERSIZED=0
while IFS= read -r file; do
    LINE_COUNT=$(wc -l < "$file" | tr -d ' ')
    if [ "$LINE_COUNT" -gt "$MAX_FILE_LINES" ]; then
        ((OVERSIZED++))
        echo -e "  ${YELLOW}⚠️  $file: $LINE_COUNT lines (> $MAX_FILE_LINES)${NC}"
    fi
done < <(find "$SRC_DIR" -name "*.py" -type f)
if [ "$OVERSIZED" -gt 0 ]; then
    QUALITY_DEDUCTIONS=$((QUALITY_DEDUCTIONS + 2))
    add_failure "quality" "$OVERSIZED file(s) exceed $MAX_FILE_LINES lines" "2"
fi

# Check for TODO/FIXME
TODO_COUNT=$(grep -rn "TODO\|FIXME" "$SRC_DIR" --include="*.py" 2>/dev/null | wc -l | tr -d ' ')
if [ "$TODO_COUNT" -gt 0 ]; then
    QUALITY_DEDUCTIONS=$((QUALITY_DEDUCTIONS + 2))
    add_failure "quality" "Found $TODO_COUNT TODO/FIXME comment(s)" "2"
    echo -e "  ${YELLOW}⚠️  $TODO_COUNT TODO/FIXME comment(s) found (-2)${NC}"
else
    echo -e "  ${GREEN}✅ No TODO/FIXME${NC}"
fi

# Check for hardcoded paths
HARDCODED=$(grep -rn "127\.0\.0\.1\|localhost" "$SRC_DIR" --include="*.py" 2>/dev/null | grep -v "test\|example\|#" | wc -l | tr -d ' ')
if [ "$HARDCODED" -gt 0 ]; then
    QUALITY_DEDUCTIONS=$((QUALITY_DEDUCTIONS + 1))
    add_failure "quality" "Found $HARDCODED hardcoded address(es)" "1"
    echo -e "  ${YELLOW}⚠️  $HARDCODED hardcoded address(es) found (-1)${NC}"
fi

SCORE_QUALITY_ACTUAL=$((SCORE_QUALITY - QUALITY_DEDUCTIONS))
if [ "$SCORE_QUALITY_ACTUAL" -lt 0 ]; then SCORE_QUALITY_ACTUAL=0; fi
echo -e "  Code quality: $SCORE_QUALITY_ACTUAL/$SCORE_QUALITY"
echo ""

# ── Final Score ──────────────────────────────────────────────
TOTAL_SCORE=$((SCORE_BUILD_ACTUAL + SCORE_FUNCTION_ACTUAL + SCORE_TEST_ACTUAL + SCORE_ARCH_ACTUAL + SCORE_QUALITY_ACTUAL))

if [ "$TOTAL_SCORE" -lt "$SCORE_PASS_THRESHOLD" ]; then
    OVERALL_RESULT="FAIL"
fi

echo "============================================================"
echo "  Sprint $SPRINT_NUM — Final Score: $TOTAL_SCORE / $SCORE_TOTAL"
echo "============================================================"
echo ""
echo "  Build:        $SCORE_BUILD_ACTUAL / $SCORE_BUILD"
echo "  Function:     $SCORE_FUNCTION_ACTUAL / $SCORE_FUNCTION"
echo "  Test:         $SCORE_TEST_ACTUAL / $SCORE_TEST"
echo "  Architecture: $SCORE_ARCH_ACTUAL / $SCORE_ARCH"
echo "  Quality:      $SCORE_QUALITY_ACTUAL / $SCORE_QUALITY"
echo ""

if [ "$OVERALL_RESULT" = "PASS" ]; then
    echo -e "${GREEN}EVALUATION: PASS (>= $SCORE_PASS_THRESHOLD)${NC}"
else
    echo -e "${RED}EVALUATION: FAIL (< $SCORE_PASS_THRESHOLD)${NC}"
fi

# ── Write Reports ────────────────────────────────────────────
cat > "$REPORT_FILE" <<EOF
## Sprint $SPRINT_NUM QA Report

### 总分: $TOTAL_SCORE / $SCORE_TOTAL

### 评分明细
| 维度 | 得分 | 满分 | 说明 |
|------|------|------|------|
| 构建正确性 | $SCORE_BUILD_ACTUAL | $SCORE_BUILD | uv build |
| 功能正确性 | $SCORE_FUNCTION_ACTUAL | $SCORE_FUNCTION | Contract acceptance criteria |
| 测试充分性 | $SCORE_TEST_ACTUAL | $SCORE_TEST | Coverage: ${TOTAL_COV}% |
| 架构一致性 | $SCORE_ARCH_ACTUAL | $SCORE_ARCH | Method chain, Options pattern, type hints |
| 代码质量 | $SCORE_QUALITY_ACTUAL | $SCORE_QUALITY | Lint, file size, TODOs |

### 判定: $OVERALL_RESULT

### 生成时间: $(date '+%Y-%m-%d %H:%M:%S')
EOF

echo "$FAILURES" > "$FAILURES_FILE"

echo ""
echo "Reports written:"
echo "  $REPORT_FILE"
echo "  $FAILURES_FILE"

if [ "$OVERALL_RESULT" = "FAIL" ]; then
    exit 1
else
    exit 0
fi
