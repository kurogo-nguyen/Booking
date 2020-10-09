-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.5.6-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for booking_db
CREATE DATABASE IF NOT EXISTS `booking_db` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `booking_db`;

-- Dumping structure for table booking_db.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.auth_group: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

-- Dumping structure for table booking_db.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.auth_group_permissions: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;

-- Dumping structure for table booking_db.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.auth_permission: ~24 rows (approximately)
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
REPLACE INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;

-- Dumping structure for table booking_db.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.auth_user: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

-- Dumping structure for table booking_db.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.auth_user_groups: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;

-- Dumping structure for table booking_db.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.auth_user_user_permissions: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;

-- Dumping structure for table booking_db.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.django_admin_log: ~0 rows (approximately)
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;

-- Dumping structure for table booking_db.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.django_content_type: ~6 rows (approximately)
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
REPLACE INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(5, 'contenttypes', 'contenttype'),
	(6, 'sessions', 'session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

-- Dumping structure for table booking_db.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.django_migrations: ~18 rows (approximately)
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
REPLACE INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2020-10-09 17:11:18.668264'),
	(2, 'auth', '0001_initial', '2020-10-09 17:11:18.900103'),
	(3, 'admin', '0001_initial', '2020-10-09 17:11:19.491346'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2020-10-09 17:11:19.628439'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-10-09 17:11:19.649713'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2020-10-09 17:11:19.757103'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2020-10-09 17:11:19.847611'),
	(8, 'auth', '0003_alter_user_email_max_length', '2020-10-09 17:11:19.924836'),
	(9, 'auth', '0004_alter_user_username_opts', '2020-10-09 17:11:19.934844'),
	(10, 'auth', '0005_alter_user_last_login_null', '2020-10-09 17:11:19.996751'),
	(11, 'auth', '0006_require_contenttypes_0002', '2020-10-09 17:11:20.000582'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2020-10-09 17:11:20.012548'),
	(13, 'auth', '0008_alter_user_username_max_length', '2020-10-09 17:11:20.034177'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2020-10-09 17:11:20.057148'),
	(15, 'auth', '0010_alter_group_name_max_length', '2020-10-09 17:11:20.157668'),
	(16, 'auth', '0011_update_proxy_permissions', '2020-10-09 17:11:20.168772'),
	(17, 'auth', '0012_alter_user_first_name_max_length', '2020-10-09 17:11:20.190856'),
	(18, 'sessions', '0001_initial', '2020-10-09 17:11:20.230390');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;

-- Dumping structure for table booking_db.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.django_session: ~0 rows (approximately)
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

-- Dumping structure for table booking_db.hotels
CREATE TABLE IF NOT EXISTS `hotels` (
  `hNo` int(11) NOT NULL AUTO_INCREMENT,
  `hName` varchar(50) NOT NULL,
  `hAddress` varchar(50) NOT NULL,
  `city` varchar(20) NOT NULL,
  `country` varchar(15) NOT NULL,
  `hPhone` int(11) NOT NULL,
  `hManager` int(11) DEFAULT NULL,
  PRIMARY KEY (`hNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.hotels: ~0 rows (approximately)
/*!40000 ALTER TABLE `hotels` DISABLE KEYS */;
/*!40000 ALTER TABLE `hotels` ENABLE KEYS */;

-- Dumping structure for table booking_db.reservations
CREATE TABLE IF NOT EXISTS `reservations` (
  `rID` int(11) NOT NULL AUTO_INCREMENT,
  `hid` int(11) NOT NULL,
  `uID` int(11) NOT NULL,
  `date-from` date NOT NULL,
  `date-to` date NOT NULL,
  `cost` int(11) NOT NULL DEFAULT 0,
  `deposit` int(11) NOT NULL DEFAULT 0,
  `tradingCode` int(11) NOT NULL DEFAULT 0,
  `time` datetime NOT NULL,
  PRIMARY KEY (`rID`,`tradingCode`),
  UNIQUE KEY `reservations_rID_uindex` (`rID`),
  UNIQUE KEY `reservations_tradingCode_uindex` (`tradingCode`),
  KEY `reservations_hotels_hNo_fk` (`hid`),
  KEY `reservations_user_uID_fk` (`uID`),
  CONSTRAINT `reservations_hotels_hNo_fk` FOREIGN KEY (`hid`) REFERENCES `hotels` (`hNo`),
  CONSTRAINT `reservations_user_uID_fk` FOREIGN KEY (`uID`) REFERENCES `user` (`uID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.reservations: ~0 rows (approximately)
/*!40000 ALTER TABLE `reservations` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservations` ENABLE KEYS */;

-- Dumping structure for table booking_db.reservation_detail
CREATE TABLE IF NOT EXISTS `reservation_detail` (
  `rID` int(11) NOT NULL,
  `roomType` enum('0','1','2') NOT NULL,
  `quantity` int(11) NOT NULL,
  `hID` int(11) DEFAULT NULL,
  PRIMARY KEY (`roomType`,`rID`),
  KEY `reservation_detail_reservations_rID_fk` (`rID`),
  KEY `reservation_detail_room_roomType_hId_fk` (`roomType`,`hID`),
  CONSTRAINT `reservation_detail_reservations_rID_fk` FOREIGN KEY (`rID`) REFERENCES `reservations` (`rID`),
  CONSTRAINT `reservation_detail_room_roomType_hId_fk` FOREIGN KEY (`roomType`, `hID`) REFERENCES `room` (`roomType`, `hId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.reservation_detail: ~0 rows (approximately)
/*!40000 ALTER TABLE `reservation_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservation_detail` ENABLE KEYS */;

-- Dumping structure for table booking_db.reviews
CREATE TABLE IF NOT EXISTS `reviews` (
  `reID` int(11) NOT NULL,
  `title` varchar(20) DEFAULT NULL,
  `rating` enum('1','2','3','4','5') NOT NULL,
  `comment` varchar(500) DEFAULT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`reID`),
  UNIQUE KEY `reviews_reID_uindex` (`reID`),
  CONSTRAINT `reviews_reservations_rID_fk` FOREIGN KEY (`reID`) REFERENCES `reservations` (`rID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.reviews: ~0 rows (approximately)
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;

-- Dumping structure for table booking_db.room
CREATE TABLE IF NOT EXISTS `room` (
  `hId` int(11) NOT NULL,
  `roomType` enum('0','1','2') NOT NULL,
  `rQuantity` int(11) NOT NULL,
  `rImg` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`roomType`,`hId`),
  UNIQUE KEY `room_hId_uindex` (`hId`),
  CONSTRAINT `room_hotels_hNo_fk` FOREIGN KEY (`hId`) REFERENCES `hotels` (`hNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.room: ~0 rows (approximately)
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
/*!40000 ALTER TABLE `room` ENABLE KEYS */;

-- Dumping structure for table booking_db.user
CREATE TABLE IF NOT EXISTS `user` (
  `uID` int(11) NOT NULL AUTO_INCREMENT,
  `uEmail` varchar(30) NOT NULL,
  `uPassword` varchar(20) NOT NULL,
  `uName` varchar(50) NOT NULL,
  `uAvatar` varchar(50) DEFAULT NULL,
  `uPhone` int(11) DEFAULT NULL,
  `Bank` enum('VietcomBank','BIDV','VPBank','') DEFAULT NULL,
  `uBank` int(11) DEFAULT NULL,
  PRIMARY KEY (`uID`,`uEmail`),
  UNIQUE KEY `user_uEmail_uindex` (`uEmail`),
  UNIQUE KEY `user_uID_uindex` (`uID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table booking_db.user: ~0 rows (approximately)
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
