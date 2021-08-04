# 失物招领平台

本平台是一个集中收集并展示校内失物招领与寻物启事信息的微信小程序，将原本分散与各个失物招领处和学生之间转发的信息整合起来，便于失主发布失物信息并查看他人拾得的失物，也便于拾得失物的人与失主取得联系。



## 目录结构

本文件所在文件夹下包含三个文件夹：

- frontend
- backend
- database



### frontend

`frontend`文件夹下为前端微信小程序工程文件。

**请注意：项目中以下信息已经[数据删除]，请根据需要填写自己的信息。**

- `frontend\Lost&Found\app.js`
  - `App.globalData.serverURL`：后端服务器IP地址或域名



### backend

`backend`文件夹下为后端Django REST framework工程文件。

在`backend\Lost\media\images`路径下存放的是先前开发时上传的测试图片，没有删除，用以体现后端对保存的文件的管理。

**请注意：项目中以下信息已经[数据删除]，请根据需要填写自己的信息。**

- `backend\Lost\Lost\settings.py`
  - `DATABASES.default.USER`：数据库用户名
  - `DATABASES.default.PASSWORD`：数据库密码
- `backend\Lost\apps\users\views.py`
  - `class GetOpenid(object):`
    - `appId`：微信小程序appId
    - `appSecret`：微信小程序appSecret
- `backend\Lost\apps\miniprogramAPI\views.py`
  - `class Auth(object):`
    - `appId`：微信小程序appId
    - `appSecret`：微信小程序appSecret
  - `class Test(APIView):`
    - `def get(self, request):`
      - `image`：测试用图保存路径，此处原本使用的是小程序审核人员提供的习主席照片



### database

`database`文件夹下为数据库结构设计图及相应sql文件。Sql文件中仅含有表结构，不含有数据。所以当运行项目时，后端返回的会是空数据。如果在启动项目时遇到报错，可参考[这篇文章](https://www.jianshu.com/p/1e1c7e4290f7)。



## 如何使用

### 方法一（推荐）

此方法相对复杂，但可以使用完整功能。

1. 创建数据库并导入数据。可参考[此文档](https://www.jianshu.com/p/1e1c7e4290f7)。
2. 在数据库的`users_student`表中插入一条带有`name (varchar(11))`和`studentID (int)`两个字段的数据，其余字段留空。此数据将用于身份验证和账号绑定。
3. 填写上述“目录结构”部分提及的[数据删除]的数据。请使用者根据自身具体情况进行填写。
4. 运行后端项目。若遇到问题，也可参考[此文档](https://www.jianshu.com/p/1e1c7e4290f7)。
5. 运行小程序。若情况正常，显示的应当是“用户信息”页面。填写步骤2中插入数据库的数据进行首次登录。若成功登录，则用户身份信息已与微信账号绑定，之后同一微信账号不再需要进行登录操作。

### 方法二

此方法相对简单，但仅能使用小程序部分，且功能不完整。

1. [添加编译模式](https://developers.weixin.qq.com/miniprogram/dev/devtools/debug.html#自定义编译)，将`启动页面`改为`pages/index/index`。
2. 编译小程序即可使用。



## 关于功能

### 已完成的部分

- 失物信息的填写、提交、查看和删除
- 用户校验
  - 身份认证
    - 限制仅校内人员可加入平台
  - 自动登录
    - 首次登录时后台会自动将所填信息与微信进行绑定
    - 已成功登陆过的用户无论是否更换设备，都可以根据微信号判断身份并自动登录
- 内容审核
  - 自动校验用户发布文本、图片等内容是否违规
  - 自动拦截敏感内容
  - 目的是降低平台被恶意利用导致传播违规内容的风险

### 未实现的想法

- 微信推送提醒
  - 使用小程序[“模板消息”功能](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/template-message.html)（已于2020年1月10日下线，小程序官方建议使用[“订阅消息”功能](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/subscribe-message.html)），及时提醒用户：
    - 在平台上发布的“寻物启事”所提到的物品被人拾到；
    - 有人在平台上发布了“失物招领”，失主信息被识别。
  - 用户将能在微信中收到一条消息，给出上述信息，了解失物的情况。
  - 模板消息/订阅消息推送位置：服务通知。
- 表单自动填充
  - 一些重复性高、变化可能性低的信息（例如联系方式），在用户第一次填写提交后，可由后台保存，今后默认自动填写。
  - 须添加设置，允许用户选择不需要平台保存过多个人信息。
- 物品信息识别
  - 识别所上传的图片包含的是什么物品，并将物品名称自动填入表单。
  - 如果上传的是一张饭卡的图片，识别饭卡上的姓名与学号。若识别到是已经加入平台的用户，通过服务通知进行微信推送提醒。
  - 允许支持NFC的手机读取饭卡信息用以自动填写表单。（不知饭卡是否支持。若可行，此功能也可用于用户登录。）
- 代码优化
  - 一个历史遗留问题
    - 先开发的用户校验功能，使用了小程序的API。之后在开发内容审核功能时才知道也需要使用小程序的API，使得与小程序API相关的代码没有得到统一管理。
    - 希望将来能将用户校验部分关于小程序API的代码移动到叫`miniprogramAPI`的`Django app`下。
