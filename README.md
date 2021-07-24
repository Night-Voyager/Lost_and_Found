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

