#!/usr/bin/env bash
# ============================================================
# pyecharts — Harness Auto-Iterator
#
# Runs evaluate.sh in a loop, parsing failures.json between
# rounds to guide fixes. Stops when score >= threshold or
# max rounds reached.
#
# Usage: bash .harness/scripts/harness-iterate.sh <sprint-number> [max-rounds]
# ============================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/../config.env"

if [ $# -lt 1 ]; then
    echo "Usage: bash $0 <sprint-number> [max-rounds]"
    exit 1
fi

SPRINT_NUM="$1"
MAX_ROUNDS="${2:-$MAX_ITERATE_ROUNDS}"
EVALUATE_SCRIPT="${SCRIPT_DIR}/evaluate.sh"
FAILURES_FILE="${SPRINT_DIR}/sprint-${SPRINT_NUM}-failures.json"
REPORT_FILE="${SPRINT_DIR}/sprint-${SPRINT_NUM}-qa-report.md"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

BEST_SCORE=0
BEST_ROUND=0
PREV_SCORE=0

echo "============================================================"
echo "  pyecharts — Harness Auto-Iterator"
echo "  Sprint: $SPRINT_NUM"
echo "  Max Rounds: $MAX_ROUNDS"
echo "  Pass Threshold: $SCORE_PASS_THRESHOLD"
echo "  $(date '+%Y-%m-%d %H:%M:%S')"
echo "============================================================"
echo ""

for ROUND in $(seq 1 "$MAX_ROUNDS"); do
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo -e "  ${BLUE}Round $ROUND / $MAX_ROUNDS${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    # Run evaluation
    EVAL_EXIT=0
    bash "$EVALUATE_SCRIPT" "$SPRINT_NUM" || EVAL_EXIT=$?

    # Extract score from report
    CURRENT_SCORE=0
    if [ -f "$REPORT_FILE" ]; then
        CURRENT_SCORE=$(grep "总分:" "$REPORT_FILE" | grep -oE '[0-9]+' | head -1 || echo "0")
    fi

    echo ""
    echo -e "  Round $ROUND Score: ${BLUE}$CURRENT_SCORE / $SCORE_TOTAL${NC}"

    # Track best score
    if [ "$CURRENT_SCORE" -gt "$BEST_SCORE" ]; then
        BEST_SCORE=$CURRENT_SCORE
        BEST_ROUND=$ROUND
    fi

    # Check if passed
    if [ "$CURRENT_SCORE" -ge "$SCORE_PASS_THRESHOLD" ]; then
        echo ""
        echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
        echo -e "${GREEN}  PASSED in Round $ROUND with score $CURRENT_SCORE${NC}"
        echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
        exit 0
    fi

    # Trend analysis
    if [ "$ROUND" -gt 1 ]; then
        if [ "$CURRENT_SCORE" -lt "$PREV_SCORE" ]; then
            echo -e "  ${RED}⚠️  REGRESSION: Score dropped from $PREV_SCORE to $CURRENT_SCORE${NC}"
            echo -e "  ${YELLOW}Recommendation: Consider rolling back to Round $BEST_ROUND (score $BEST_SCORE)${NC}"
        elif [ "$CURRENT_SCORE" -eq "$PREV_SCORE" ]; then
            echo -e "  ${YELLOW}⚠️  STAGNATION: Score unchanged at $CURRENT_SCORE${NC}"
            echo -e "  ${YELLOW}Recommendation: Consider changing implementation approach${NC}"
        else
            IMPROVEMENT=$((CURRENT_SCORE - PREV_SCORE))
            echo -e "  ${GREEN}↑ Improved by $IMPROVEMENT points${NC}"
        fi
    fi

    PREV_SCORE=$CURRENT_SCORE

    # Show failures for next round
    if [ -f "$FAILURES_FILE" ] && [ "$ROUND" -lt "$MAX_ROUNDS" ]; then
        FAILURE_COUNT=$(python3 -c "import json; print(len(json.load(open('$FAILURES_FILE'))))" 2>/dev/null || echo "0")
        if [ "$FAILURE_COUNT" -gt 0 ]; then
            echo ""
            echo -e "  ${YELLOW}Failures to fix before Round $((ROUND + 1)):${NC}"
            python3 -c "
import json
with open('$FAILURES_FILE') as f:
    failures = json.load(f)
for i, failure in enumerate(failures, 1):
    print(f'    {i}. [{failure[\"dimension\"]}] {failure[\"description\"]} (-{failure[\"points_lost\"]})')
" 2>/dev/null || true
        fi
    fi

    if [ "$ROUND" -lt "$MAX_ROUNDS" ]; then
        echo ""
        echo -e "  ${BLUE}Waiting for fixes before Round $((ROUND + 1))...${NC}"
        echo -e "  ${BLUE}(Agent should fix failures and re-run this script)${NC}"
        exit 1
    fi
done

# Max rounds exhausted
echo ""
echo -e "${RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${RED}  FAILED after $MAX_ROUNDS rounds${NC}"
echo -e "${RED}  Best score: $BEST_SCORE (Round $BEST_ROUND)${NC}"
echo -e "${RED}  Threshold: $SCORE_PASS_THRESHOLD${NC}"
echo -e "${RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Action required: Report to user with blocking reasons."
exit 1
