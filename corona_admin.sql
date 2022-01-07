-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 07, 2022 at 08:26 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `corona_admin`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
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
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add admin_user', 7, 'add_admin_user'),
(26, 'Can change admin_user', 7, 'change_admin_user'),
(27, 'Can delete admin_user', 7, 'delete_admin_user'),
(28, 'Can view admin_user', 7, 'view_admin_user'),
(29, 'Can add category', 8, 'add_category'),
(30, 'Can change category', 8, 'change_category'),
(31, 'Can delete category', 8, 'delete_category'),
(32, 'Can view category', 8, 'view_category'),
(33, 'Can add product', 9, 'add_product'),
(34, 'Can change product', 9, 'change_product'),
(35, 'Can delete product', 9, 'delete_product'),
(36, 'Can view product', 9, 'view_product'),
(37, 'Can add static_page', 10, 'add_static_page'),
(38, 'Can change static_page', 10, 'change_static_page'),
(39, 'Can delete static_page', 10, 'delete_static_page'),
(40, 'Can view static_page', 10, 'view_static_page'),
(41, 'Can add user', 11, 'add_user'),
(42, 'Can change user', 11, 'change_user'),
(43, 'Can delete user', 11, 'delete_user'),
(44, 'Can view user', 11, 'view_user'),
(45, 'Can add banner', 12, 'add_banner'),
(46, 'Can change banner', 12, 'change_banner'),
(47, 'Can delete banner', 12, 'delete_banner'),
(48, 'Can view banner', 12, 'view_banner'),
(49, 'Can add sub_category', 13, 'add_sub_category'),
(50, 'Can change sub_category', 13, 'change_sub_category'),
(51, 'Can delete sub_category', 13, 'delete_sub_category'),
(52, 'Can view sub_category', 13, 'view_sub_category'),
(53, 'Can add child_Category', 14, 'add_child_category'),
(54, 'Can change child_Category', 14, 'change_child_category'),
(55, 'Can delete child_Category', 14, 'delete_child_category'),
(56, 'Can view child_Category', 14, 'view_child_category'),
(57, 'Can add category', 15, 'add_categories'),
(58, 'Can change category', 15, 'change_categories'),
(59, 'Can delete category', 15, 'delete_categories'),
(60, 'Can view category', 15, 'view_categories');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$180000$vupgNgZTHQXM$cg0RK/ij5nz+FDZTInlWNr4EQfjdWNqDj8MLnEJkuAY=', '2022-01-05 05:36:18.993220', 1, 'Admin', '', '', 'np022@gmail.com', 1, 1, '2021-12-23 10:51:55.634057');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-12-23 10:52:43.244506', '1', 'admin_user object (1)', 1, '[{\"added\": {}}]', 7, 1),
(2, '2021-12-23 12:07:08.204824', '1', 'fd', 1, '[{\"added\": {}}]', 8, 1),
(3, '2021-12-23 12:08:40.478676', '2', 'dfdf', 1, '[{\"added\": {}}]', 8, 1),
(4, '2021-12-23 12:49:20.863707', '3', 'slug', 1, '[{\"added\": {}}]', 8, 1),
(5, '2021-12-23 12:49:47.182196', '4', 'Nikhil Patil', 1, '[{\"added\": {}}]', 8, 1),
(6, '2021-12-23 12:53:11.563505', '5', 'navai ( nai kakri te kkai', 1, '[{\"added\": {}}]', 8, 1),
(7, '2021-12-23 13:00:39.639597', '5', 'Indoor Games', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 8, 1),
(8, '2021-12-23 13:00:49.265440', '2', 'Outdoor Games', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 8, 1),
(9, '2021-12-23 13:00:56.679347', '1', 'Air Sports', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 8, 1),
(10, '2021-12-23 13:01:08.721967', '4', 'water sport', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 8, 1),
(11, '2021-12-23 13:01:35.884174', '3', 'Pc & RPG games', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 8, 1),
(12, '2021-12-24 05:26:38.667482', '9', 'Air Sportsdd', 3, '', 8, 1),
(13, '2021-12-24 05:26:50.231026', '8', 'Air Sportss', 3, '', 8, 1),
(14, '2021-12-24 05:26:50.232455', '6', 'Cricket', 3, '', 8, 1),
(15, '2021-12-24 06:24:16.022353', '14', 'Outdoor Gamess', 3, '', 8, 1),
(16, '2021-12-24 06:24:16.024684', '13', 'Outdoor Gamess', 3, '', 8, 1),
(17, '2021-12-24 07:48:39.917141', '25', 'Hardik Patel', 1, '[{\"added\": {}}]', 8, 1),
(18, '2021-12-31 12:41:52.201389', '1', 'user object (1)', 1, '[{\"added\": {}}]', 11, 1),
(19, '2021-12-31 12:47:01.879968', '1', 'Nikhil Patila', 2, '[{\"changed\": {\"fields\": [\"Last name\"]}}]', 11, 1),
(20, '2021-12-31 12:47:47.119955', '1', 'Nikhil Patila', 2, '[{\"changed\": {\"fields\": [\"Username\"]}}]', 11, 1),
(21, '2021-12-31 12:48:28.397674', '2', 'sdsad sdfsd', 1, '[{\"added\": {}}]', 11, 1),
(22, '2021-12-31 12:49:29.673020', '3', 'Nikhil Patil', 1, '[{\"added\": {}}]', 11, 1),
(23, '2021-12-31 12:50:44.358791', '4', 'sdsad Patil', 1, '[{\"added\": {}}]', 11, 1),
(24, '2021-12-31 12:52:40.339677', '5', 'Nikhil Patil', 1, '[{\"added\": {}}]', 11, 1),
(25, '2021-12-31 12:55:42.630861', '6', 'Nikhil Patil', 1, '[{\"added\": {}}]', 11, 1),
(26, '2022-01-03 12:19:43.529849', '1', 'Image', 1, '[{\"added\": {}}]', 12, 1),
(27, '2022-01-03 12:19:54.117151', '1', 'Video', 2, '[{\"changed\": {\"fields\": [\"Short title\"]}}]', 12, 1),
(28, '2022-01-03 12:50:12.025623', '2', 'Image', 1, '[{\"added\": {}}]', 12, 1),
(29, '2022-01-03 13:00:01.663805', '2', 'Image', 2, '[{\"changed\": {\"fields\": [\"Extension\"]}}]', 12, 1),
(30, '2022-01-03 13:00:12.704958', '1', 'Video', 2, '[{\"changed\": {\"fields\": [\"Extension\"]}}]', 12, 1),
(31, '2022-01-05 05:36:39.515437', '52', 'Cat1', 1, '[{\"added\": {}}]', 8, 1),
(32, '2022-01-05 05:36:56.122493', '53', 'Sub1', 1, '[{\"added\": {}}]', 8, 1),
(33, '2022-01-05 05:54:07.812503', '1', 'category', 1, '[{\"added\": {}}]', 15, 1),
(34, '2022-01-05 05:54:31.122176', '2', 'Subcategory', 1, '[{\"added\": {}}]', 15, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'swooee', 'admin_user'),
(12, 'swooee', 'banner'),
(15, 'swooee', 'categories'),
(8, 'swooee', 'category'),
(14, 'swooee', 'child_category'),
(9, 'swooee', 'product'),
(10, 'swooee', 'static_page'),
(13, 'swooee', 'sub_category'),
(11, 'swooee', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-12-23 10:51:21.688786'),
(2, 'auth', '0001_initial', '2021-12-23 10:51:21.784991'),
(3, 'admin', '0001_initial', '2021-12-23 10:51:22.021241'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-12-23 10:51:22.082266'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-12-23 10:51:22.088379'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-12-23 10:51:22.132431'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-12-23 10:51:22.160077'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-12-23 10:51:22.173456'),
(9, 'auth', '0004_alter_user_username_opts', '2021-12-23 10:51:22.179439'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-12-23 10:51:22.211560'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-12-23 10:51:22.214113'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-12-23 10:51:22.220512'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-12-23 10:51:22.236458'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-12-23 10:51:22.248601'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-12-23 10:51:22.260559'),
(16, 'auth', '0011_update_proxy_permissions', '2021-12-23 10:51:22.266778'),
(17, 'sessions', '0001_initial', '2021-12-23 10:51:22.283921'),
(18, 'swooee', '0001_initial', '2021-12-23 10:51:22.350446'),
(19, 'swooee', '0002_auto_20211223_1817', '2021-12-23 12:47:35.320682'),
(20, 'swooee', '0003_auto_20211223_1834', '2021-12-23 13:04:49.583707'),
(21, 'swooee', '0004_product_category', '2021-12-23 13:06:15.296378'),
(22, 'swooee', '0005_auto_20211224_1313', '2021-12-24 07:43:37.316969'),
(23, 'swooee', '0006_auto_20211224_1320', '2021-12-24 07:50:40.630171'),
(24, 'swooee', '0007_auto_20211224_1323', '2021-12-24 07:53:17.842702'),
(25, 'swooee', '0008_auto_20211224_1326', '2021-12-24 07:56:43.250239'),
(26, 'swooee', '0009_auto_20211224_1438', '2021-12-24 09:08:04.552111'),
(27, 'swooee', '0010_auto_20211224_1454', '2021-12-24 09:24:52.934557'),
(28, 'swooee', '0011_auto_20211229_0956', '2021-12-29 04:27:39.372935'),
(29, 'swooee', '0012_auto_20211229_0957', '2021-12-29 04:27:39.383904'),
(30, 'swooee', '0013_auto_20211229_1018', '2021-12-29 04:48:05.642550'),
(31, 'swooee', '0002_auto_20211229_1020', '2021-12-29 04:50:59.235763'),
(32, 'swooee', '0003_auto_20211229_1024', '2021-12-29 04:54:46.747327'),
(33, 'swooee', '0002_user', '2021-12-31 12:40:47.010777'),
(34, 'swooee', '0003_auto_20211231_1824', '2021-12-31 12:54:52.102939'),
(35, 'swooee', '0004_auto_20211231_1825', '2021-12-31 12:55:32.693929'),
(36, 'swooee', '0005_user_checkbox', '2021-12-31 12:58:39.856978'),
(37, 'swooee', '0006_auto_20211231_1902', '2021-12-31 13:32:59.544641'),
(38, 'swooee', '0002_static_page_page', '2022-01-03 09:15:15.825606'),
(39, 'swooee', '0003_auto_20220103_1453', '2022-01-03 09:23:24.460854'),
(40, 'swooee', '0004_auto_20220103_1512', '2022-01-03 09:42:18.757095'),
(41, 'swooee', '0005_auto_20220103_1520', '2022-01-03 09:50:32.366064'),
(42, 'swooee', '0006_auto_20220103_1705', '2022-01-03 11:35:40.432586'),
(43, 'swooee', '0002_auto_20220103_1728', '2022-01-03 11:58:56.423006'),
(44, 'swooee', '0003_banner', '2022-01-03 12:18:18.605375'),
(45, 'swooee', '0004_banner_extension', '2022-01-03 12:59:35.755695'),
(46, 'swooee', '0002_delete_banner', '2022-01-03 13:54:45.201619'),
(47, 'swooee', '0002_banner', '2022-01-03 13:57:00.058013'),
(48, 'swooee', '0003_sub_category', '2022-01-04 11:58:10.368312'),
(49, 'swooee', '0004_child_category', '2022-01-04 12:00:57.755332'),
(50, 'swooee', '0005_auto_20220104_1733', '2022-01-04 12:04:00.738247'),
(51, 'swooee', '0006_auto_20220104_1841', '2022-01-04 13:12:04.008036'),
(52, 'swooee', '0003_category_parent', '2022-01-05 05:34:49.861826'),
(53, 'swooee', '0004_auto_20220105_1120', '2022-01-05 05:50:22.654323'),
(54, 'swooee', '0005_categories', '2022-01-05 05:52:08.120927'),
(55, 'swooee', '0006_auto_20220105_1143', '2022-01-05 06:13:30.870972'),
(56, 'swooee', '0007_auto_20220105_1145', '2022-01-05 06:15:44.503610'),
(57, 'swooee', '0008_auto_20220105_1151', '2022-01-05 06:21:10.857246'),
(58, 'swooee', '0002_auto_20220105_1236', '2022-01-05 07:07:06.789967'),
(59, 'swooee', '0003_auto_20220106_1149', '2022-01-06 06:19:10.804593'),
(60, 'swooee', '0004_auto_20220106_1217', '2022-01-06 06:47:33.182643'),
(61, 'swooee', '0002_auto_20220106_1325', '2022-01-06 07:55:07.773984'),
(62, 'swooee', '0003_auto_20220106_1325', '2022-01-06 07:55:19.087965'),
(63, 'swooee', '0004_auto_20220106_1332', '2022-01-06 08:02:13.516924');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('621ao9i0yjudnpi3yn691em1xgsdxhl0', 'YjkwZGFhNDJjYjYzNWExNzBkOTczY2IzMWQzYmJlOTI2MjA5NmM3Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhMzQ0NDhjYmU4ODYwNWNjMzU1NTE5OTQ0ZTQwNjc4NGQxNzM1Njc3IiwiaWQiOjF9', '2022-01-14 12:02:07.321768'),
('6p37mf318nc1vsdspmr6jx5rh9ooc38w', 'MTcwOWJlZjEzYjM5YWI3YmRlOWM5MzRmMTNlOGY4YmVmNjFlYTJhODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhMzQ0NDhjYmU4ODYwNWNjMzU1NTE5OTQ0ZTQwNjc4NGQxNzM1Njc3In0=', '2022-01-06 10:52:28.326122'),
('b2u8zcr5z15vuf1wzhedojmj5hw7k3ik', 'YjkwZGFhNDJjYjYzNWExNzBkOTczY2IzMWQzYmJlOTI2MjA5NmM3Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhMzQ0NDhjYmU4ODYwNWNjMzU1NTE5OTQ0ZTQwNjc4NGQxNzM1Njc3IiwiaWQiOjF9', '2022-01-19 09:56:00.916578'),
('cc20k3fpawiytzr9i3vw5nnl6iyyw7iw', 'NWMwNWE0NzIzODQ2Zjk1MGE0OGY0NzZjZjgwYzQwYTFiNzI3ZTgxODp7ImlkIjoxLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTM0NDQ4Y2JlODg2MDVjYzM1NTUxOTk0NGU0MDY3ODRkMTczNTY3NyJ9', '2022-01-19 05:36:18.996091'),
('omcy0tt1h5dy8zzz543f034mr2i5emsn', 'OTM2YjkxN2E5MjJjNDMxMzhiYjA4ZDY3NGMwZjZlYjc0ZjExMTljMjp7ImlkIjoxfQ==', '2022-01-19 13:42:42.463189'),
('xgegoi5uj0t40y30qzebud3cwvqxyekg', 'OTM2YjkxN2E5MjJjNDMxMzhiYjA4ZDY3NGMwZjZlYjc0ZjExMTljMjp7ImlkIjoxfQ==', '2022-01-19 12:10:26.909025'),
('yow9iiw2uaf7ab1mm8d5kps0y2cj0lss', 'OTM2YjkxN2E5MjJjNDMxMzhiYjA4ZDY3NGMwZjZlYjc0ZjExMTljMjp7ImlkIjoxfQ==', '2022-01-21 05:03:16.956533');

-- --------------------------------------------------------

--
-- Table structure for table `swooee_admin_user`
--

CREATE TABLE `swooee_admin_user` (
  `id` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `swooee_admin_user`
--

INSERT INTO `swooee_admin_user` (`id`, `username`, `password`) VALUES
(1, 'Admin', 'ABCD!123');

-- --------------------------------------------------------

--
-- Table structure for table `swooee_banner`
--

CREATE TABLE `swooee_banner` (
  `id` int(11) NOT NULL,
  `short_title` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `discription` longtext NOT NULL,
  `file` varchar(100) NOT NULL,
  `extension` varchar(255) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `status` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `swooee_banner`
--

INSERT INTO `swooee_banner` (`id`, `short_title`, `slug`, `discription`, `file`, `extension`, `created_at`, `updated_at`, `status`) VALUES
(1, 'Video', 'video', 'Swooee.com', 'Banners/Swoee-Revised-3-1_BUFhcfx.mp4', 'vid', '2022-01-04 10:29:28.201242', '2022-01-04 13:00:32.301336', '0'),
(3, 'Image', 'image', 'Images Upload For banner', 'Banners/81DEFTfCTL._UL1500__Jiq3xiX.jpg', 'img', '2022-01-04 11:27:29.693215', '2022-01-04 11:27:29.693215', '0');

-- --------------------------------------------------------

--
-- Table structure for table `swooee_categories`
--

CREATE TABLE `swooee_categories` (
  `id` int(11) NOT NULL,
  `category` varchar(50) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `Image` varchar(100) NOT NULL,
  `status` varchar(1) NOT NULL,
  `lft` int(10) UNSIGNED NOT NULL CHECK (`lft` >= 0),
  `rght` int(10) UNSIGNED NOT NULL CHECK (`rght` >= 0),
  `tree_id` int(10) UNSIGNED NOT NULL CHECK (`tree_id` >= 0),
  `level` int(10) UNSIGNED NOT NULL CHECK (`level` >= 0),
  `parent_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `swooee_product`
--

CREATE TABLE `swooee_product` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `discription` varchar(255) NOT NULL,
  `Image` varchar(100) NOT NULL,
  `amazon` varchar(200) NOT NULL,
  `amazon_sell_price` varchar(20) NOT NULL,
  `amazon_MRP` varchar(20) NOT NULL,
  `awin` varchar(200) NOT NULL,
  `awin_sell_price` varchar(20) NOT NULL,
  `awin_MRP` varchar(20) NOT NULL,
  `ebay` varchar(200) NOT NULL,
  `ebay_sell_price` varchar(20) NOT NULL,
  `ebay_MRP` varchar(20) NOT NULL,
  `walmart` varchar(200) NOT NULL,
  `walmart_sell_price` varchar(20) NOT NULL,
  `walmart_MRP` varchar(20) NOT NULL,
  `youtube` varchar(200) NOT NULL,
  `status` varchar(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `swooee_product`
--

INSERT INTO `swooee_product` (`id`, `name`, `slug`, `discription`, `Image`, `amazon`, `amazon_sell_price`, `amazon_MRP`, `awin`, `awin_sell_price`, `awin_MRP`, `ebay`, `ebay_sell_price`, `ebay_MRP`, `walmart`, `walmart_sell_price`, `walmart_MRP`, `youtube`, `status`, `created_at`, `updated_at`) VALUES
(13, 'product_min', 'product_min', 'product_min product_max product_aurl product_amin product_amax product_eurl product_emin product_emax product_wurl product_wmin product_wmax product_youtubeproduct_min product_max product_aurl product_amin product_amax product_eurl product_emin product_em', 'productimages/81DEFTfCTL._UL1500__A4tbJlr.jpg', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', '0', '2022-01-05 12:54:08.311730', '2022-01-05 12:54:08.311730');

-- --------------------------------------------------------

--
-- Table structure for table `swooee_static_page`
--

CREATE TABLE `swooee_static_page` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `discription` longtext NOT NULL,
  `Image` varchar(100) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `status` varchar(1) NOT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `page` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `swooee_static_page`
--

INSERT INTO `swooee_static_page` (`id`, `title`, `slug`, `discription`, `Image`, `created_at`, `status`, `updated_at`, `page`) VALUES
(20, 'About Us', 'about-us', '      About Swooee.com\r\n\r\nSome commands require additional packages\r\n\r\n*  South\r\n*  Haystack\r\n*  Django Command Extensions\r\n*  Shortcuts ', 'staticPages/81DEFTfCTL._UL1500__WRpz893.jpg', '2022-01-03 15:20:36.084761', '0', '2022-01-04 11:43:53.496848', '\n<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    \n\n<!-- Required meta tags -->\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">\n<title></title>\n<!-- plugins:css -->\n<link rel=\"stylesheet\" href=\"/static/assets/vendors/mdi/css/materialdesignicons.min.css\">\n<link rel=\"stylesheet\" href=\"/static/assets/vendors/css/vendor.bundle.base.css\">\n<script src=\"https://code.jquery.com/jquery-3.5.0.js\"></script>\n<!-- endinject -->\n<!-- Plugin css for this page -->\n<link rel=\"stylesheet\" href=\"/static/assets/vendors/jvectormap/jquery-jvectormap.css\">\n<link rel=\"stylesheet\" href=\"/static/assets/vendors/flag-icon-css/css/flag-icon.min.css\">\n<link rel=\"stylesheet\" href=\"/static/assets/vendors/owl-carousel-2/owl.carousel.min.css\">\n<link rel=\"stylesheet\" href=\"/static/assets/vendors/owl-carousel-2/owl.theme.default.min.css\">\n\n\n<!-- End plugin css for this page -->\n<!-- inject:css -->\n<!-- endinject -->\n\n<!-- Plugin css for this page -->\n<link rel=\"stylesheet\" href=\"/static/assets/vendors/select2/select2.min.css\">\n<link rel=\"stylesheet\" href=\"/static/assets/vendors/select2-bootstrap-theme/select2-bootstrap.min.css\">\n<!-- End plugin css for this page -->\n\n<!-- Layout styles -->\n<link rel=\"stylesheet\" href=\"/static/assets/css/style.css\">\n<!-- End layout styles -->\n<link rel=\"shortcut icon\" href=\"/static/assets/images/logo1.png\" />\n\n</head>\n<body>\n    <div class=\"container-fluid documentation\">\n      <div class=\"row\">\n        <div class=\"col-md-12 col-xl-12 main-panel\">\n          <div class=\"main-panel-wrapper\">\n              <div class=\"row\">\n                  <div class=\"col-12 mb-4\">\n                      <h2 class=\"mt-2 text-center font-weight-light text-uppercase\">About Us</h2>\n                  </div>\n                  <div class=\"col-12\">\n                      <div class=\"card col-12 mb-4\">\n                          <div class=\"card-body form-group\">\n                              <h3 class=\"mb-4\">About Us</h3>\n                              <textarea class=\'form-control main-panel file-upload-info\' disabled>      About Swooee.com\r\n\r\nSome commands require additional packages\r\n\r\n*  South\r\n*  Haystack\r\n*  Django Command Extensions\r\n*  Shortcuts </textarea>\n                          </div>\n                      </div>\n                  </div>\n              </div>  \n          </div>\n        </div>\n    </div>\n    \n    <script src=\"https://code.jquery.com/jquery-3.3.1.min.js\" integrity=\"sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=\" crossorigin=\"anonymous\"></script>\n    <script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js\" integrity=\"sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1\" crossorigin=\"anonymous\"></script>\n    <script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js\" integrity=\"sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM\" crossorigin=\"anonymous\"></script>\n    <script src=\"/static/assets/vendors/codemirror/codemirror.js\"></script>\n    <script src=\"https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.45.0/mode/ruby/ruby.min.js\"></script>\n    <script src=\"/static/assets/vendors/pwstabs/jquery.pwstabs.min.js\"></script>\n    <script src=\"script.js\"></script>\n</body>\n</html>');

-- --------------------------------------------------------

--
-- Table structure for table `swooee_user`
--

CREATE TABLE `swooee_user` (
  `id` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `email` varchar(254) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `password` varchar(30) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `Image` varchar(100) NOT NULL,
  `status` varchar(1) NOT NULL,
  `checkbox` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `swooee_user`
--

INSERT INTO `swooee_user` (`id`, `username`, `email`, `first_name`, `last_name`, `slug`, `password`, `created_at`, `updated_at`, `Image`, `status`, `checkbox`) VALUES
(62, 'Admin', 'akash13@mailinator.com', 'Abc123', 'fhag123', 'abc123-fhag123', '', '2022-01-03 12:41:14.586939', '2022-01-06 11:31:35.736414', 'userimages/pic-1.png', '0', '0'),
(72, 'Nilam', 'nilam@mailinator.com', 'Nilam', 'Soni', 'nilam-soni', '', '2022-01-03 12:54:44.189182', '2022-01-06 11:36:42.502885', 'userimages/pic-2.png', '0', '0'),
(73, 'Admin11', 'nikhil@mailinator.com', 'Nikhil', 'fhag', 'nikhil-fhag', 'Nikhil', '2022-01-03 12:57:33.869865', '2022-01-05 13:33:52.143138', 'userimages/pic-1_gI8nb7X.png', '0', '0'),
(74, 'Admin1223', 'akky9988@mailinator.com', 'Akash', 'Suthar', 'akash-suthar', '!234567', '2022-01-03 12:57:33.869865', '2022-01-05 13:33:52.143138', 'userimages/pic-4.png', '0', '0'),
(75, 'npo111', 'nik@mailinator.com', 'NIlesh', '', 'nilesh', '', '2022-01-05 19:12:21.295753', '2022-01-06 11:37:07.701737', 'userimages/colour_scheme_example.jpg', '0', '0');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `swooee_admin_user`
--
ALTER TABLE `swooee_admin_user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `swooee_banner`
--
ALTER TABLE `swooee_banner`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `swooee_categories`
--
ALTER TABLE `swooee_categories`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `swooee_product`
--
ALTER TABLE `swooee_product`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `swooee_product_slug_c9fc0ac7_uniq` (`slug`);

--
-- Indexes for table `swooee_static_page`
--
ALTER TABLE `swooee_static_page`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `swooee_user`
--
ALTER TABLE `swooee_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT for table `swooee_admin_user`
--
ALTER TABLE `swooee_admin_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `swooee_banner`
--
ALTER TABLE `swooee_banner`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `swooee_categories`
--
ALTER TABLE `swooee_categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `swooee_product`
--
ALTER TABLE `swooee_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `swooee_static_page`
--
ALTER TABLE `swooee_static_page`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `swooee_user`
--
ALTER TABLE `swooee_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
