# 微信原生适配器 · WX_NATIVE

1. 从目标 `project.config.json` 的 `miniprogramRoot` 解出小程序根，再读根下 `app.json` 的页面、分包与 TabBar。自定义构建目录或同仓示例要回溯至实际维护的源文件。
2. 布局顺序从页面 WXML、公共壳、组件 WXSS 追到页面配置。区分 `navigationStyle: "custom"` 和系统导航、`tabBar.custom` 和系统底栏。在组件样式隔离时，确认命中的选择器确实作用于该节点。
3. 状态从 `App.onLaunch` 的鉴权流程追到页面 `onLoad` / `onShow` 和真正的请求入口。异步初始化要有页面可等待或订阅的就绪信号；在 `onLaunch` 声明 `async` 并不能据此推断首屏已经等待。列表返回可用共享模型、`eventChannel` 或重新拉取。
4. 用实际 `tabBar.list` 解析跳转目标。跳 Tab 可用 `wx.switchTab`，普通页面可用 `wx.navigateTo`。对自定义返回，再看 `getCurrentPages()` 长度为 1 时的出口。检查 `setData` 时追踪数据实际变化的字段及调用频率。
