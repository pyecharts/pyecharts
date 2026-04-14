# Sprint {N} 合约

## Sprint 目标

（一句话描述本 Sprint 要实现什么）

## 上下文

- **依赖的前置 Sprint**: Sprint {N-1}（或"无"）
- **本 Sprint 修改的包列表**:
  - `pyecharts/xxx/`
  - `test/test_xxx.py`

## 交付物清单

| 文件 | 操作 | 说明 |
|------|------|------|
| `pyecharts/xxx/yyy.py` | 新增 | 实现 XxxClass |
| `test/test_xxx.py` | 新增 | XxxClass 的单元测试 |
| `pyecharts/zzz.py` | 修改 | 添加 xxx 支持 |

## 对外接口

```python
# 新增或修改的公开 API（只写签名，不写实现）
class XxxOpts(BasicOpts):
    """Xxx 的配置选项。"""

    def __init__(self, param: str = "default"):
        ...
```

## 评分维度（满分 100）

| 维度 | 满分 | 评估内容 |
|------|------|----------|
| 构建正确性 | 20 | `uv build` 成功 |
| 功能正确性 | 30 | 各验收命令通过 |
| 测试充分性 | 20 | 新增函数测试覆盖(8) + 增量覆盖率≥70%(7) + 渲染验证(5) |
| 架构一致性 | 20 | 方法链 / Options 模式 / 类型提示 / 命名一致 |
| 代码质量 | 10 | Flake8 通过 / 文件 < 500 行 |

## 验收标准

### 必须通过（MUST）

- [ ] **M-BUILD**: `uv build` 返回 0
- [ ] **M-REGRESSION**: `uv run pytest -v --cov-config=pyproject.toml --cov=./ test/` 全部 PASS
- [ ] **M-TEST**: 新增/修改的每个公开函数有测试，增量覆盖率 ≥ 70%
- [ ] **M-VERIFY**: （在此填写具体的 FAIL_TO_PASS 验证命令）
  - 实现前: `uv run pytest test/test_xxx.py::test_new_feature` → FAIL
  - 实现后: `uv run pytest test/test_xxx.py::test_new_feature` → PASS
- [ ] **M-RENDER**: （涉及渲染变更时填写）
  - 生成的 HTML 可正常打开
  - ECharts 选项 JSON 结构正确
- [ ] （在此添加更多 MUST 条款）

### 功能验收（SHOULD）

- [ ] （在此填写功能验收标准）
- [ ] （每条都要有具体的验证命令和预期输出）

### 代码质量（CODE）

- [ ] 新增文件 < 500 行
- [ ] 所有公开函数都有类型提示
- [ ] 所有公开函数都有 Google 风格文档字符串
- [ ] 方法链模式正确（修改方法返回 self）
- [ ] Options 模式一致（继承 BasicOpts）
- [ ] 无硬编码路径
- [ ] 无 TODO/FIXME 注释
- [ ] `make lint` 无错误

## 风险点

1. （列出可能的技术风险）
2. （列出可能的兼容性风险）
3. （列出可能的渲染风险）

## 多轮迭代策略

- **第 1 轮**: 实现核心功能，确保 M-BUILD + M-REGRESSION + M-TEST 通过
- **第 2 轮**: 修复 Evaluator 发现的问题，提升架构一致性和代码质量
- **第 3 轮**: 精修边界场景，确保评分 ≥ 90

## 失败回滚

```bash
git stash
```
