SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for jd_comment_product_page_comments_action
-- ----------------------------
DROP TABLE IF EXISTS `jd_comment_product_page_comments_action`;
CREATE TABLE `jd_comment_product_page_comments_action`  (
`project_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '作者id',
`keyword` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '搜索词',
`product_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '商品id',
`page` int NULL DEFAULT NULL COMMENT '翻页',
`data` mediumtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '数据结果',
`extractor_comments_status` int NULL DEFAULT 0 COMMENT '状态',
`extractor_comments_cut_status` int NULL DEFAULT 0 COMMENT '状态',
`create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
`update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
UNIQUE INDEX `project_id`(`project_id` ASC, `keyword` ASC, `product_id` ASC, `page` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

SET FOREIGN_KEY_CHECKS = 1;
