# Update



本功能由文档维护者依据 [教程](https://www.bilibili.com/video/BV188spztEZL) 复现，用来Unity的Update功能。

使用方法：Update节点会暴露一个deltaTime的节点，以及一个出节点供使用。

配置必看：
- 创建一个名为 `Update` 的全局计时器，并且准确的配置在关卡实体上。
- 在关卡实体上，挂载 `InitUpdate` 的节点图。
- 在需要使用Update的节点图内，添加一个名为 `Time` 的节点图变量，类型为浮点数。
- 如果不想执行上一步，可将 `UpdateNeeded` 节点图自行改名使用。
- 如果对前面的内容有疑问，参考参考存档进行配置。


