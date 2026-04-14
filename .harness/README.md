# pyecharts — Harness 开发模式

> **Harness** 是一套 AI Agent 驱动的质量保证体系，管理软件开发的完整生命周期：
> 需求分析 → 合约设计 → 代码实现 → 测试验证 → 质量评估。

## 快速开始

### 强制启动仪式

收到任何涉及 **sprint / harness / 合约 / 评估 / 需求开发** 的任务时，**必须先读取以下 3 个文件**：

```bash
read_file .harness/README.md
read_file .harness/prompts/generator.md
read_file .harness/prompts/evaluator.md
```

**原因**：AI Agent 容易"凭记忆执行"而遗漏关键流程，只有每次重新读取才能确保不遗漏。

---

## 八步三 Agent 工作流

### 概览

```
Step 1: [Planner]    需求分析 → 扩展为完整技术规格
Step 2: [Generator]  写 sprint-N-contract.md（合约先行）
Step 3: [Evaluator]  独立审查合约（sub agent，怀疑视角）
Step 4: ⏸️ 用户确认   与用户讨论合约，等待用户确认
Step 5: [Generator]  实现代码
Step 6: ⚠️ 全量回归   存量全量回归测试（MANDATORY）
Step 7: [Evaluator]  执行评估脚本 + 独立代码审查
Step 8: 评分判定     ≥ 90 → 继续；< 90 → 修复后重跑
```

### 三 Agent 架构

| Agent | 角色 | 职责 | 提示词文件 |
|-------|------|------|-----------|
| **Planner** | 首席架构师 | 需求分析 → 技术规格 | `prompts/planner.md` |
| **Generator** | 高级 Python 工程师 | 合约起草 → 代码实现 | `prompts/generator.md` |
| **Evaluator** | 独立审查者 | 合约审查 → 代码评估 | `prompts/evaluator.md` |

---

### Step 1: [Planner] 需求分析

**触发条件**：收到新的功能需求或技术任务。

**执行动作**：
1. 读取 `.harness/prompts/planner.md`
2. 将简短需求扩展为完整技术规格
3. 输出 `product-spec.md`（包含项目概述、功能列表、技术设计、Sprint 计划）

**规划原则**：
- 约束交付物，不约束实现路径
- 宁可拆小 Sprint，不要大而全
- 每个 Sprint 必须可独立验证
- 渐进式增强
- 测试先行

### Step 2: [Generator] 写合约

**执行动作**：
1. 从 `.harness/sprints/sprint-template.md` 复制模板
2. 填写：Sprint 目标、上下文、交付物清单、对外接口
3. 定义验收标准（MUST / SHOULD / CODE）
4. 列出风险点
5. 输出 `.harness/sprints/sprint-N-contract.md`

**合约必须包含的强制条款**：
- **M-BUILD**: `uv build` 返回 0
- **M-REGRESSION**: `uv run pytest -v --cov-config=pyproject.toml --cov=./ test/` 全部 PASS（存量全量回归）
- **M-TEST**: 新增/修改的每个公开函数必须有测试，增量覆盖率 ≥ 70%
- **M-VERIFY**: FAIL_TO_PASS 验证（实现前 FAIL，实现后 PASS）
- **M-RENDER**: 涉及图表渲染变更时，生成的 HTML 可正常打开且 ECharts 选项正确

### Step 3: [Evaluator] 独立审查合约

**执行动作**：
1. 使用 sub agent 以 Evaluator 角色独立审查合约
2. 读取 `.harness/prompts/evaluator.md` 获取审查标准
3. 以怀疑论者视角审查：可测量性、覆盖完整性、风险评估
4. 输出合约审查报告

**审查输出格式**：

```markdown
## Evaluator 合约审查报告

### 总体评价
APPROVE / NEEDS_REVISION / REJECT

### 逐条审查
| # | 验收标准 | 可测量性 | 覆盖度 | 问题 | 建议修改 |
|---|---------|---------|--------|------|---------|

### 遗漏的验收标准
- ...

### 风险点补充
- ...
```

### Step 4: ⏸️ 用户确认合约

**双重门禁机制**：
1. Evaluator 审查通过
2. 用户明确确认（"可以开始"、"确认"、"开始实现"等）

**未经确认禁止进入 Step 5。**

### Step 5: [Generator] 实现代码

**执行动作**：
1. 读取 `.harness/prompts/generator.md` 获取编码规范
2. 按合约逐条实现
3. 自评：按合约验收标准检查
4. 输出 `.harness/sprints/sprint-N-result.md`

### Step 6: ⚠️ 存量全量回归测试（MANDATORY）

**历史教训**：只跑修改涉及的包会遗漏存量回归。

**强制规则**：
- **禁止"就近验证"**：不能只跑修改涉及的测试文件
- 必须跑全量：`uv run pytest -v --cov-config=pyproject.toml --cov=./ test/`
- 如果有 FAIL，必须先修复再提交

**执行命令**：

```bash
# 单元测试全量回归
uv run pytest -v --cov-config=pyproject.toml --cov=./ test/
```

### Step 7: [Evaluator] 执行评估

**执行动作**：
1. 运行 `.harness/scripts/preflight.sh`（30 秒快速预检）
2. 运行 `.harness/scripts/evaluate.sh`（完整评估）
3. 使用 sub agent 以 Evaluator 角色独立代码审查
4. 输出 `.harness/sprints/sprint-N-qa-report.md` + `.harness/sprints/sprint-N-failures.json`

