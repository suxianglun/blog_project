
### 使用背景




### 参考资料


### 分支命名及使用规范

* 分支命名规范
	- 自己开发分支命名统一为 username ，如：yifeng
	- 分支两条主线为 Master分支和develop分支
	- Master作为发布分支，develop作为开发测试分支、自己开发分支从dev checkout出去，发布即 merge to master

* 分支合并规范
	- 从最新的develop分支checkout出自己的开发分支
	- 在自己开发开发分支开发完成后，先去develop分支pull最新代码，
	- 将develop 分支最新代码 merge 到自己分支，确保无冲突
	- 再切回develop分支merge自己开发分支代码，确保无冲突，且能正常运行

### commit 提交规范
* $git cz

* 用于说明 commit 的类别，只允许使用下面7个标识。

  - feat：新功能（feature）

  - fix：修补bug

  - docs：文档（documentation）

  - style： 格式（不影响代码运行的变动）

  - refactor：重构（即不是新增功能，也不是修改bug的代码变动）

  - test：增加测试

  - chore：构建过程或辅助工具的变动


### 代码规范
* 文件命名规范
	- 文件命名使用下划线命名法，如：hello_world
	- 请使用英文进行命名，不允许使用拼音。命名要求具有可读性，尽量避免使用缩写与数字
	- 未完待续

* 代码编码规范
	- 文件编码统一使用 UTF-8 编码；

### 文件目录结构(以LIb文件说明)

- lib
	- main.dart 入口文件
	- common 公共的method
	- components widget
	- generated
	- model 存放模型, 不应该加入逻辑层
	- router 路由
	- views 展示界面
	- widget (与components概念重合,废弃)
