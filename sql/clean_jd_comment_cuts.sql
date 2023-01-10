SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for clean_jd_comment_cuts
-- ----------------------------
DROP TABLE IF EXISTS `clean_jd_comment_cuts`;
CREATE TABLE `clean_jd_comment_cuts`  (
  `project_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '作者id',
  `comments_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '评论id',
  `cut` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '评论内容',
  UNIQUE INDEX `project_id`(`project_id` ASC, `comments_id` ASC, `cut` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

SET FOREIGN_KEY_CHECKS = 1;
