# Frontend Experience Guardian

一套面向编码助手的前端体验守卫。根据改动所属的应用和构建目标选择 Skill；同一份 uni-app 源码可以分别接受浏览器和微信小程序评审。

| Skill | 适用目标 | 典型检查 |
| --- | --- | --- |
| [web-experience-guardian](skills/web-experience-guardian/SKILL.md) | 浏览器应用、uni-app H5 | 异步布局、键盘与焦点、浏览器返回后的筛选和列表状态 |
| [miniprogram-experience-guardian](skills/miniprogram-experience-guardian/SKILL.md) | 原生微信、uni-app mp-weixin | 安全区与胶囊、权限初始化、返回页面后的数据同步 |

## 安装与迁移

通过 Skills CLI 安装需要的一端或两端：

~~~sh
npx skills add crazycola23/Frontend-Experience-Guardian --skill web-experience-guardian miniprogram-experience-guardian
~~~

手动安装时，将 `skills/` 下所需的**整个子目录**复制到助手的技能目录，每个目录都包含自己的规则和报告协议。以前安装了 `frontend-experience-guardian` 的用户，升级时将旧目录移出技能发现路径，原来显式调用旧名称的指令改用对应平台的新名称。

## 在任务中使用

- **普通实现**：改动触及哪个用户操作，就应用对应规则。只改文案时，沿用现有交付方式。
- **常规代码评审**：沿用调用方的报告格式。Matt 双轴评审将仓库规范和有改前改后证据的体验回归纳入 Standards，将工单承诺或差异额外改变的行为纳入 Spec。
- **专门体验评审**：默认静态、只读，输出统一报告。例如“评审微信端编辑评级后返回列表的体验”。
- **明确要求实测**：按需读取对应平台的运行参考。报告区分静态和运行证据；必测步骤无法完成时保留原因。

浏览器端的键盘、路由和布局等案例见 [Web 评审场景](skills/web-experience-guardian/evals/README.md)。两套独立安装包携带同一份[平台路由](skills/web-experience-guardian/references/guardian-routing.md)、[报告契约](skills/web-experience-guardian/references/guardian-contract.md)和 [JSON Schema](skills/web-experience-guardian/references/guardian-report.schema.json)。

维护者可以用[双端试用场景](tests/review-scenarios.md)复核普通开发、代码评审和实测验收的行为。

[MIT License](LICENSE)
