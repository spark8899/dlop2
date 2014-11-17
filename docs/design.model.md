# 简介
dlop是自己开发的运维管理平台，以flask+mysql为框架开发的。

flask链接：http://flask.pocoo.org/

web模板使用的sb-admin2，链接：http://startbootstrap.com/template-overviews/sb-admin-2/

# 设计思路
以CMDB为基础，运用流行的管理工具puppet和ansible支撑整个运维平台。


# 导航图

```bash
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
```

# 数据库设计

```bash
/*
   创建DLOP数据库
*/
CREATE SCHEMA IF NOT EXISTS `dlop` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;


/*
  创建相关表
*/
-- -----------------------------------------------------------------------------------
-- Table `user`
-- -----------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `user` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `username` VARCHAR(80) NOT NULL COMMENT '用户名',
  `is_enabled` BIT NOT NULL comment '账号是否启用',
  `email` VARCHAR(120) NULL comment '邮箱地址' ,
  `mobilephone` INT(11) NULL '手机号',
  `password` INT(11) NULL '用户密码',
  `role` INT(11) NULL '权限表',
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;


/*
  插入相关数据
*/


/*
  修改账号权限
*/
```

