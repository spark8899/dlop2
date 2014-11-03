# 简介
dlop是大乐游戏的运维管理平台，以flask+mysql为框架开发的。

flask链接：http://flask.pocoo.org/

web模板使用的sb-admin2，链接：http://startbootstrap.com/template-overviews/sb-admin-2/

# 设计思路
以CMDB为基础，运用流行的管理工具puppet和ansible支撑整个运维平台。


# 导航图

|-- 主页
|
|-- 资产管理
|   |
|   |-- 服务器管理
|   |
|   |-- 网络设备管理
|   |
|   |-- IDC管理
|   |
|   |-- 机型管理
|
|-- 项目管理
|   |
|   |-- 项目管理
|   |
|   |-- 项目模块管理
|
|-- 事件管理
|
|-- 脚本库
|
|-- 日志管理
