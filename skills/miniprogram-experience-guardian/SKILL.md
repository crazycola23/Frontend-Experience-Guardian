---
name: miniprogram-experience-guardian
description: 微信原生小程序和 uni-app 的 mp-weixin 端体验守卫。开发相关页面、组件与交互时静默应用规则，评审时按证据检查安全区、异步布局、权限和页面栈。uni-app 的 H5 交给 Web 守卫。
---

# 微信小程序体验守卫

按[目标路由](references/guardian-routing.md)确认受改动影响的包和构建目标。命中微信小程序时使用 `MINIPROGRAM`；按源代码选[微信原生 WX_NATIVE](references/adapter-wx-native.md) 或 [uni-app UNIAPP](references/adapter-uniapp.md)。同仓的独立 Web 应用单独判定。

- **普通实现**　只把[平台规则](references/mini-invariants.md)中与本次改动相关的约束用于设计和代码，沿用任务原有交付格式。
- **Matt 双轴评审**　在 Standards 或 Spec 中归入有证据的体验问题，一处问题记录一次。遵循原评审格式。
- **点名体验评审**　默认只读静态审查。沿受影响的用户操作追到源码分支和可观察后果，按[共同报告协议](references/guardian-contract.md)输出完整报告。用户要求修复时再动相应代码。

用户明确要求实测时，再读[运行验证](references/optional-runtime.md)选择覆盖该行为的验证方法。