### Step 8: 评分判定

| 分数 | 含义 | 操作 |
|------|------|------|
| 100 | 完美 | 可直接合并 |
| 95-99 | 优秀 | 可合并，记录 warning |
| 90-94 | 通过 | 建议修复后合并 |
| < 90 | 不通过 | **禁止合并**，必须修复 |

**多轮迭代规则**：
- 第一轮 < 90 分 → 必须修复重跑，最多 3 轮
- 若后续轮次分数低于前一轮 → 保留最高分轮次
- 三轮后仍 < 90 → 停止，向用户汇报失分原因

**评分趋势判断**：

| 情况 | 建议 |
|------|------|
| 评分持续上升 | 继续精炼，聚焦剩余失分项 |
| 评分停滞（连续 2 轮无改善） | 换实现方案而非修补 |
| 评分回退 | 立即标记 REGRESSION，建议回滚 |
| 3 轮后仍 < 90 | 上报用户，附带阻塞原因 |

---

## 评分维度（满分 100）

| 维度 | 满分 | 评估内容 | Hard Threshold |
|------|------|----------|---------------|
| **构建正确性** | 20 | `uv build` 成功 | 构建失败 → 整体 FAIL |
| **功能正确性** | 30 | 合约验收命令全部通过 | 核心路径不通 → FAIL |
| **测试充分性** | 20 | 新增函数测试覆盖(8) + 增量覆盖率≥70%(7) + 渲染验证(5) | M-TEST 失败 → FAIL |
| **架构一致性** | 20 | 方法链 / Options 模式 / 类型提示 / 命名一致 | 架构违规 → -5/项 |
| **代码质量** | 10 | Flake8 通过 / 文件 < 500 行 | 单文件 > 500 行 → WARN |

---

## 自动化脚本

### 快速预检（30 秒）

```bash
bash .harness/scripts/preflight.sh
```

检查项：
- Python 版本 ≥ 3.7
- `uv build` 成功
- `flake8` 无错误
- dead code 检测

### 完整评估

```bash
bash .harness/scripts/evaluate.sh <sprint-number>
```

输出：
- `sprint-N-qa-report.md` — 人类可读报告
- `sprint-N-failures.json` — 机器可读失分 JSON

### 全量回归测试

```bash
bash .harness/scripts/regression.sh
```

### 自动迭代

```bash
bash .harness/scripts/harness-iterate.sh <sprint-number> [max-rounds]
```

循环：evaluate → 解析 failures.json → 修复 → 重跑（默认最多 3 轮）

### 多 Sprint 自动编排

```bash
bash .harness/scripts/vision-master.sh
```

---

## 目录结构

```
.harness/
├── README.md                    # 本文件
├── config.env                   # 配置常量
├── vision-state.json            # 跨 Session 状态
│
├── prompts/                     # Agent 角色提示词
│   ├── planner.md               # Planner — 首席架构师
│   ├── generator.md             # Generator — 高级 Python 工程师
│   ├── evaluator.md             # Evaluator — 独立审查者
│   └── regression.md            # 回归测试模板
│
├── scripts/                     # 自动化脚本
│   ├── evaluate.sh              # 完整评估
│   ├── preflight.sh             # 快速预检
│   ├── regression.sh            # 回归测试
│   ├── harness-iterate.sh       # 自动迭代器
│   └── vision-master.sh         # 多 Sprint 编排
│
├── sprints/                     # Sprint 产物
│   ├── SPRINT_INDEX.md          # 汇总索引
│   ├── sprint-template.md       # 合约模板
│   ├── sprint-N-contract.md     # 合约
│   ├── sprint-N-result.md       # 实现结果
│   ├── sprint-N-qa-report.md    # QA 报告
│   └── sprint-N-failures.json   # 失分 JSON
│
└── artifacts/                   # 累积决策
    └── build-context.md         # Build Context
```

---

## 触发规则

### 自动触发 Harness

当修改以下路径时，自动触发 Harness 流程：
- `pyecharts/`
- `test/`
- `examples/`

### 强制启动仪式

当收到包含以下关键词的任务时：
- sprint、harness、合约、评估、需求开发

### 豁免场景

以下场景不触发 Harness：
- 纯文档修改（`.md` 文件）
- 配置文件调整（`.gitignore`、`pyproject.toml` 等）
- CI/CD 脚本修改
- 纯重构（不改变外部行为）

---

## Git 提交规则

### 禁止提交的文件

- `*.pyc`、`__pycache__/` — Python 编译产物
- `.pytest_cache/`、`.coverage`、`coverage.xml` — 测试产物
- `dist/`、`build/`、`*.egg-info/` — 构建产物
- `.idea/`、`.vscode/` — IDE 配置
- `.harness/sprints/sprint-*-result.md` — AI 内部产物
- `.harness/sprints/sprint-*-qa-report.md` — AI 内部产物
- `.harness/sprints/sprint-*-failures.json` — AI 内部产物
- `.harness/vision-master.log` — 运行时日志

### 提交前检查

1. 读取 `.gitignore` 文件
2. 运行 `git status` 检查暂存区
3. 禁止使用 `git add .` 或 `git add -A`
