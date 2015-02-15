/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50622
Source Host           : localhost:3306
Source Database       : testapp

Target Server Type    : MYSQL
Target Server Version : 50622
File Encoding         : 65001

Date: 2015-02-06 20:28:51
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `testapp_yplayer`
-- ----------------------------
DROP TABLE IF EXISTS `testapp_yplayer`;
CREATE TABLE `testapp_yplayer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `id_name` varchar(100) NOT NULL,
  `width` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  `video_id` varchar(100),
  `frameborder` int(11) NOT NULL,
  `count` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of testapp_yplayer
-- ----------------------------
INSERT INTO `testapp_yplayer` VALUES ('1', 'video1', 'player1', '640', '390', 'o33GEoHyM7I', '0', '0');
INSERT INTO `testapp_yplayer` VALUES ('2', 'video2', 'player2', '640', '390', '3V_zgT93EgA', '0', '0');
INSERT INTO `testapp_yplayer` VALUES ('3', 'video3', 'player3', '640', '390', '0Niin-szO60', '0', '0');
INSERT INTO `testapp_yplayer` VALUES ('4', 'video4', 'player4', '640', '390', 'dUbH6apUHDU', '0', '0');
