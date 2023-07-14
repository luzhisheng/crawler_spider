-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: eb_supports_xxxxx
-- ------------------------------------------------------
-- Server version	5.7.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clean_xxxxx_dy_author_detail`
--

DROP TABLE IF EXISTS `clean_xxxxx_dy_author_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clean_xxxxx_dy_author_detail` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `updateTime` varchar(50) DEFAULT '' COMMENT '时间',
  `Name` varchar(100) DEFAULT '' COMMENT '抖音号名称',
  `HeaderImg` varchar(255) DEFAULT '' COMMENT '头像',
  `DouYinId` varchar(50) DEFAULT '' COMMENT '抖音id',
  `SubDetail` varchar(255) DEFAULT '' COMMENT '简介',
  `FansCnt` int(12) DEFAULT '0' COMMENT '粉丝',
  `FavCnt` int(12) DEFAULT '0' COMMENT '点赞',
  `Sex` smallint(1) DEFAULT '0' COMMENT '性别',
  `IsShow` smallint(1) DEFAULT '0',
  `Reputation` smallint(1) DEFAULT '0' COMMENT '带货口碑',
  `City` varchar(50) DEFAULT '' COMMENT '城市',
  `CustomVerify` varchar(100) DEFAULT '' COMMENT '个人认证',
  `McnName` varchar(100) DEFAULT '' COMMENT 'MCN机构',
  `EnterpriseVerify` varchar(100) DEFAULT '' COMMENT '企业认证',
  `WorksType` varchar(100) DEFAULT '' COMMENT '达人类型',
  `MainSaleType` varchar(50) DEFAULT '' COMMENT '带货信息',
  `SaleType` varchar(50) DEFAULT '' COMMENT '带货信息',
  `UserId` varchar(50) DEFAULT '' COMMENT '抖音uid',
  `McnId` varchar(50) DEFAULT '',
  `SecUserId` varchar(100) DEFAULT '' COMMENT '抖音sec_uid',
  `HasGoodWindow` smallint(1) DEFAULT '0',
  `HasLiveHistory` smallint(1) DEFAULT '0',
  `ShopId` varchar(50) DEFAULT '' COMMENT '店铺id',
  `ShopName` varchar(100) DEFAULT '' COMMENT '店铺名称',
  `ProductType` varchar(100) DEFAULT '' COMMENT '主营类型',
  `isFav` smallint(1) DEFAULT '0',
  `RoomId` varchar(50) DEFAULT '' COMMENT '直播间id',
  `UserLevel` smallint(1) DEFAULT '0' COMMENT '达人带货等级',
  `roomGoodsFlag` smallint(1) DEFAULT '0',
  `awemeGoodsFlag` smallint(1) DEFAULT '0',
  `fansMilestone` text COMMENT '粉丝里程碑',
  `deduplication` varchar(100) DEFAULT '' COMMENT '去重字段',
  `spider_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '爬虫抓取时间',
  UNIQUE KEY `task_id` (`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clean_xxxxx_dy_author_room_info`
--

DROP TABLE IF EXISTS `clean_xxxxx_dy_author_room_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clean_xxxxx_dy_author_room_info` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `authorId` varchar(100) DEFAULT NULL COMMENT '抖音id',
  `BeginTime` varchar(50) DEFAULT '' COMMENT '开播时间',
  `CreativeFlag` varchar(100) DEFAULT '',
  `EndTime` varchar(50) DEFAULT '' COMMENT '开播结束时间',
  `Gmv` int(12) DEFAULT '0' COMMENT '销售额',
  `GoodsCnt` int(12) DEFAULT '0' COMMENT '商品数',
  `LiveName` varchar(50) DEFAULT '' COMMENT '直播间名称',
  `LiveTime` varchar(50) DEFAULT '' COMMENT '直播时长',
  `PenRate` varchar(50) DEFAULT '' COMMENT '穿透率=直播观看人数/直播曝光人数',
  `RoomId` varchar(50) DEFAULT '' COMMENT '直播间id',
  `RoomPic` varchar(100) DEFAULT '' COMMENT '头像',
  `SaleCnt` int(12) DEFAULT '0' COMMENT '销量',
  `TotalUser` int(12) DEFAULT '0' COMMENT '观看人次',
  `TraffiOriginList` text COMMENT '观众来源',
  `UserCount` int(12) DEFAULT '0' COMMENT '人气峰值',
  `UvValue` varchar(50) DEFAULT '' COMMENT 'uv价值',
  `deduplication` varchar(100) DEFAULT '' COMMENT '去重字段',
  `spider_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '爬虫抓取时间',
  UNIQUE KEY `task_id` (`deduplication`) USING BTREE,
  KEY `authorId` (`authorId`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clean_xxxxx_dy_author_search_list`
--

DROP TABLE IF EXISTS `clean_xxxxx_dy_author_search_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clean_xxxxx_dy_author_search_list` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `AwemeCnt` int(12) DEFAULT '0',
  `AwemeGmv` int(12) DEFAULT '0',
  `AwemeGoodsCnt` int(12) DEFAULT '0',
  `CustomVerify` varchar(50) DEFAULT '',
  `DouYinId` varchar(50) DEFAULT '' COMMENT '抖音id',
  `EnterpriseVerify` varchar(50) DEFAULT '',
  `FansAddCnt` int(12) DEFAULT '0',
  `FansCnt` int(12) DEFAULT '0' COMMENT '粉丝',
  `FavAddCnt` int(12) DEFAULT '0',
  `FavCnt` varchar(100) DEFAULT '' COMMENT '点赞',
  `Gmv` varchar(50) DEFAULT '0' COMMENT '销量',
  `GroupId` int(12) DEFAULT '0',
  `HasGoodWindow` smallint(6) DEFAULT '0',
  `HasLiveHistory` smallint(6) DEFAULT '0',
  `HeaderImg` varchar(150) DEFAULT '' COMMENT '头像',
  `IsAddFav` smallint(6) DEFAULT '0',
  `IsLiving` varchar(50) DEFAULT '',
  `LatestData` varchar(255) DEFAULT '',
  `Name` varchar(50) DEFAULT '' COMMENT '昵称',
  `PerAwemeFavCnt` int(12) DEFAULT '0',
  `PerCnt` int(12) DEFAULT '0',
  `PerFavFen` varchar(50) DEFAULT '',
  `PerGmv` varchar(50) DEFAULT '',
  `PerGoodsCnt` int(12) DEFAULT '0' COMMENT '商品数',
  `PerSale` varchar(50) DEFAULT '',
  `PerUserCnt` int(12) DEFAULT '0',
  `RemarkName` varchar(50) DEFAULT '',
  `Reputation` int(12) DEFAULT '0',
  `RoomCnt` int(12) DEFAULT '0',
  `Sale` int(12) DEFAULT '0',
  `SaleCnt` int(12) DEFAULT '0',
  `SaleGoodsType` varchar(50) DEFAULT '',
  `ShopId` varchar(50) DEFAULT '',
  `ShopName` varchar(50) DEFAULT '',
  `TotalGmv` varchar(50) DEFAULT '',
  `UV` varchar(50) DEFAULT '',
  `UserId` varchar(50) DEFAULT '' COMMENT 'UserId',
  `UserLevel` smallint(6) DEFAULT '0' COMMENT '等级',
  `WorksType` varchar(50) DEFAULT '' COMMENT 'uv价值',
  `deduplication` varchar(100) DEFAULT '' COMMENT '去重字段',
  `spider_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '爬虫抓取时间',
  UNIQUE KEY `deduplication` (`deduplication`) USING BTREE,
  KEY `UserId` (`UserId`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clean_xxxxx_dy_live_room_detail`
--

DROP TABLE IF EXISTS `clean_xxxxx_dy_live_room_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clean_xxxxx_dy_live_room_detail` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `RoomId` varchar(100) DEFAULT NULL,
  `people_FansCnt` int(10) DEFAULT '0' COMMENT '粉丝',
  `people_HeaderImg` varchar(150) DEFAULT '0' COMMENT '头像',
  `people_Name` varchar(255) DEFAULT '0' COMMENT '昵称',
  `people_SecUserId` varchar(100) DEFAULT '' COMMENT '抖音sec_uid',
  `people_UserId` varchar(50) DEFAULT '' COMMENT '抖音uid',
  `room_AvgUserCount` int(12) DEFAULT '0' COMMENT '平均在线',
  `room_BeginTime` varchar(50) DEFAULT '' COMMENT '开播时间',
  `room_EndTime` varchar(50) DEFAULT '' COMMENT '下播时间',
  `room_Gmv` int(12) DEFAULT '0' COMMENT '销售额',
  `room_GoodsCnt` int(12) DEFAULT '0' COMMENT '商品数',
  `room_LiveExposedNum` smallint(6) DEFAULT '0',
  `room_LiveTransNum` smallint(6) DEFAULT '0',
  `room_LiveViewer` smallint(6) DEFAULT '0',
  `room_MaxUserCnt` int(12) DEFAULT '0' COMMENT '人气峰值',
  `room_RoomId` varchar(100) DEFAULT '' COMMENT '直播id',
  `room_SaleCnt` int(12) DEFAULT '0' COMMENT '总销量',
  `room_TotalUser` int(12) DEFAULT '0' COMMENT '观看人次',
  `room_UserCount` int(12) DEFAULT '0',
  `room_viewer_info_other` int(12) DEFAULT '0' COMMENT '其他',
  `room_viewer_info_video` int(12) DEFAULT '0' COMMENT '短视频引流',
  `room_viewer_info_follow` int(12) DEFAULT '0' COMMENT '关注',
  `room_viewer_info_feed` int(12) DEFAULT '0' COMMENT '推荐feed',
  `room_viewer_info_city` int(12) DEFAULT '0' COMMENT '直播推荐/同城',
  `room_viewer_info_plaza` int(12) DEFAULT '0' COMMENT '直播广场',
  `room_viewer_info_search` int(12) DEFAULT '0' COMMENT '搜索',
  `room_viewer_info_home` int(12) DEFAULT '0' COMMENT '个人主页',
  `room_WebRoomId` varchar(50) DEFAULT '',
  `deduplication` varchar(100) DEFAULT '' COMMENT '去重字段',
  `spider_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '爬虫抓取时间',
  UNIQUE KEY `task_id` (`deduplication`) USING BTREE,
  KEY `roomid` (`RoomId`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clean_xxxxx_dy_live_room_flow_info`
--

DROP TABLE IF EXISTS `clean_xxxxx_dy_live_room_flow_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clean_xxxxx_dy_live_room_flow_info` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `RoomId` varchar(100) DEFAULT NULL,
  `FavCnt` int(12) DEFAULT '0' COMMENT '粉丝',
  `FollowCnt` int(8) DEFAULT '0' COMMENT '关注',
  `FullTime` varchar(50) DEFAULT '' COMMENT '时间',
  `Gmv` int(12) DEFAULT '0' COMMENT '销售额',
  `OnExplainGoods` varchar(255) DEFAULT '' COMMENT '关于商品说明',
  `OnSellGoods` varchar(255) DEFAULT '' COMMENT '售卖商品',
  `SaleCnt` int(12) DEFAULT '0' COMMENT '销售数量',
  `TotalUserCnt` int(12) DEFAULT '0' COMMENT '总用户数',
  `UserCnt` int(12) DEFAULT '0' COMMENT '当前用户数',
  `deduplication` varchar(100) DEFAULT '' COMMENT '去重字段',
  `spider_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '爬虫抓取时间',
  UNIQUE KEY `task_id` (`deduplication`) USING BTREE,
  KEY `roomid` (`RoomId`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clean_xxxxx_dy_live_room_goods`
--

DROP TABLE IF EXISTS `clean_xxxxx_dy_live_room_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clean_xxxxx_dy_live_room_goods` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `RoomId` varchar(100) DEFAULT NULL,
  `Gmv` varchar(50) DEFAULT '' COMMENT '销售额',
  `GmvValue` decimal(20,2) DEFAULT '0.00' COMMENT '销售额',
  `GoodName` varchar(50) DEFAULT '' COMMENT '商品名字',
  `GoodPic` varchar(255) DEFAULT '' COMMENT '商品图片',
  `GoodsId` varchar(50) DEFAULT '' COMMENT '商品id',
  `SaleCnt` int(12) DEFAULT '0' COMMENT ' 销量',
  `SaleCntValue` varchar(50) DEFAULT '' COMMENT ' 销量',
  `SellPrice` decimal(20,2) DEFAULT '0.00' COMMENT '直播价格',
  `StartTime` datetime DEFAULT NULL COMMENT '上架时间',
  `deduplication` varchar(100) DEFAULT '' COMMENT '去重字段',
  `spider_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '爬虫抓取时间',
  UNIQUE KEY `task_id` (`deduplication`) USING BTREE,
  KEY `RoomId` (`RoomId`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clean_xxxxx_dy_live_search_list`
--

DROP TABLE IF EXISTS `clean_xxxxx_dy_live_search_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clean_xxxxx_dy_live_search_list` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `BeginTime` varchar(50) DEFAULT '' COMMENT '开播时间',
  `Gmv` varchar(50) DEFAULT '' COMMENT '销售额',
  `GoodsCnt` int(12) DEFAULT '0' COMMENT '商品数',
  `IsLiving` varchar(50) DEFAULT '' COMMENT '直播间id',
  `LiveName` varchar(100) DEFAULT '' COMMENT '直播间名字',
  `LiveTime` varchar(50) DEFAULT '' COMMENT '直播间时长',
  `RoomId` varchar(50) DEFAULT '' COMMENT ' 直播间id',
  `RoomPic` varchar(50) DEFAULT '' COMMENT ' 直播间图片',
  `SaleCnt` int(12) DEFAULT '0' COMMENT '销量',
  `TotalUser` int(12) DEFAULT '0' COMMENT '观看人次',
  `UserCount` int(12) DEFAULT '0' COMMENT '人气峰值',
  `blogger_FansCnt` int(12) DEFAULT '0' COMMENT '达人粉丝',
  `blogger_HeaderImg` varchar(100) DEFAULT '' COMMENT '达人图像',
  `blogger_Name` varchar(50) DEFAULT '' COMMENT '达人名称',
  `blogger_UserId` varchar(50) DEFAULT '' COMMENT '达人id',
  `deduplication` varchar(100) DEFAULT '' COMMENT '去重字段',
  `spider_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '爬虫抓取时间',
  UNIQUE KEY `task_id` (`task_id`,`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `xxxxx_dy_author_detail`
--

DROP TABLE IF EXISTS `xxxxx_dy_author_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `xxxxx_dy_author_detail` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `data` mediumtext COMMENT '数据结果',
  `deduplication` varchar(50) DEFAULT '' COMMENT '去重字段',
  `status` smallint(6) DEFAULT '0' COMMENT '状态',
  `status_extrator` smallint(6) DEFAULT '0' COMMENT '清洗状态',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `task_id` (`task_id`,`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `xxxxx_dy_author_monitor`
--

DROP TABLE IF EXISTS `xxxxx_dy_author_monitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `xxxxx_dy_author_monitor` (
  `task_id` varchar(100) DEFAULT '' COMMENT '项目id',
  `authorId` varchar(100) DEFAULT '' COMMENT '用户id',
  `LiveName` varchar(100) DEFAULT '' COMMENT '直播间名称',
  `BeginTime` datetime DEFAULT NULL COMMENT '开播时间',
  `EndTime` datetime DEFAULT NULL COMMENT '开播结束时间',
  `status` smallint(6) DEFAULT '0' COMMENT '状态',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `authorId` (`authorId`,`BeginTime`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `xxxxx_dy_author_room_info`
--

DROP TABLE IF EXISTS `xxxxx_dy_author_room_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `xxxxx_dy_author_room_info` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `data` mediumtext COMMENT '数据结果',
  `deduplication` varchar(50) DEFAULT '' COMMENT '去重字段',
  `status` smallint(6) DEFAULT '0' COMMENT '状态',
  `status_extrator` smallint(6) DEFAULT '0' COMMENT '清洗状态',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `task_id` (`task_id`,`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `xxxxx_dy_author_search_list`
--

DROP TABLE IF EXISTS `xxxxx_dy_author_search_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `xxxxx_dy_author_search_list` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `data` mediumtext COMMENT '数据结果',
  `deduplication` varchar(100) DEFAULT '' COMMENT '去重字段',
  `status` smallint(6) DEFAULT '0' COMMENT '状态',
  `status_extrator` smallint(6) DEFAULT '0' COMMENT '清洗状态',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `task_id` (`task_id`,`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `xxxxx_dy_live_room_detail`
--

DROP TABLE IF EXISTS `xxxxx_dy_live_room_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `xxxxx_dy_live_room_detail` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `data` mediumtext COMMENT '数据结果',
  `deduplication` varchar(50) DEFAULT '' COMMENT '去重字段',
  `status` smallint(6) DEFAULT '0' COMMENT '状态',
  `status_extrator` smallint(6) DEFAULT '0' COMMENT '清洗状态',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `task_id` (`task_id`,`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `xxxxx_dy_live_room_flow_info`
--

DROP TABLE IF EXISTS `xxxxx_dy_live_room_flow_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `xxxxx_dy_live_room_flow_info` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `data` mediumtext COMMENT '数据结果',
  `deduplication` varchar(100) DEFAULT '' COMMENT '去重字段',
  `status` smallint(6) DEFAULT '0' COMMENT '状态',
  `status_extrator` smallint(6) DEFAULT '0' COMMENT '清洗状态',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `task_id` (`task_id`,`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `xxxxx_dy_live_room_goods`
--

DROP TABLE IF EXISTS `xxxxx_dy_live_room_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `xxxxx_dy_live_room_goods` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `data` mediumtext COMMENT '数据结果',
  `deduplication` varchar(100) DEFAULT '' COMMENT '去重字段',
  `status` smallint(6) DEFAULT '0' COMMENT '状态',
  `status_extrator` smallint(6) DEFAULT '0' COMMENT '清洗状态',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `task_id` (`task_id`,`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `xxxxx_dy_live_search_list`
--

DROP TABLE IF EXISTS `xxxxx_dy_live_search_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `xxxxx_dy_live_search_list` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `data` mediumtext COMMENT '数据结果',
  `deduplication` varchar(100) DEFAULT '' COMMENT '去重字段',
  `status` smallint(6) DEFAULT '0' COMMENT '状态',
  `status_extrator` smallint(6) DEFAULT '0' COMMENT '清洗状态',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `task_id` (`task_id`,`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `xxxxx_dy_sign`
--

DROP TABLE IF EXISTS `xxxxx_dy_sign`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `xxxxx_dy_sign` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `data` mediumtext COMMENT '数据结果',
  `status` smallint(6) DEFAULT '0' COMMENT '状态',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `task_id` (`task_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `project_xxxxx_dy_author_detail`
--

DROP TABLE IF EXISTS `project_xxxxx_dy_author_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_xxxxx_dy_author_detail` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `payload_get` text COMMENT 'get请求参数',
  `payload_post` varchar(255) DEFAULT '' COMMENT 'post请求参数',
  `deduplication` varchar(50) DEFAULT '' COMMENT '去重字段',
  `weight` tinyint(1) DEFAULT '0' COMMENT '权重',
  `status` tinyint(1) DEFAULT '0',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `task_id` (`task_id`,`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `project_xxxxx_dy_author_monitor`
--

DROP TABLE IF EXISTS `project_xxxxx_dy_author_monitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_xxxxx_dy_author_monitor` (
  `task_id` varchar(100) DEFAULT '' COMMENT '项目id',
  `authorId` varchar(100) DEFAULT '' COMMENT '用户id',
  `BeginTime` datetime DEFAULT NULL COMMENT '开播时间',
  `EndTime` datetime DEFAULT NULL COMMENT '开播结束时间',
  `count` int(11) DEFAULT '0' COMMENT '计数',
  `weight` tinyint(1) DEFAULT '0' COMMENT '权重',
  `status` smallint(6) DEFAULT '0' COMMENT '状态',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `authorId` (`authorId`,`task_id`,`BeginTime`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `project_xxxxx_dy_author_room_info`
--

DROP TABLE IF EXISTS `project_xxxxx_dy_author_room_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_xxxxx_dy_author_room_info` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `payload_get` varchar(255) DEFAULT '' COMMENT 'get请求参数',
  `payload_post` varchar(255) DEFAULT '' COMMENT 'post请求参数',
  `deduplication` varchar(50) DEFAULT '' COMMENT '去重字段',
  `weight` tinyint(1) DEFAULT '0' COMMENT '权重',
  `status` tinyint(1) DEFAULT '0',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `task_id` (`task_id`,`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `project_xxxxx_dy_author_search_list`
--

DROP TABLE IF EXISTS `project_xxxxx_dy_author_search_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_xxxxx_dy_author_search_list` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `payload_get` text COMMENT 'get请求参数',
  `payload_post` varchar(255) DEFAULT '' COMMENT 'post请求参数',
  `deduplication` varchar(50) DEFAULT '' COMMENT '去重字段',
  `weight` tinyint(4) DEFAULT NULL COMMENT '权重',
  `status` tinyint(1) DEFAULT '0',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `task_id` (`task_id`,`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `project_xxxxx_dy_live_room_detail`
--

DROP TABLE IF EXISTS `project_xxxxx_dy_live_room_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_xxxxx_dy_live_room_detail` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `payload_get` text COMMENT 'get请求参数',
  `payload_post` varchar(255) DEFAULT '' COMMENT 'post请求参数',
  `deduplication` varchar(50) DEFAULT '' COMMENT '去重字段',
  `weight` tinyint(1) DEFAULT '0' COMMENT '权重',
  `status` tinyint(1) DEFAULT '0',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `task_id` (`task_id`,`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `project_xxxxx_dy_live_room_flow_info`
--

DROP TABLE IF EXISTS `project_xxxxx_dy_live_room_flow_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_xxxxx_dy_live_room_flow_info` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `payload_get` text COMMENT 'get请求参数',
  `payload_post` varchar(255) DEFAULT '' COMMENT 'post请求参数',
  `deduplication` varchar(100) DEFAULT '' COMMENT '去重字段',
  `weight` tinyint(1) DEFAULT '0' COMMENT '权重',
  `status` tinyint(1) DEFAULT '0',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `task_id` (`task_id`,`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `project_xxxxx_dy_live_room_goods`
--

DROP TABLE IF EXISTS `project_xxxxx_dy_live_room_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_xxxxx_dy_live_room_goods` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `payload_get` text COMMENT 'get请求参数',
  `payload_post` varchar(255) DEFAULT '' COMMENT 'post请求参数',
  `deduplication` varchar(50) DEFAULT '' COMMENT '去重字段',
  `weight` tinyint(1) DEFAULT '0' COMMENT '权重',
  `status` tinyint(1) DEFAULT '0',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `task_id` (`task_id`,`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `project_xxxxx_dy_live_search_list`
--

DROP TABLE IF EXISTS `project_xxxxx_dy_live_search_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_xxxxx_dy_live_search_list` (
  `task_id` varchar(100) DEFAULT NULL COMMENT '项目id',
  `payload_get` text COMMENT 'get请求参数',
  `payload_post` varchar(255) DEFAULT '' COMMENT 'post请求参数',
  `deduplication` varchar(50) DEFAULT '' COMMENT '去重字段',
  `weight` tinyint(4) DEFAULT NULL COMMENT '权重',
  `status` tinyint(1) DEFAULT '0',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `task_id` (`task_id`,`deduplication`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-14 12:19:08
