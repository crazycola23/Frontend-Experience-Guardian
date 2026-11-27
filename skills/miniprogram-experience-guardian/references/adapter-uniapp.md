# uni-app 微信端适配器 · UNIAPP

1. 从工作包启动脚本、用户指定的端或构建配置确认 `mp-weixin`，并找到实际的 `pages.json`、`manifest.json` 与 Vue 页面。HBuilderX 项目和 CLI 项目的源码位置可以不同。在 `unpackage/dist` 或 `dist` 看到 `app.json`，应沿构建关系回到源文件。
2. 判断受改动的 `#ifdef MP-WEIXIN`、`#ifndef`、组合条件及公共代码在微信构建中是否生效。只影响 H5 的分支交回 Web 路由；共用组件以此次目标版本的参数、布局与调用处为准。
3. 从 `pages.json` 的页面、`subPackages`、`tabBar` 配置识别实际导航容器。检查页面的 `onShow`、全局状态和数据服务。Vue 的挂载钩子在已有页面回到前台时可能不会重跑；列表刷新若由响应式 store 完成，应沿 store 的变更验证。
4. 对布局与视图更新，优先查看源 Vue 组件、主题变量、插槽和模板依赖。怀疑编译适配差异时再查看微信产物。微信端需要测量节点时用组件支持的选择器查询接口，如 `uni.createSelectorQuery()`；`document.querySelector()` 和 `window.history` 属于浏览器宿主。
