#!/usr/bin/env bash
# ============================================================
# pyecharts — Vision Master (Multi-Sprint Orchestrator)
#
# Orchestrates multiple Sprints in sequence, tracking progress
# in vision-state.json and maintaining the Sprint index.
#
# Usage: bash .harness/scripts/vision-master.sh [start-sprint] [end-sprint]
# ============================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HARNESS_DIR="${SCRIPT_DIR}/.."
source "${HARNESS_DIR}/config.env"

STATE_FILE="${HARNESS_DIR}/vision-state.json"
INDEX_FILE="${SPRINT_DIR}/SPRINT_INDEX.md"
LOG_FILE="${HARNESS_DIR}/vision-master.log"
ITERATE_SCRIPT="${SCRIPT_DIR}/harness-iterate.sh"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

log() {
    local msg="[$(date '+%Y-%m-%d %H:%M:%S')] $1"
    echo "$msg" >> "$LOG_FILE"
    echo -e "$msg"
}

update_state() {
    local key="$1"
    local value="$2"
    python3 -c "
import json
with open('$STATE_FILE', 'r') as f:
    state = json.load(f)
state['$key'] = $value
state['last_updated'] = '$(date '+%Y-%m-%d')'
with open('$STATE_FILE', 'w') as f:
    json.dump(state, f, indent=2)
" 2>/dev/null
}

get_state() {
    local key="$1"
    python3 -c "
import json
with open('$STATE_FILE', 'r') as f:
    state = json.load(f)
print(json.dumps(state.get('$key', '')))
" 2>/dev/null
}

get_current_round() {
    python3 -c "
import json
with open('$STATE_FILE', 'r') as f:
    state = json.load(f)
print(state.get('round', 0))
" 2>/dev/null
}

echo "============================================================"
echo "  pyecharts — Vision Master"
echo "  $(date '+%Y-%m-%d %H:%M:%S')"
echo "============================================================"
echo ""

# Read current state
CURRENT_ROUND=$(get_current_round)
COMPLETED=$(get_state "completed_sprints")
CURRENT_SPRINT=$(get_state "current_sprint")
VISION_PCT=$(get_state "vision_completion_pct")

log "Vision Master started"
log "  Current round: $CURRENT_ROUND"
log "  Completed sprints: $COMPLETED"
log "  Current sprint: $CURRENT_SPRINT"
log "  Vision completion: $VISION_PCT%"

# Determine sprint range
START_SPRINT="${1:-}"
END_SPRINT="${2:-}"

if [ -z "$START_SPRINT" ]; then
    START_SPRINT=$(python3 -c "
import json
with open('$STATE_FILE', 'r') as f:
    state = json.load(f)
completed = state.get('completed_sprints', [])
if completed:
    print(max(completed) + 1)
else:
    print(1)
" 2>/dev/null)
fi

if [ -z "$END_SPRINT" ]; then
    END_SPRINT=$START_SPRINT
fi

log "Sprint range: $START_SPRINT to $END_SPRINT"
echo ""

# Process each sprint
for SPRINT_NUM in $(seq "$START_SPRINT" "$END_SPRINT"); do
    echo ""
    echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║  Sprint $SPRINT_NUM                                                    ║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""

    CONTRACT_FILE="${SPRINT_DIR}/sprint-${SPRINT_NUM}-contract.md"

    # Check if contract exists
    if [ ! -f "$CONTRACT_FILE" ]; then
        log "${YELLOW}Sprint $SPRINT_NUM: No contract found at $CONTRACT_FILE${NC}"
        echo -e "${YELLOW}⏸️  Sprint $SPRINT_NUM: Contract not found. Stopping.${NC}"
        echo ""
        echo "Next steps:"
        echo "  1. [Planner] Analyze requirements"
        echo "  2. [Generator] Write sprint-${SPRINT_NUM}-contract.md"
        echo "  3. [Evaluator] Review contract"
        echo "  4. User confirms contract"
        echo "  5. Re-run: bash $0 $SPRINT_NUM $END_SPRINT"
        break
    fi

    # Update state: current sprint
    update_state "current_sprint" "$SPRINT_NUM"
    NEW_ROUND=$((CURRENT_ROUND + 1))
    update_state "round" "$NEW_ROUND"
    CURRENT_ROUND=$NEW_ROUND

    log "Starting Sprint $SPRINT_NUM (round $CURRENT_ROUND)"

    # Run iteration
    ITERATE_EXIT=0
    bash "$ITERATE_SCRIPT" "$SPRINT_NUM" "$MAX_ITERATE_ROUNDS" || ITERATE_EXIT=$?

    if [ "$ITERATE_EXIT" -eq 0 ]; then
        # Sprint passed
        log "${GREEN}Sprint $SPRINT_NUM: PASSED${NC}"

        # Extract final score
        REPORT_FILE="${SPRINT_DIR}/sprint-${SPRINT_NUM}-qa-report.md"
        FINAL_SCORE=0
        if [ -f "$REPORT_FILE" ]; then
            FINAL_SCORE=$(grep "总分:" "$REPORT_FILE" | grep -oE '[0-9]+' | head -1 || echo "0")
        fi

        # Update state: add to completed
        python3 -c "
import json
with open('$STATE_FILE', 'r') as f:
    state = json.load(f)
if $SPRINT_NUM not in state.get('completed_sprints', []):
    state.setdefault('completed_sprints', []).append($SPRINT_NUM)
state['current_sprint'] = None
state['score_history'].append({'sprint': $SPRINT_NUM, 'score': $FINAL_SCORE, 'round': $CURRENT_ROUND})
state['last_updated'] = '$(date '+%Y-%m-%d')'
with open('$STATE_FILE', 'w') as f:
    json.dump(state, f, indent=2)
" 2>/dev/null

        echo -e "${GREEN}✅ Sprint $SPRINT_NUM completed with score $FINAL_SCORE${NC}"
    else
        # Sprint failed
        log "${RED}Sprint $SPRINT_NUM: FAILED after $MAX_ITERATE_ROUNDS rounds${NC}"
        echo -e "${RED}❌ Sprint $SPRINT_NUM failed. Stopping vision master.${NC}"
        echo ""
        echo "Action required:"
        echo "  1. Review failures: cat ${SPRINT_DIR}/sprint-${SPRINT_NUM}-failures.json"
        echo "  2. Fix issues manually"
        echo "  3. Re-run: bash $0 $SPRINT_NUM $END_SPRINT"
        exit 1
    fi
done

# Final summary
echo ""
echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  Vision Master — Summary                                    ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

python3 -c "
import json
with open('$STATE_FILE', 'r') as f:
    state = json.load(f)
completed = state.get('completed_sprints', [])
history = state.get('score_history', [])
print(f'  Completed Sprints: {len(completed)}')
print(f'  Total Rounds: {state.get(\"round\", 0)}')
if history:
    avg_score = sum(h['score'] for h in history) / len(history)
    print(f'  Average Score: {avg_score:.1f}')
print(f'  Vision Completion: {state.get(\"vision_completion_pct\", 0)}%')
" 2>/dev/null

log "Vision Master completed"
echo ""
echo -e "${GREEN}Vision Master finished.${NC}"
