# 体验守卫报告 v1

点名体验评审时，每个受影响的应用包、构建目标各输出一个 JSON 对象，字段服从同目录的 [JSON Schema](guardian-report.schema.json)。向人汇报时可把发现显示成 `[P0][W-C2] file:line — 影响 → 修复`。向编排器交付时使用原始 JSON。

包、目标或适配器尚未确认时，先汇报已有静态结果，标明“目标未确认，验收未完成”，待确认后再交付 v1 JSON。已确认路由、仅缺运行会话时，照常交付报告，将无法执行的必测操作逐项记为 `RUNTIME / required: true / NOT_RUN`，结论为 `INCOMPLETE`。已证实 P0 时按下文优先级判定。

| 字段 | 填写方式 |
| --- | --- |
| `schemaVersion`、`package` | 版本填数字 `1`。包填相对仓库根目录的应用路径，根包用 `.`。 |
| `target`、`adapter` | 取[目标路由](guardian-routing.md)中对应的一组值。 |
| `scope` | 默认 `STATIC`。有明确运行验证请求才填 `RUNTIME`，包含本次所需的静态证据和运行证据。 |
| `findings[]` | 每项写 `ruleId`、`severity`、`location`、`problem`、`fix`。说明触发条件、用户后果和最小修复。源码位置填 `{"file":"相对仓库的路径","line":1}`，行号从 1 开始。实测已证实缺陷、源码归因尚未定位时填 `null`。 |
| `evidence[]` | 每项写 `probeId`、`kind`（`STATIC` 或 `RUNTIME`）、`required`（布尔）、`status`、`detail`。同一探针沿用稳定的名字，`detail` 填文件行号、实测动作与观察、产物路径或未执行原因。每个发现都需对应到一项可核实的 `FAIL` 证据。 |
| `blindspots[]` | 填与本次改动有关、证据尚未覆盖的具体影响。没有则填 `[]`。必测项缺证同时记入 `evidence`。 |

先按请求和改动确定适用检查、必测项，再填结果。`PASS` 和 `FAIL` 代表实际检查已有结论，`FAIL` 需对应已证实的产品问题。`NOT_RUN` 代表该项未执行或中途未取得所需证据，例如自动化端口不可用。`NOT_APPLICABLE` 仅用于经确认与范围无关的条目，填 `required: false` 并说明理由。纯静态请求只记录静态检查；用户明确要求的运行检查必须逐项记录，即使环境阻止执行。

## 明确要求实测且需要机读放行时

从工单或用户原始验收要求独立列出必测操作，为每项指定稳定的 `probeId`。每项各留一条 `kind: RUNTIME`、`required: true` 的记录。在 `detail` 写明本次操作与观察；只有静态依据时保留静态记录，并另记该实测项为 `NOT_RUN`。

按 v1 Schema 校验报告结构后，可用本技能附带的[覆盖检查脚本](../scripts/check_runtime_coverage.py)对照原始清单。以下命令从技能目录运行，验收项为鼠标关闭弹窗和键盘关闭后焦点恢复。

```sh
python scripts/check_runtime_coverage.py report.json --require W-D3.mouse-close --require W-D3.keyboard-restore
```

脚本使用 Python 3.8+ 标准库。退出码 `0` 表示报告结论为 `PASS`、清单中的每项均有唯一的必测运行通过记录、报告无失败证据；`1` 表示未放行，`2` 表示参数或输入读取错误。Schema 合法的 `INCOMPLETE` 报告仍可交付。清单的完整性取决于原始要求，观察的真实性需回看证据。

## 计算 verdict

按已证实的用户后果定级。P0 用于核心操作无法完成、权限暴露或可重现的数据错误；P1 用于任务仍可完成但存在可验证的体验损失，例如焦点丢失导致键盘用户必须重新定位。Web 规则编号用于定位检查项，具体严重度取决于本次影响。只有主观偏好或证据仍不足时，保留为建议或待验证项，`findings` 只收录已证实的问题。

按顺序采用首个命中的结论。

1. 有已证实的 P0，填 `BLOCKED (P0)`。保留其他未完成项。
2. 任一必测项为 `NOT_RUN`、全篇缺少已执行的相关检查，或 `RUNTIME` 范围没有实际运行观察，填 `INCOMPLETE`。在证据中说明补验条件。
3. 有已证实的 P1，填 `NEEDS_POLISH (P1)`。
4. 其余填 `PASS`。它只覆盖 `package`、`target` 和 `scope` 指定的范围。

例如仅要求 Web 静态评审，检查完按钮提交锁后可交付以下报告。

```json
{
  "schemaVersion": 1,
  "target": "WEB",
  "adapter": "BROWSER",
  "package": "apps/web",
  "scope": "STATIC",
  "verdict": "PASS",
  "findings": [],
  "evidence": [
    {
      "probeId": "W-B3.submit-lock",
      "kind": "STATIC",
      "required": true,
      "status": "PASS",
      "detail": "src/views/Order.vue:42 在提交入口检查 pending，且在异常和成功分支共用的 finally 中释放。"
    }
  ],
  "blindspots": []
}
```
