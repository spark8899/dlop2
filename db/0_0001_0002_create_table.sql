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
  `id` CHAR(8) comment '机型ID',
  `type` VARCHAR(80) comment '机型类型',
  `manufacturer` VARCHAR(80) NOT NULL COMMENT '厂商',
  `model` VARCHAR(120) NOT NULL COMMENT '设备型号',
  `cpu_name` VARCHAR(80) NULL comment 'cpu名称' ,
  `clock_speed` INT NULL comment 'cpu频率' ,
  `cpu_num` TINYINT NULL comment 'cpu数量' ,
  `memory_type` VARCHAR(80) NULL comment '内存型号',
  `memory_size` INT NULL comment '内存大小',
  `network_port` TINYINT NULL comment '网口数量',
  `harddisk_name` VARCHAR(80) NULL comment '硬盘名称',
  `harddisk_size` INT NULL comment '硬盘大小',
  `flashdisk_size` INT NULL comment '闪存大小',
  `raid_type` VARCHAR(80) NULL comment 'raid类型',
  `remote_manage_card` VARCHAR(80) NULL comment '远程管理卡名称',
  `virtual_type` VARCHAR(80) NULL comment '虚拟化类型',
  `unit` TINYINT NULL comment '机柜U数',
  `desc` VARCHAR(120) NULL comment '备注',
  PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;
