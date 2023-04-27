-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Usuario` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(200) NOT NULL,
  `email` VARCHAR(200) NOT NULL,
  `rua` VARCHAR(200) NOT NULL,
  `numero` INT NOT NULL,
  `bairro` VARCHAR(200) NOT NULL,
  `cep` VARCHAR(45) NOT NULL,
  `cidade` VARCHAR(48) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Plano`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Plano` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `valor` INT NOT NULL,
  `categoria` VARCHAR(20) NOT NULL,
  `Usuario_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Plano_Usuario_idx` (`Usuario_id` ASC) ,
  CONSTRAINT `fk_Plano_Usuario`
    FOREIGN KEY (`Usuario_id`)
    REFERENCES `mydb`.`Usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Catalogo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Catalogo` (
  `codigo` BIGINT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(200) NOT NULL,
  `genero` VARCHAR(100) NOT NULL,
  `sinopse` VARCHAR(500) NOT NULL,
  `duracao` TIME NOT NULL,
  `dt_lancamento` DATE NOT NULL,
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Usuario_has_Catalogo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Usuario_has_Catalogo` (
  `Usuario_id` BIGINT NOT NULL,
  `Catalogo_codigo` BIGINT NOT NULL,
  PRIMARY KEY (`Usuario_id`, `Catalogo_codigo`),
  INDEX `fk_Usuario_has_Catalogo_Catalogo1_idx` (`Catalogo_codigo` ASC) ,
  INDEX `fk_Usuario_has_Catalogo_Usuario1_idx` (`Usuario_id` ASC) ,
  CONSTRAINT `fk_Usuario_has_Catalogo_Usuario1`
    FOREIGN KEY (`Usuario_id`)
    REFERENCES `mydb`.`Usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_has_Catalogo_Catalogo1`
    FOREIGN KEY (`Catalogo_codigo`)
    REFERENCES `mydb`.`Catalogo` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
