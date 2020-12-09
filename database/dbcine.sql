-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: dbcine
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `asiento`
--

DROP TABLE IF EXISTS `asiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asiento` (
  `idasiento` int NOT NULL AUTO_INCREMENT,
  `silla_numero` varchar(45) DEFAULT NULL,
  `fila_letras` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idasiento`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asiento`
--

LOCK TABLES `asiento` WRITE;
/*!40000 ALTER TABLE `asiento` DISABLE KEYS */;
INSERT INTO `asiento` VALUES (1,'1','A'),(2,'2','A'),(3,'3','A'),(4,'4','A'),(5,'5','A'),(6,'6','A'),(7,'7','A'),(8,'8','A'),(9,'9','A'),(10,'10','A'),(11,'11','A'),(12,'12','A'),(13,'13','A'),(14,'14','A'),(15,'15','A'),(16,'16','A');
/*!40000 ALTER TABLE `asiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boleto`
--

DROP TABLE IF EXISTS `boleto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `boleto` (
  `idboleto` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(45) DEFAULT NULL,
  `fecha` varchar(20) DEFAULT NULL,
  `hora` varchar(20) DEFAULT NULL,
  `compradetallada_idcompra` int NOT NULL,
  `sala_idsala` int NOT NULL,
  `peliculas_idpeliculas` int NOT NULL,
  `sucursal_idsucursal` int NOT NULL,
  `usuario_idusuario` int NOT NULL,
  PRIMARY KEY (`idboleto`),
  KEY `fk_boleto_sala1_idx` (`sala_idsala`),
  KEY `fk_boleto_peliculas1_idx` (`peliculas_idpeliculas`),
  KEY `fk_boleto_compra1_idx` (`compradetallada_idcompra`),
  KEY `fk_boleto_sucursal1_idx` (`sucursal_idsucursal`),
  KEY `fk_boleto_usuario1_idx` (`usuario_idusuario`),
  CONSTRAINT `fk_boleto_compra1` FOREIGN KEY (`compradetallada_idcompra`) REFERENCES `compradetallada` (`idcompra`),
  CONSTRAINT `fk_boleto_peliculas1` FOREIGN KEY (`peliculas_idpeliculas`) REFERENCES `peliculas` (`idpeliculas`),
  CONSTRAINT `fk_boleto_sala1` FOREIGN KEY (`sala_idsala`) REFERENCES `sala` (`idsala`),
  CONSTRAINT `fk_boleto_sucursal1` FOREIGN KEY (`sucursal_idsucursal`) REFERENCES `sucursal` (`idsucursal`),
  CONSTRAINT `fk_boleto_usuario1` FOREIGN KEY (`usuario_idusuario`) REFERENCES `usuario` (`idusuario`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boleto`
--

LOCK TABLES `boleto` WRITE;
/*!40000 ALTER TABLE `boleto` DISABLE KEYS */;
INSERT INTO `boleto` VALUES (1,'Niño 2D','10/10/2020','11:00 a. m.',1,1,2,1,2),(2,'Adulto 2D','10/10/2020','11:00 a. m.',1,1,2,1,2),(3,'Adulto 2D','10/10/2020','11:00 a. m.',1,1,2,1,2),(4,'Niño 3D','10/10/2020','11:15 a. m.',2,2,2,3,1),(5,'Niño 3D','10/10/2020','11:15 a. m.',2,2,2,3,1),(6,'Adulto 3D','10/10/2020','11:15 a. m.',2,2,2,3,1),(7,'Adulto 3D','15/10/2020','01:30 p. m.',3,4,3,2,2),(8,'Adulto 3D','15/10/2020','01:30 p. m.',3,4,3,2,2),(9,'Adulto 2D','27/11/2020','05:00 p. m.',4,3,1,1,3),(10,'Adulto 2D','27/11/2020','05:00 p. m.',5,3,1,3,1);
/*!40000 ALTER TABLE `boleto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boleto_asiento`
--

DROP TABLE IF EXISTS `boleto_asiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `boleto_asiento` (
  `idboleto_asiento` int NOT NULL AUTO_INCREMENT,
  `asiento_idasiento` int NOT NULL,
  `boleto_idboleto` int NOT NULL,
  PRIMARY KEY (`idboleto_asiento`),
  KEY `fk_boleto_asiento_asiento1_idx` (`asiento_idasiento`),
  KEY `fk_boleto_asiento_boleto1_idx` (`boleto_idboleto`),
  CONSTRAINT `fk_boleto_asiento_asiento1` FOREIGN KEY (`asiento_idasiento`) REFERENCES `asiento` (`idasiento`),
  CONSTRAINT `fk_boleto_asiento_boleto1` FOREIGN KEY (`boleto_idboleto`) REFERENCES `boleto` (`idboleto`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boleto_asiento`
--

LOCK TABLES `boleto_asiento` WRITE;
/*!40000 ALTER TABLE `boleto_asiento` DISABLE KEYS */;
INSERT INTO `boleto_asiento` VALUES (1,1,1),(2,2,1),(3,3,1),(4,7,2),(5,8,2),(6,9,2),(7,13,3),(8,14,3);
/*!40000 ALTER TABLE `boleto_asiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compradetallada`
--

DROP TABLE IF EXISTS `compradetallada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compradetallada` (
  `idcompra` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(100) DEFAULT NULL,
  `precios_unitarios` varchar(100) DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `monto_total` varchar(45) DEFAULT NULL,
  `estado` varchar(45) DEFAULT NULL,
  `usuario_idusuario` int NOT NULL,
  PRIMARY KEY (`idcompra`),
  KEY `fk_compradetallada_usuario1_idx` (`usuario_idusuario`),
  CONSTRAINT `fk_compradetallada_usuario1` FOREIGN KEY (`usuario_idusuario`) REFERENCES `usuario` (`idusuario`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compradetallada`
--

LOCK TABLES `compradetallada` WRITE;
/*!40000 ALTER TABLE `compradetallada` DISABLE KEYS */;
INSERT INTO `compradetallada` VALUES (1,'1 Niño 2D, 2 Adulto 2D ','3.50, 4.00',3,'11.50','Finalizada',1),(2,'2 Niño 3D, 1 Adulto 3D','4.50, 5.00',3,'14.00','Finalizada',2),(3,'2 Adulto 3D','5.00',2,'10.00','Finalizada',3),(4,NULL,NULL,NULL,NULL,NULL,0),(5,NULL,NULL,NULL,NULL,NULL,0),(6,NULL,NULL,NULL,NULL,NULL,0);
/*!40000 ALTER TABLE `compradetallada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `peliculas`
--

DROP TABLE IF EXISTS `peliculas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `peliculas` (
  `idpeliculas` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(45) DEFAULT NULL,
  `descripcion` varchar(10000) DEFAULT NULL,
  `fecha` varchar(20) DEFAULT NULL,
  `hora` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`idpeliculas`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peliculas`
--

LOCK TABLES `peliculas` WRITE;
/*!40000 ALTER TABLE `peliculas` DISABLE KEYS */;
INSERT INTO `peliculas` VALUES (1,'Fuga de Pretoria','Fuga de Pretoria es la historia real de Tim Jenkin y Stephen Lee, jóvenes sudafricanos blancos marcados como \"terroristas\", y encarcelados en 1978 por trabajar en operaciones encubiertas para el prohibido ANC de Nelson Mandela. ¡Encarcelados en una prisión de máxima seguridad de Pretoria, deciden enviar un mensaje claro al régimen del apartheid y escapar! Con un ingenio impresionante, vigilancia meticulosa y llaves de madera diseñadas para 10 puertas de acero, apuestan por la libertad. Actores: Daniel Radcliffe, Daniel Webber, Ian Hart. Director: Francis Annan. Clasificación: AA. Género: Drama/Thriller. Duración: 106 minutos','07/10/2020','02:00 p. m.'),(2,'¡Scooby!','¡Scooby! revela cómo se conocieron los amigos de toda la vida Scooby y Shaggy, y cómo se unieron con los jóvenes detectives Fred, Velma y Daphne para formar Mystery Inc. Ahora, con cientos de casos resueltos y aventuras compartidas, Scooby y la pandilla se enfrentan al misterio más desafiante de todos los tiempos: una trama para liberar Cerberus, el perro fantasma, sobre el mundo. Mientras compiten para detener este “perrocalipsis\" global, la pandilla descubre que Scooby tiene un legado secreto y un gran y épico destino que nadie imaginaba. Director: Tony Cervone. Clasificación: A. Género: Animación. Duración: 93 minutos','10/10/2020','11:30 a. m.'),(3,'Mientras estés conmigo','Cuenta la historia real de la estrella de música cristiana Jeremy Camp, profundizando en su aventura de amor y pérdida, demostrando así que siempre hay esperanza. Actores: Gary Sinise,Nathan Parsons,Britt Robertson,K.J. Apa. Directores: Andrew Erwin, Jon Erwin. Clasificación: A. Género: Drama. Duración: 110 minutos','13/10/2020','05:00 p. m.');
/*!40000 ALTER TABLE `peliculas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `peliculas_sucursal`
--

DROP TABLE IF EXISTS `peliculas_sucursal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `peliculas_sucursal` (
  `idpeliculas_sucursal` int NOT NULL AUTO_INCREMENT,
  `peliculas_idpeliculas` int NOT NULL,
  `sucursal_idsucursal` int NOT NULL,
  PRIMARY KEY (`idpeliculas_sucursal`),
  KEY `fk_peliculas_sucursal_peliculas1_idx` (`peliculas_idpeliculas`),
  KEY `fk_peliculas_sucursal_sucursal1_idx` (`sucursal_idsucursal`),
  CONSTRAINT `fk_peliculas_sucursal_peliculas1` FOREIGN KEY (`peliculas_idpeliculas`) REFERENCES `peliculas` (`idpeliculas`),
  CONSTRAINT `fk_peliculas_sucursal_sucursal1` FOREIGN KEY (`sucursal_idsucursal`) REFERENCES `sucursal` (`idsucursal`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peliculas_sucursal`
--

LOCK TABLES `peliculas_sucursal` WRITE;
/*!40000 ALTER TABLE `peliculas_sucursal` DISABLE KEYS */;
INSERT INTO `peliculas_sucursal` VALUES (1,1,1),(2,2,1),(3,3,1),(4,1,2),(5,2,2),(6,3,2),(7,1,3),(8,2,3),(9,3,3);
/*!40000 ALTER TABLE `peliculas_sucursal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sala`
--

DROP TABLE IF EXISTS `sala`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sala` (
  `idsala` int NOT NULL AUTO_INCREMENT,
  `capacidad` int DEFAULT NULL,
  `tipo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idsala`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sala`
--

LOCK TABLES `sala` WRITE;
/*!40000 ALTER TABLE `sala` DISABLE KEYS */;
INSERT INTO `sala` VALUES (1,180,'2D'),(2,180,'3D'),(3,180,'2D'),(4,180,'3D');
/*!40000 ALTER TABLE `sala` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sala_peliculas`
--

DROP TABLE IF EXISTS `sala_peliculas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sala_peliculas` (
  `sala_peliculas` int NOT NULL AUTO_INCREMENT,
  `peliculas_idpeliculas` int NOT NULL,
  `sala_idsala` int NOT NULL,
  PRIMARY KEY (`sala_peliculas`),
  KEY `fk_sala_peliculas_peliculas1_idx` (`peliculas_idpeliculas`),
  KEY `fk_sala_peliculas_sala1_idx` (`sala_idsala`),
  CONSTRAINT `fk_sala_peliculas_peliculas1` FOREIGN KEY (`peliculas_idpeliculas`) REFERENCES `peliculas` (`idpeliculas`),
  CONSTRAINT `fk_sala_peliculas_sala1` FOREIGN KEY (`sala_idsala`) REFERENCES `sala` (`idsala`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sala_peliculas`
--

LOCK TABLES `sala_peliculas` WRITE;
/*!40000 ALTER TABLE `sala_peliculas` DISABLE KEYS */;
INSERT INTO `sala_peliculas` VALUES (1,1,3),(2,2,1),(3,2,2),(4,3,4);
/*!40000 ALTER TABLE `sala_peliculas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sucursal`
--

DROP TABLE IF EXISTS `sucursal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sucursal` (
  `idsucursal` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `departamento` varchar(45) DEFAULT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idsucursal`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sucursal`
--

LOCK TABLES `sucursal` WRITE;
/*!40000 ALTER TABLE `sucursal` DISABLE KEYS */;
INSERT INTO `sucursal` VALUES (1,'Cinépolis Galerías','San Salvador','3er nivel, Paseo Gral. Escalón, San Salvador'),(2,'Cinépolis Multiplaza','San Salvador','Carretera Panamericana 503, San Salvador'),(3,'Cinépolis Metrocentro Santa Ana','Santa Ana','Colonia Loma Linda, final avenida Independencia Sur y by pass, Santa Ana, El Salvador');
/*!40000 ALTER TABLE `sucursal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `idusuario` int NOT NULL AUTO_INCREMENT,
  `user` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idusuario`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Melanie Nicole Argueta Carías','melanie123@hotmail.com','Melanie123'),(2,'Mónica Valeria Avelar Reyes','valery10@gmail.com','valery_ar'),(3,'David Omar Guzmán Rivera','davguz@gmail.com','davidguzman00');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-08 17:56:59
