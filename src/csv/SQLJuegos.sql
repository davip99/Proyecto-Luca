USE `railway`;

CREATE  TABLE IF NOT EXISTS `Juegos` (
  `id`INT NOT NULL AUTO_INCREMENT,
  `rank` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `platform` VARCHAR(255) NOT NULL ,
  `year` INT NULL,
  `genre` VARCHAR(255) NOT NULL,
  `publisher` VARCHAR(255) NOT NULL,
  `na_sales` FLOAT NOT NULL,
  `eu_sales` FLOAT NOT NULL,
  `jp_sales` FLOAT NOT NULL,
  `other_sales` FLOAT NOT NULL,
  `global_sales` FLOAT NOT NULL,
  PRIMARY KEY (`id`) );
  
SELECT AVG(na_sales) FROM `Juegos`