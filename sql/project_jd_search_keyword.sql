/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 80031
Source Host           : 127.0.0.1:3306
Source Database       : eb_supports_jd

Target Server Type    : MYSQL
Target Server Version : 80031
File Encoding         : 65001

Date: 2022-12-05 01:05:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for project_jd_search_keyword
-- ----------------------------
DROP TABLE IF EXISTS `project_jd_search_keyword`;
CREATE TABLE `project_jd_search_keyword` (
  `id` int NOT NULL AUTO_INCREMENT,
  `project_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '项目id',
  `keyword` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '作者id',
  `score` tinyint(1) DEFAULT '1',
  `status` tinyint(1) DEFAULT '0',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `project_id` (`project_id`,`keyword`,`score`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;
