-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: localhost    Database: virtugaming
-- ------------------------------------------------------
-- Server version	5.7.11-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `session`
--

DROP TABLE IF EXISTS `session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `session` (
  `user_id` int(11) DEFAULT NULL,
  `session_id` varchar(200) NOT NULL,
  `creation_date` datetime DEFAULT NULL,
  `expiration_date` datetime DEFAULT NULL,
  `ip_address` varchar(45) DEFAULT NULL,
  `device_name` varchar(45) DEFAULT NULL,
  `is_remember_me` int(1) DEFAULT NULL,
  PRIMARY KEY (`session_id`),
  KEY `user_id_idx` (`user_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session`
--

LOCK TABLES `session` WRITE;
/*!40000 ALTER TABLE `session` DISABLE KEYS */;
INSERT INTO `session` VALUES (1,'3Ivt1Pwy8rWwPi2tbfDdaLPTo6mWn7SKjhNllzrn','2016-06-09 23:41:35','2016-06-10 23:41:35','127.0.0.1','Desktop 1',0),(1,'9DGdGNPPCVFhCRM751Xz30KDFo72CTo0kY','2016-06-08 17:15:01','2016-06-09 17:15:01','127.0.0.1','Desktop 1',0),(1,'h0cGjsOvmcPJpM4Q37coh0lAkkTEImklA','2016-06-08 17:18:08','2016-06-09 17:18:08','127.0.0.1','Desktop 1',0),(2,'nGBAuxH0PKRQe0zBgKUIhxbMKx9D30K4hxSelhoiPGAZO','2016-07-13 20:03:08','2016-07-14 20:03:08','127.0.0.1','Desktop 1',0),(1,'WC7mi2DvbjWjYa0PMvZS6eFsPAq3zna0knhqy','2016-06-09 23:42:54','2016-06-10 23:42:54','127.0.0.1','Desktop 1',0),(1,'xaGP6oX0iD7Gz5qSmXao2xAXNPqx1WYFVwVe3','2016-07-10 03:29:32','2016-07-11 03:29:32','127.0.0.1','Desktop 1',0);
/*!40000 ALTER TABLE `session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-13 21:05:52
