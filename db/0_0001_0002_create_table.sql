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


