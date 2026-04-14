#!/usr/bin/env bash
# ============================================================
# pyecharts — Preflight Check (30-second quick validation)
# No Docker dependency required.
#
# Usage: bash .harness/scripts/preflight.sh
# ============================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/../config.env"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

PASS_COUNT=0
FAIL_COUNT=0
WARN_COUNT=0

pass() { echo -e "${GREEN}✅ PASS${NC}: $1"; ((PASS_COUNT++)); }
fail() { echo -e "${RED}❌ FAIL${NC}: $1"; ((FAIL_COUNT++)); }
warn() { echo -e "${YELLOW}⚠️  WARN${NC}: $1"; ((WARN_COUNT++)); }

echo "============================================================"
echo "  pyecharts — Preflight Check"
echo "  $(date '+%Y-%m-%d %H:%M:%S')"
echo "============================================================"
echo ""

# ── Check 1: Python version ────────────────────────────────
echo "── Check 1: Python version ──"
PYTHON_VERSION=$(python3 --version 2>/dev/null | awk '{print $2}')
if [ -z "$PYTHON_VERSION" ]; then
    fail "Python3 not found"
else
    MAJOR=$(echo "$PYTHON_VERSION" | cut -d. -f1)
    MINOR=$(echo "$PYTHON_VERSION" | cut -d. -f2)
    REQ_MAJOR=$(echo "$PYTHON_MIN_VERSION" | cut -d. -f1)
    REQ_MINOR=$(echo "$PYTHON_MIN_VERSION" | cut -d. -f2)
    if [ "$MAJOR" -gt "$REQ_MAJOR" ] || ([ "$MAJOR" -eq "$REQ_MAJOR" ] && [ "$MINOR" -ge "$REQ_MINOR" ]); then
        pass "Python $PYTHON_VERSION >= $PYTHON_MIN_VERSION"
    else
        fail "Python $PYTHON_VERSION < $PYTHON_MIN_VERSION"
    fi
fi
echo ""

# ── Check 2: uv available ──────────────────────────────────
echo "── Check 2: uv available ──"
if command -v uv &>/dev/null; then
    UV_VERSION=$(uv --version 2>/dev/null)
    pass "uv found: $UV_VERSION"
else
    fail "uv not found (install: https://docs.astral.sh/uv/)"
fi
echo ""

# ── Check 3: Build ──────────────────────────────────────────
echo "── Check 3: Build validation ──"
if $BUILD_CMD 2>/dev/null; then
    pass "uv build succeeded"
else
    fail "uv build failed"
fi
echo ""

# ── Check 4: Flake8 ─────────────────────────────────────────
echo "── Check 4: Flake8 lint ──"
FLAKE8_OUTPUT=$($LINT_CMD 2>&1) || true
if [ -z "$FLAKE8_OUTPUT" ]; then
    pass "flake8: no errors"
else
    FLAKE8_COUNT=$(echo "$FLAKE8_OUTPUT" | wc -l | tr -d ' ')
    warn "flake8: $FLAKE8_COUNT issue(s) found"
    echo "$FLAKE8_OUTPUT" | head -5
fi
echo ""

# ── Check 5: Dead code detection ────────────────────────────
echo "── Check 5: Dead code detection ──"
DEAD_CODE_PATTERNS=("def _unused_" "class _Unused")
DEAD_CODE_FOUND=0
for pattern in "${DEAD_CODE_PATTERNS[@]}"; do
    MATCHES=$(grep -rn "$pattern" "$SRC_DIR" 2>/dev/null | wc -l | tr -d ' ')
    DEAD_CODE_FOUND=$((DEAD_CODE_FOUND + MATCHES))
done
if [ "$DEAD_CODE_FOUND" -eq 0 ]; then
    pass "No obvious dead code patterns found"
else
    warn "Found $DEAD_CODE_FOUND potential dead code pattern(s)"
fi
echo ""

# ── Check 6: File size ───────────────────────────────────────
echo "── Check 6: File size check (max $MAX_FILE_LINES lines) ──"
OVERSIZED_FILES=0
while IFS= read -r file; do
    LINE_COUNT=$(wc -l < "$file" | tr -d ' ')
    if [ "$LINE_COUNT" -gt "$MAX_FILE_LINES" ]; then
        warn "$file: $LINE_COUNT lines (> $MAX_FILE_LINES)"
        ((OVERSIZED_FILES++))
    fi
done < <(find "$SRC_DIR" -name "*.py" -type f)
if [ "$OVERSIZED_FILES" -eq 0 ]; then
    pass "All source files within $MAX_FILE_LINES line limit"
fi
echo ""

# ── Check 7: TODO/FIXME detection ────────────────────────────
echo "── Check 7: TODO/FIXME detection ──"
TODO_COUNT=$(grep -rn "TODO\|FIXME" "$SRC_DIR" --include="*.py" 2>/dev/null | wc -l | tr -d ' ')
if [ "$TODO_COUNT" -eq 0 ]; then
    pass "No TODO/FIXME comments found"
else
    warn "Found $TODO_COUNT TODO/FIXME comment(s)"
    grep -rn "TODO\|FIXME" "$SRC_DIR" --include="*.py" 2>/dev/null | head -5
fi
echo ""

# ── Summary ──────────────────────────────────────────────────
echo "============================================================"
echo "  Preflight Summary"
echo "============================================================"
echo -e "  ${GREEN}PASS${NC}: $PASS_COUNT"
echo -e "  ${RED}FAIL${NC}: $FAIL_COUNT"
echo -e "  ${YELLOW}WARN${NC}: $WARN_COUNT"
echo ""

if [ "$FAIL_COUNT" -gt 0 ]; then
    echo -e "${RED}PREFLIGHT FAILED${NC} — Fix $FAIL_COUNT failure(s) before proceeding."
    exit 1
else
    echo -e "${GREEN}PREFLIGHT PASSED${NC}"
    exit 0
fi
