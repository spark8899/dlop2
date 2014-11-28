/*
-- -----------------------------------------------------------------------------------
-- Table `user`
-- -----------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `user` (
  `user_id` INT NOT NULL AUTO_INCREMENT ,
  `username` VARCHAR(80) NOT NULL COMMENT '用户名',
  `is_enabled` BIT NOT NULL comment '账号是否启用',
  `email` VARCHAR(120) NULL comment '邮箱地址' ,
  `mobilephone` INT(11) NULL comment '手机号',
  `password` VARCHAR(80) NULL comment '用户密码',
  `role` INT(11) NULL  comment '权限表',
  PRIMARY KEY (`user_id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;
*/

-- -----------------------------------------------------------------------------------
-- Table `asset_model`
-- -----------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `asset_model` (
  `id` CHAR(8) comment '编码',
  `type` VARCHAR(80) NOT NULL comment '类型',
  `manufacturer` VARCHAR(80) NOT NULL COMMENT '厂商',
  `model` VARCHAR(120) NOT NULL COMMENT '设备型号',
  `cpu_model` VARCHAR(80) NULL comment 'cpu型号' ,
  `cpu_num` TINYINT UNSIGNED NULL comment 'cpu数量' ,
  `memory_size` INT UNSIGNED NULL comment '内存大小',
  `netcard_num` TINYINT unsigned NULL comment '网口数量',
  `harddisk` VARCHAR(80) NULL comment '硬盘',
  `flashdisk` VARCHAR(80) NULL comment '闪存',
  `raid` VARCHAR(80) NULL comment 'RAID',
  `remote_manage` VARCHAR(80) NULL comment '远程管理',
  `virtual` VARCHAR(80) NULL comment '虚拟化',
  `unit` TINYINT UNSIGNED NULL comment '高度',
  `desc` VARCHAR(240) NULL comment '备注',
  PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- -----------------------------------------------------------------------------------
-- Table `asset_idc`
-- -----------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `asset_idc` (
  `id` CHAR(8) comment '编码',
  `bandwidth` VARCHAR(120) NULL comment '带宽',
  `rack_num` INT UNSIGNED NULL comment '机柜数量',
  `rack_code` VARCHAR(120) NULL comment '机柜编号',
  `lan_ip` VARCHAR(120) NULL comment '内网网段',
  `wan_ip` VARCHAR(120) NULL comment '外网网段',
  `location` VARCHAR(120) NULL comment '详细地址',
  `telephone` VARCHAR(20) NULL comment '电话',
  `auth_code` VARCHAR(120) NULL comment '验证码',
  `tax` VARCHAR(20) NULL comment '传真',
  `desc` VARCHAR(240) NULL comment '备注',
  PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;
