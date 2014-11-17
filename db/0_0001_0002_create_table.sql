-- -----------------------------------------------------------------------------------
-- Table `user`
-- -----------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `user` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `username` VARCHAR(80) NOT NULL COMMENT '用户名',
  `is_enabled` BIT NOT NULL comment '账号是否启用',
  `email` VARCHAR(120) NULL comment '邮箱地址' ,
  `mobilephone` INT(11) NULL comment '手机号',
  `password` INT(11) NULL comment '用户密码',
  `role` INT(11) NULL  comment '权限表',
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

-- -----------------------------------------------------------------------------------
-- Table `server_model`
-- -----------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `config_model` (
  `config_id` CHAR(4) comment '配置ID',
  `type` VARCHAR(80) NOT NULL COMMENT '服务器型号',
  `brand` VARCHAR(80) NOT NULL COMMENT '厂商',
  `cpu_name` VARCHAR(80) NULL comment 'cpu名称' ,
  `clock_speed` INT NULL comment 'cpu频率' ,
  `cpu_num` TINYINT NULL comment 'cpu数量' ,
  `memory_type` VARCHAR(20) NULL comment '内存型号',
  `memory_size` INT NULL comment '内存大小',
  `netcard_num` TINYINT NULL comment '网卡数量',
  `harddisk_name` VARCHAR(80) NULL comment '硬盘名称',
  `harddisk_size` TINYINT NULL comment '硬盘大小',
  `raid_type` VARCHAR(80) NULL comment 'raid类型',
  `remote_manage_card` VARCHAR(80) NULL comment '远程管理卡名称',
  `virtual_type` VARCHAR(80) NULL  comment '虚拟化类型',
  `unit` TINYINT NULL  comment '服务器大小U数',
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

-- -----------------------------------------------------------------------------------
-- Table `network_model`
-- -----------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `config_model` (
  `config_id` CHAR(4) comment '配置ID',
  `type` VARCHAR(80) NOT NULL COMMENT '网络型号',
  `brand` VARCHAR(80) NOT NULL COMMENT '厂商',
  `cpu_name` VARCHAR(80) NULL comment 'cpu名称' ,
  `clock_speed` INT NULL comment 'cpu频率' ,
  `cpu_num` TINYINT NULL comment 'cpu数量' ,
  `memory_size` INT NULL comment '内存大小',
  `netcard_num` TINYINT NULL comment '网卡数量',
  `harddisk_name` VARCHAR(80) NULL comment '硬盘名称',
  `harddisk_size` TINYINT NULL comment '硬盘大小',
  `raid_type` VARCHAR(80) NULL comment 'raid类型',
  `remote_manage_card` VARCHAR(80) NULL comment '远程管理卡名称',
  `virtual_type` VARCHAR(80) NULL  comment '虚拟化类型',
  `unit` TINYINT NULL  comment '服务器大小U数',
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;
