/*
 Navicat Premium Data Transfer

 Source Server         : google cloud
 Source Server Type    : MySQL
 Source Server Version : 80031 (8.0.31-google)
 Source Host           : 35.246.24.203:3306
 Source Schema         : progSDTeamProject

 Target Server Type    : MySQL
 Target Server Version : 80031 (8.0.31-google)
 File Encoding         : 65001

 Date: 02/11/2023 10:30:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Customers
-- ----------------------------
DROP TABLE IF EXISTS `Customers`;
CREATE TABLE `Customers` (
  `customerID` int NOT NULL COMMENT 'ID',
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '姓名',
  `password` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '密码',
  `email` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '邮箱',
  `accountBalance` float(128,2) DEFAULT NULL COMMENT '余额',
  PRIMARY KEY (`email`,`customerID`) USING BTREE,
  UNIQUE KEY `email` (`email`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of Customers
-- ----------------------------
BEGIN;
INSERT INTO `Customers` (`customerID`, `name`, `password`, `email`, `accountBalance`) VALUES (8, 'test', '123456', '123456@com', 5.50);
INSERT INTO `Customers` (`customerID`, `name`, `password`, `email`, `accountBalance`) VALUES (10, 'test_11', '123456789', '2864387Z@student.gla.ac.uk', 5.50);
INSERT INTO `Customers` (`customerID`, `name`, `password`, `email`, `accountBalance`) VALUES (7, 'Yujia Zhang', '123456', '2864389Z@student.gla.ac.uk', 4.90);
INSERT INTO `Customers` (`customerID`, `name`, `password`, `email`, `accountBalance`) VALUES (9, 'test_11', '321321', '2864389ZZ@student.gla.ac.uk', 5.14);
INSERT INTO `Customers` (`customerID`, `name`, `password`, `email`, `accountBalance`) VALUES (5, 'Yuqing Ren', '9988', 'renyuqing@gmail.com', 105.01);
INSERT INTO `Customers` (`customerID`, `name`, `password`, `email`, `accountBalance`) VALUES (1, 'Zhang,Ruixian', '3022008a', 'zhangruixian@gmail.com', 590.14);
INSERT INTO `Customers` (`customerID`, `name`, `password`, `email`, `accountBalance`) VALUES (2, 'Yujia Ye', 'adsd2132', 'zhangyujia@gmail.com', 152.19);
INSERT INTO `Customers` (`customerID`, `name`, `password`, `email`, `accountBalance`) VALUES (3, 'Junan Zheng', 'oi2313', 'zhengjunan@yahool.com', 4.39);
INSERT INTO `Customers` (`customerID`, `name`, `password`, `email`, `accountBalance`) VALUES (4, 'Junan Zheng', 'oi2313', 'zhengjunnan99@gmail.com', 5.50);
INSERT INTO `Customers` (`customerID`, `name`, `password`, `email`, `accountBalance`) VALUES (6, 'Zhihan Zhou', '123', 'zzh282604691@163.com', 5.50);
COMMIT;

-- ----------------------------
-- Table structure for Managers
-- ----------------------------
DROP TABLE IF EXISTS `Managers`;
CREATE TABLE `Managers` (
  `managerID` int NOT NULL COMMENT 'ID',
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '姓名',
  `password` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '密码',
  `email` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '邮箱',
  PRIMARY KEY (`email`,`managerID`) USING BTREE,
  UNIQUE KEY `email` (`email`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of Managers
-- ----------------------------
BEGIN;
INSERT INTO `Managers` (`managerID`, `name`, `password`, `email`) VALUES (3, 'Yujia Zhang', '123', '123456@com');
INSERT INTO `Managers` (`managerID`, `name`, `password`, `email`) VALUES (2, 'Yujia Zhang', '123456', '2864389Z@student.gla.ac.uk');
INSERT INTO `Managers` (`managerID`, `name`, `password`, `email`) VALUES (1, 'Manager', 'manager123', 'manager123@gmail.com');
COMMIT;

-- ----------------------------
-- Table structure for Managers_ver
-- ----------------------------
DROP TABLE IF EXISTS `Managers_ver`;
CREATE TABLE `Managers_ver` (
  `managerID` int NOT NULL AUTO_INCREMENT COMMENT '维修人员ID',
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '姓名',
  `password` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '密码',
  `email` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '邮箱',
  `code_ver` varchar(255) NOT NULL COMMENT '验证码',
  PRIMARY KEY (`managerID`) USING BTREE,
  UNIQUE KEY `email` (`email`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of Managers_ver
-- ----------------------------
BEGIN;
INSERT INTO `Managers_ver` (`managerID`, `name`, `password`, `email`, `code_ver`) VALUES (1, 'RRR', '3022008a', 'zhangruixian98@gmail.com', '3742');
INSERT INTO `Managers_ver` (`managerID`, `name`, `password`, `email`, `code_ver`) VALUES (2, 'Yujia Zhang', '123456', '2864389Z@student.gla.ac.uk', '8330');
INSERT INTO `Managers_ver` (`managerID`, `name`, `password`, `email`, `code_ver`) VALUES (3, 'yujia', '123456', 'zyj_8209500@163.com', '5045');
COMMIT;

-- ----------------------------
-- Table structure for Operators
-- ----------------------------
DROP TABLE IF EXISTS `Operators`;
CREATE TABLE `Operators` (
  `operatorID` int NOT NULL AUTO_INCREMENT COMMENT '维修人员ID',
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '姓名',
  `password` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '密码',
  `email` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '邮箱',
  PRIMARY KEY (`operatorID`) USING BTREE,
  UNIQUE KEY `email` (`email`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of Operators
-- ----------------------------
BEGIN;
INSERT INTO `Operators` (`operatorID`, `name`, `password`, `email`) VALUES (1, 'ZZZ', '3022008', 'zhangruixian@gmail.com');
INSERT INTO `Operators` (`operatorID`, `name`, `password`, `email`) VALUES (2, 'Yuqing Ren', '9988', 'renyuqing@gmail.com');
INSERT INTO `Operators` (`operatorID`, `name`, `password`, `email`) VALUES (3, 'yujia', '321', '123456@com');
COMMIT;

-- ----------------------------
-- Table structure for Operators_ver
-- ----------------------------
DROP TABLE IF EXISTS `Operators_ver`;
CREATE TABLE `Operators_ver` (
  `operatorID` int NOT NULL AUTO_INCREMENT COMMENT '维修人员ID',
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '姓名',
  `password` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '密码',
  `email` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '邮箱',
  `code_ver` varchar(255) NOT NULL COMMENT '验证码',
  PRIMARY KEY (`operatorID`) USING BTREE,
  UNIQUE KEY `email` (`email`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of Operators_ver
-- ----------------------------
BEGIN;
INSERT INTO `Operators_ver` (`operatorID`, `name`, `password`, `email`, `code_ver`) VALUES (1, 'RRR', '3022008a', 'zhangruixian98@gmail.com', '9823');
INSERT INTO `Operators_ver` (`operatorID`, `name`, `password`, `email`, `code_ver`) VALUES (2, 'Yuqing Ren', '9988', 'renyuqing@gmail.com', '2017');
INSERT INTO `Operators_ver` (`operatorID`, `name`, `password`, `email`, `code_ver`) VALUES (3, 'zhangyujia', '123456', '2864389Z@com', '4364');
COMMIT;

-- ----------------------------
-- Table structure for Order
-- ----------------------------
DROP TABLE IF EXISTS `Order`;
CREATE TABLE `Order` (
  `orderID` int NOT NULL AUTO_INCREMENT COMMENT '订单编号',
  `renter` int NOT NULL COMMENT '租用人ID',
  `bike` int NOT NULL COMMENT '租用车ID',
  `startTime` datetime NOT NULL COMMENT '起租时间',
  `endTime` datetime DEFAULT NULL COMMENT '租用结束时间',
  `createTime` datetime NOT NULL COMMENT '订单创建时间',
  `finishTime` datetime DEFAULT NULL COMMENT '订单结束时间',
  `cost` double(10,2) DEFAULT NULL COMMENT '支付金额',
  `isPaid` tinyint(1) NOT NULL COMMENT '支付状态',
  `status` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '订单状态',
  `startStop` int DEFAULT NULL COMMENT '开始站点',
  `endStop` int DEFAULT NULL COMMENT '结束站点',
  PRIMARY KEY (`orderID`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=192 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of Order
-- ----------------------------
BEGIN;
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (1, 2, 2, '2023-10-16 15:47:04', '2023-10-16 15:47:09', '2023-10-22 15:47:04', '2023-10-22 15:47:09', 0.10, 1, '1', 1, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (2, 2, 2, '2023-10-16 15:48:01', '2023-10-16 15:48:06', '2023-10-22 15:48:01', '2023-10-22 15:48:06', 0.10, 1, '1', 2, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (3, 3, 2, '2023-10-17 15:49:14', '2023-10-17 15:49:19', '2023-10-22 15:49:14', '2023-10-22 15:49:20', 0.10, 1, '1', 3, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (4, 3, 2, '2023-10-17 15:49:57', '2023-10-17 15:50:07', '2023-10-22 15:49:57', '2023-10-22 15:50:08', 0.20, 1, '1', 4, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (5, 1, 1, '2023-10-17 15:50:49', '2023-10-17 15:50:59', '2023-10-22 15:50:49', '2023-10-22 15:51:00', 0.20, 1, '1', 5, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (6, 1, 2, '2023-10-17 15:51:20', '2023-10-17 15:51:30', '2023-10-22 15:51:20', '2023-10-22 15:51:31', 0.20, 1, '1', 1, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (7, 1, 2, '2023-10-17 16:18:32', '2023-10-17 16:18:42', '2023-10-22 16:18:32', '2023-10-22 16:18:42', 0.20, 1, '1', 2, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (8, 1, 2, '2023-10-18 16:19:01', '2023-10-18 16:19:10', '2023-10-22 16:19:01', '2023-10-22 16:19:10', 0.18, 1, '1', 3, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (9, 3, 2, '2023-10-18 16:19:34', '2023-10-18 16:19:42', '2023-10-22 16:19:34', '2023-10-22 16:19:42', 0.16, 1, '1', 4, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (10, 2, 2, '2023-10-18 15:47:04', '2023-10-18 15:47:09', '2023-10-22 15:47:04', '2023-10-22 15:47:09', 0.10, 1, '1', 5, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (11, 2, 2, '2023-10-18 15:47:04', '2023-10-18 15:47:09', '2023-10-22 15:47:04', '2023-10-22 15:47:09', 0.10, 1, '1', 1, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (12, 2, 2, '2023-10-18 15:48:01', '2023-10-18 15:48:06', '2023-10-22 15:48:01', '2023-10-22 15:48:06', 0.10, 1, '1', 2, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (13, 3, 2, '2023-10-18 15:49:14', '2023-10-18 15:49:19', '2023-10-22 15:49:14', '2023-10-22 15:49:20', 0.10, 1, '1', 3, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (14, 3, 2, '2023-10-19 15:49:57', '2023-10-19 15:50:07', '2023-10-22 15:49:57', '2023-10-22 15:50:08', 0.20, 1, '1', 4, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (15, 1, 1, '2023-10-19 15:50:49', '2023-10-19 15:50:59', '2023-10-22 15:50:49', '2023-10-22 15:51:00', 0.20, 1, '1', 5, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (16, 1, 2, '2023-10-19 15:51:20', '2023-10-19 15:51:30', '2023-10-22 15:51:20', '2023-10-22 15:51:31', 0.20, 1, '1', 1, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (17, 1, 2, '2023-10-19 16:18:32', '2023-10-19 16:18:42', '2023-10-22 16:18:32', '2023-10-22 16:18:42', 0.20, 1, '1', 2, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (18, 1, 2, '2023-10-20 16:19:01', '2023-10-20 16:19:10', '2023-10-22 16:19:01', '2023-10-22 16:19:10', 0.18, 1, '1', 3, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (19, 3, 2, '2023-10-20 16:19:34', '2023-10-20 16:19:42', '2023-10-22 16:19:34', '2023-10-22 16:19:42', 0.16, 1, '1', 4, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (20, 2, 2, '2023-10-20 15:47:04', '2023-10-20 15:47:09', '2023-10-22 15:47:04', '2023-10-22 15:47:09', 0.10, 1, '1', 5, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (21, 2, 2, '2023-10-21 15:47:04', '2023-10-21 15:47:09', '2023-10-22 15:47:04', '2023-10-22 15:47:09', 0.10, 1, '1', 1, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (22, 2, 2, '2023-10-21 15:48:01', '2023-10-21 15:48:06', '2023-10-22 15:48:01', '2023-10-22 15:48:06', 0.10, 1, '1', 2, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (23, 3, 2, '2023-10-21 15:49:14', '2023-10-21 15:49:19', '2023-10-22 15:49:14', '2023-10-22 15:49:20', 0.10, 1, '1', 3, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (24, 3, 2, '2023-10-21 15:49:57', '2023-10-21 15:50:07', '2023-10-22 15:49:57', '2023-10-22 15:50:08', 0.20, 1, '1', 4, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (25, 1, 1, '2023-10-21 15:50:49', '2023-10-21 15:50:59', '2023-10-22 15:50:49', '2023-10-22 15:51:00', 0.20, 1, '1', 5, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (26, 1, 2, '2023-10-22 15:51:20', '2023-10-22 15:51:30', '2023-10-22 15:51:20', '2023-10-22 15:51:31', 0.20, 1, '1', 1, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (27, 1, 2, '2023-10-22 16:18:32', '2023-10-22 16:18:42', '2023-10-22 16:18:32', '2023-10-22 16:18:42', 0.20, 1, '1', 2, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (28, 1, 2, '2023-10-22 16:19:01', '2023-10-22 16:19:10', '2023-10-22 16:19:01', '2023-10-22 16:19:10', 0.18, 1, '1', 3, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (29, 3, 2, '2023-10-22 16:19:34', '2023-10-22 16:19:42', '2023-10-22 16:19:34', '2023-10-22 16:19:42', 0.16, 1, '1', 4, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (30, 2, 2, '2023-10-22 15:47:04', '2023-10-22 15:47:09', '2023-10-22 15:47:04', '2023-10-22 15:47:09', 0.10, 1, '1', 5, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (31, 2, 11, '2023-10-25 11:33:37', '2023-10-25 11:40:37', '2023-10-25 11:33:37', '2023-10-25 17:17:05', 8.40, 1, '1', 2, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (32, 1, 1, '2023-10-25 13:07:06', '2023-10-25 13:20:06', '2023-10-25 13:07:06', '2023-10-25 17:36:32', 15.60, 1, '1', 8, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (33, 1, 1, '2023-10-25 09:31:22', '2023-10-25 09:42:22', '2023-10-25 09:31:22', '2023-10-25 23:59:59', 13.20, 1, '1', 5, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (34, 3, 16, '2023-10-25 21:15:52', '2023-10-25 21:27:52', '2023-10-25 21:15:52', '2023-10-25 23:59:59', 14.40, 1, '1', 4, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (35, 4, 21, '2023-10-25 16:27:25', '2023-10-25 16:39:25', '2023-10-25 16:27:25', '2023-10-25 23:59:59', 14.40, 1, '1', 3, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (36, 2, 1, '2023-10-25 23:59:25', '2023-10-25 23:59:59', '2023-10-25 23:59:25', '2023-10-25 23:59:59', 0.68, 1, '1', 4, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (37, 4, 4, '2023-10-25 08:55:24', '2023-10-25 09:01:24', '2023-10-25 08:55:24', '2023-10-25 10:03:56', 7.20, 1, '1', 2, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (38, 2, 3, '2023-10-25 06:30:14', '2023-10-25 06:51:14', '2023-10-25 06:30:14', '2023-10-25 17:30:40', 25.20, 1, '1', 3, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (39, 3, 5, '2023-10-25 20:17:27', '2023-10-25 20:32:27', '2023-10-25 20:17:27', '2023-10-25 23:59:59', 18.00, 1, '1', 7, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (40, 1, 6, '2023-10-25 23:53:55', '2023-10-25 23:59:59', '2023-10-25 23:53:55', '2023-10-25 23:59:59', 7.28, 1, '1', 5, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (41, 1, 1, '2023-10-25 22:19:10', '2023-10-25 22:22:10', '2023-10-25 22:19:10', '2023-10-25 23:59:59', 3.60, 1, '1', 1, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (42, 4, 23, '2023-10-25 10:52:23', '2023-10-25 10:54:23', '2023-10-25 10:52:23', '2023-10-25 11:23:04', 2.40, 1, '1', 7, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (43, 1, 11, '2023-10-25 01:39:55', '2023-10-25 01:49:55', '2023-10-25 01:39:55', '2023-10-25 05:02:50', 12.00, 1, '1', 7, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (44, 1, 22, '2023-10-25 12:27:28', '2023-10-25 12:51:28', '2023-10-25 12:27:28', '2023-10-25 23:59:59', 28.80, 1, '1', 3, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (45, 1, 1, '2023-10-25 23:23:04', '2023-10-25 23:26:04', '2023-10-25 23:23:04', '2023-10-25 23:59:59', 3.60, 1, '1', 7, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (46, 2, 20, '2023-10-25 08:33:22', '2023-10-25 09:03:22', '2023-10-25 08:33:22', '2023-10-25 15:12:34', 36.00, 1, '1', 2, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (47, 2, 18, '2023-10-25 03:28:01', '2023-10-25 03:53:01', '2023-10-25 03:28:01', '2023-10-25 16:25:20', 30.00, 1, '1', 4, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (48, 1, 20, '2023-10-25 20:30:46', '2023-10-25 20:47:46', '2023-10-25 20:30:46', '2023-10-25 23:59:59', 20.40, 1, '1', 3, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (49, 3, 2, '2023-10-25 21:11:36', '2023-10-25 21:38:36', '2023-10-25 21:11:36', '2023-10-25 23:59:59', 32.40, 1, '1', 2, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (50, 1, 7, '2023-10-25 09:13:00', '2023-10-25 09:13:00', '2023-10-25 09:13:00', '2023-10-25 20:23:38', 0.00, 1, '1', 5, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (51, 3, 21, '2023-10-26 12:37:52', '2023-10-26 12:40:52', '2023-10-26 12:37:52', '2023-10-26 23:59:59', 3.60, 1, '1', 6, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (52, 2, 6, '2023-10-26 04:23:47', '2023-10-26 04:42:47', '2023-10-26 04:23:47', '2023-10-26 23:59:59', 22.80, 1, '1', 1, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (53, 1, 24, '2023-10-26 13:01:44', '2023-10-26 13:25:44', '2023-10-26 13:01:44', '2023-10-26 20:57:45', 28.80, 1, '1', 7, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (54, 3, 21, '2023-10-26 12:36:27', '2023-10-26 12:57:27', '2023-10-26 12:36:27', '2023-10-26 23:59:59', 25.20, 1, '1', 6, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (55, 3, 24, '2023-10-26 20:07:50', '2023-10-26 20:29:50', '2023-10-26 20:07:50', '2023-10-26 23:59:59', 26.40, 1, '1', 3, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (56, 1, 11, '2023-10-26 00:55:15', '2023-10-26 00:55:15', '2023-10-26 00:55:15', '2023-10-26 02:52:57', 0.00, 1, '1', 6, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (57, 4, 24, '2023-10-26 11:39:30', '2023-10-26 12:04:30', '2023-10-26 11:39:30', '2023-10-26 22:40:15', 30.00, 1, '1', 4, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (58, 4, 7, '2023-10-26 02:57:49', '2023-10-26 03:26:49', '2023-10-26 02:57:49', '2023-10-26 13:13:11', 34.80, 1, '1', 5, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (59, 1, 7, '2023-10-26 21:11:38', '2023-10-26 21:26:38', '2023-10-26 21:11:38', '2023-10-26 23:59:59', 18.00, 1, '1', 4, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (60, 1, 16, '2023-10-26 16:31:15', '2023-10-26 16:38:15', '2023-10-26 16:31:15', '2023-10-26 23:59:59', 8.40, 1, '1', 4, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (61, 3, 1, '2023-10-26 23:03:40', '2023-10-26 23:22:40', '2023-10-26 23:03:40', '2023-10-26 23:59:59', 22.80, 1, '1', 7, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (62, 2, 13, '2023-10-26 15:59:39', '2023-10-26 16:29:39', '2023-10-26 15:59:39', '2023-10-26 23:59:59', 36.00, 1, '1', 8, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (63, 2, 2, '2023-10-26 02:30:26', '2023-10-26 02:44:26', '2023-10-26 02:30:26', '2023-10-26 08:50:58', 16.80, 1, '1', 8, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (64, 3, 16, '2023-10-26 00:31:09', '2023-10-26 01:01:09', '2023-10-26 00:31:09', '2023-10-26 05:16:14', 36.00, 1, '1', 1, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (65, 3, 13, '2023-10-26 09:33:37', '2023-10-26 09:46:37', '2023-10-26 09:33:37', '2023-10-26 23:59:59', 15.60, 1, '1', 1, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (66, 2, 17, '2023-10-26 02:55:29', '2023-10-26 02:56:29', '2023-10-26 02:55:29', '2023-10-26 13:09:34', 1.20, 1, '1', 5, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (67, 3, 12, '2023-10-26 17:22:05', '2023-10-26 17:52:05', '2023-10-26 17:22:05', '2023-10-26 23:59:59', 36.00, 1, '1', 5, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (68, 2, 9, '2023-10-26 06:16:47', '2023-10-26 06:34:47', '2023-10-26 06:16:47', '2023-10-26 11:53:27', 21.60, 1, '1', 6, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (69, 2, 6, '2023-10-26 04:30:28', '2023-10-26 04:38:28', '2023-10-26 04:30:28', '2023-10-26 23:59:59', 9.60, 1, '1', 1, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (70, 3, 5, '2023-10-26 10:39:16', '2023-10-26 11:06:16', '2023-10-26 10:39:16', '2023-10-26 15:03:07', 32.40, 1, '1', 6, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (71, 4, 21, '2023-10-27 05:14:57', '2023-10-27 05:43:57', '2023-10-27 05:14:57', '2023-10-27 11:06:37', 34.80, 1, '1', 8, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (72, 4, 4, '2023-10-27 00:11:14', '2023-10-27 00:32:14', '2023-10-27 00:11:14', '2023-10-27 19:09:14', 25.20, 1, '1', 2, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (73, 4, 23, '2023-10-27 10:08:04', '2023-10-27 10:15:04', '2023-10-27 10:08:04', '2023-10-27 23:48:24', 8.40, 1, '1', 7, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (74, 1, 22, '2023-10-27 02:34:05', '2023-10-27 02:45:05', '2023-10-27 02:34:05', '2023-10-27 15:31:23', 13.20, 1, '1', 8, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (75, 1, 23, '2023-10-27 14:10:47', '2023-10-27 14:25:47', '2023-10-27 14:10:47', '2023-10-27 23:28:34', 18.00, 1, '1', 6, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (76, 3, 17, '2023-10-27 03:11:17', '2023-10-27 03:30:17', '2023-10-27 03:11:17', '2023-10-27 06:46:33', 22.80, 1, '1', 3, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (77, 2, 20, '2023-10-27 04:19:12', '2023-10-27 04:27:12', '2023-10-27 04:19:12', '2023-10-27 07:52:45', 9.60, 1, '1', 2, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (78, 1, 15, '2023-10-27 20:44:26', '2023-10-27 21:08:26', '2023-10-27 20:44:26', '2023-10-27 23:59:59', 28.80, 1, '1', 4, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (79, 3, 10, '2023-10-27 01:09:42', '2023-10-27 01:36:42', '2023-10-27 01:09:42', '2023-10-27 22:06:37', 32.40, 1, '1', 7, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (80, 1, 20, '2023-10-27 16:19:21', '2023-10-27 16:41:21', '2023-10-27 16:19:21', '2023-10-27 20:41:49', 26.40, 1, '1', 5, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (81, 3, 22, '2023-10-27 09:25:15', '2023-10-27 09:39:15', '2023-10-27 09:25:15', '2023-10-27 14:50:36', 16.80, 1, '1', 7, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (82, 3, 11, '2023-10-27 04:10:19', '2023-10-27 04:12:19', '2023-10-27 04:10:19', '2023-10-27 07:10:39', 2.40, 1, '1', 1, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (83, 1, 16, '2023-10-27 12:31:16', '2023-10-27 12:54:16', '2023-10-27 12:31:16', '2023-10-27 23:59:59', 27.60, 1, '1', 3, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (84, 4, 12, '2023-10-27 18:08:19', '2023-10-27 18:25:19', '2023-10-27 18:08:19', '2023-10-27 21:11:38', 20.40, 1, '1', 1, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (85, 1, 10, '2023-10-27 18:33:55', '2023-10-27 18:40:55', '2023-10-27 18:33:55', '2023-10-27 23:59:59', 8.40, 1, '1', 1, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (86, 4, 3, '2023-10-27 06:24:36', '2023-10-27 06:50:36', '2023-10-27 06:24:36', '2023-10-27 19:22:22', 31.20, 1, '1', 4, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (87, 4, 4, '2023-10-27 16:30:19', '2023-10-27 16:49:19', '2023-10-27 16:30:19', '2023-10-27 23:59:59', 22.80, 1, '1', 3, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (88, 4, 2, '2023-10-27 22:09:56', '2023-10-27 22:18:56', '2023-10-27 22:09:56', '2023-10-27 23:59:59', 10.80, 1, '1', 5, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (89, 2, 8, '2023-10-27 22:51:22', '2023-10-27 23:21:22', '2023-10-27 22:51:22', '2023-10-27 23:59:59', 36.00, 1, '1', 2, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (90, 4, 19, '2023-10-27 00:07:45', '2023-10-27 00:14:45', '2023-10-27 00:07:45', '2023-10-27 03:41:42', 8.40, 1, '1', 5, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (91, 3, 24, '2023-10-28 08:57:22', '2023-10-28 09:21:22', '2023-10-28 08:57:22', '2023-10-28 15:48:05', 28.80, 1, '1', 4, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (92, 1, 16, '2023-10-28 16:27:13', '2023-10-28 16:50:13', '2023-10-28 16:27:13', '2023-10-28 23:59:59', 27.60, 1, '1', 5, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (93, 1, 17, '2023-10-28 20:06:57', '2023-10-28 20:16:57', '2023-10-28 20:06:57', '2023-10-28 23:59:59', 12.00, 1, '1', 7, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (94, 3, 7, '2023-10-28 05:33:44', '2023-10-28 05:50:44', '2023-10-28 05:33:44', '2023-10-28 13:35:00', 20.40, 1, '1', 2, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (95, 3, 1, '2023-10-28 19:26:14', '2023-10-28 19:43:14', '2023-10-28 19:26:14', '2023-10-28 23:59:59', 20.40, 1, '1', 1, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (96, 4, 11, '2023-10-28 08:50:47', '2023-10-28 09:10:47', '2023-10-28 08:50:47', '2023-10-28 23:59:59', 24.00, 1, '1', 6, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (97, 4, 11, '2023-10-28 02:08:26', '2023-10-28 02:31:26', '2023-10-28 02:08:26', '2023-10-28 12:58:16', 27.60, 1, '1', 2, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (98, 4, 13, '2023-10-28 02:07:08', '2023-10-28 02:18:08', '2023-10-28 02:07:08', '2023-10-28 20:22:23', 13.20, 1, '1', 3, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (99, 2, 3, '2023-10-28 15:03:37', '2023-10-28 15:32:37', '2023-10-28 15:03:37', '2023-10-28 23:59:59', 34.80, 1, '1', 2, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (100, 2, 7, '2023-10-28 19:26:25', '2023-10-28 19:51:25', '2023-10-28 19:26:25', '2023-10-28 23:59:59', 30.00, 1, '1', 7, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (101, 4, 3, '2023-10-28 14:20:19', '2023-10-28 14:35:19', '2023-10-28 14:20:19', '2023-10-28 18:50:13', 18.00, 1, '1', 7, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (102, 3, 20, '2023-10-28 18:59:06', '2023-10-28 19:13:06', '2023-10-28 18:59:06', '2023-10-28 23:59:59', 16.80, 1, '1', 1, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (103, 4, 9, '2023-10-28 21:07:17', '2023-10-28 21:14:17', '2023-10-28 21:07:17', '2023-10-28 23:59:59', 8.40, 1, '1', 4, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (104, 1, 8, '2023-10-28 06:06:58', '2023-10-28 06:12:58', '2023-10-28 06:06:58', '2023-10-28 11:29:49', 7.20, 1, '1', 2, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (105, 4, 20, '2023-10-28 08:40:50', '2023-10-28 08:45:50', '2023-10-28 08:40:50', '2023-10-28 11:44:39', 6.00, 1, '1', 1, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (106, 1, 22, '2023-10-28 05:09:42', '2023-10-28 05:15:42', '2023-10-28 05:09:42', '2023-10-28 11:23:10', 7.20, 1, '1', 4, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (107, 1, 2, '2023-10-28 21:54:01', '2023-10-28 22:16:01', '2023-10-28 21:54:01', '2023-10-28 23:59:59', 26.40, 1, '1', 7, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (108, 2, 17, '2023-10-28 16:11:42', '2023-10-28 16:32:42', '2023-10-28 16:11:42', '2023-10-28 23:59:59', 25.20, 1, '1', 2, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (109, 2, 15, '2023-10-28 23:19:57', '2023-10-28 23:36:57', '2023-10-28 23:19:57', '2023-10-28 23:59:59', 20.40, 1, '1', 3, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (110, 1, 21, '2023-10-28 10:25:43', '2023-10-28 10:30:43', '2023-10-28 10:25:43', '2023-10-28 23:59:59', 6.00, 1, '1', 2, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (111, 2, 14, '2023-10-29 00:50:41', '2023-10-29 01:02:41', '2023-10-29 00:50:41', '2023-10-29 07:33:46', 14.40, 1, '1', 1, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (112, 3, 14, '2023-10-29 04:35:21', '2023-10-29 04:57:21', '2023-10-29 04:35:21', '2023-10-29 23:59:59', 26.40, 1, '1', 5, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (113, 2, 6, '2023-10-29 08:56:11', '2023-10-29 09:17:11', '2023-10-29 08:56:11', '2023-10-29 23:15:31', 25.20, 1, '1', 3, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (114, 3, 22, '2023-10-29 03:19:35', '2023-10-29 03:48:35', '2023-10-29 03:19:35', '2023-10-29 16:25:19', 34.80, 1, '1', 4, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (115, 1, 17, '2023-10-29 08:25:19', '2023-10-29 08:30:19', '2023-10-29 08:25:19', '2023-10-29 18:33:48', 6.00, 1, '1', 7, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (116, 1, 24, '2023-10-29 02:33:46', '2023-10-29 02:45:46', '2023-10-29 02:33:46', '2023-10-29 23:59:59', 14.40, 1, '1', 5, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (117, 3, 18, '2023-10-29 07:23:18', '2023-10-29 07:26:18', '2023-10-29 07:23:18', '2023-10-29 18:45:43', 3.60, 1, '1', 4, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (118, 4, 1, '2023-10-29 22:17:42', '2023-10-29 22:38:42', '2023-10-29 22:17:42', '2023-10-29 23:59:59', 25.20, 1, '1', 1, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (119, 2, 13, '2023-10-29 16:45:01', '2023-10-29 16:59:01', '2023-10-29 16:45:01', '2023-10-29 19:58:35', 16.80, 1, '1', 2, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (120, 2, 8, '2023-10-29 12:40:51', '2023-10-29 12:47:51', '2023-10-29 12:40:51', '2023-10-29 19:19:41', 8.40, 1, '1', 7, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (121, 1, 10, '2023-10-29 16:49:13', '2023-10-29 17:14:13', '2023-10-29 16:49:13', '2023-10-29 18:02:10', 30.00, 1, '1', 8, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (122, 3, 20, '2023-10-29 19:47:05', '2023-10-29 20:08:05', '2023-10-29 19:47:05', '2023-10-29 23:59:59', 25.20, 1, '1', 7, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (123, 1, 16, '2023-10-29 16:51:53', '2023-10-29 17:05:53', '2023-10-29 16:51:53', '2023-10-29 23:47:55', 16.80, 1, '1', 2, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (124, 3, 5, '2023-10-29 08:54:52', '2023-10-29 09:03:52', '2023-10-29 08:54:52', '2023-10-29 23:59:59', 10.80, 1, '1', 6, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (125, 4, 22, '2023-10-29 12:32:49', '2023-10-29 12:32:49', '2023-10-29 12:32:49', '2023-10-29 23:15:07', 0.00, 1, '1', 7, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (126, 2, 1, '2023-10-29 00:33:31', '2023-10-29 00:40:31', '2023-10-29 00:33:31', '2023-10-29 18:54:07', 8.40, 1, '1', 4, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (127, 1, 1, '2023-10-29 16:47:01', '2023-10-29 17:00:01', '2023-10-29 16:47:01', '2023-10-29 23:59:59', 15.60, 1, '1', 6, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (128, 1, 18, '2023-10-29 13:47:06', '2023-10-29 13:55:06', '2023-10-29 13:47:06', '2023-10-29 20:53:00', 9.60, 1, '1', 7, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (129, 1, 4, '2023-10-29 06:30:51', '2023-10-29 06:41:51', '2023-10-29 06:30:51', '2023-10-29 22:28:50', 13.20, 1, '1', 1, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (130, 1, 1, '2023-10-29 20:36:45', '2023-10-29 21:05:45', '2023-10-29 20:36:45', '2023-10-29 23:59:59', 34.80, 1, '1', 7, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (131, 2, 8, '2023-10-30 21:05:33', '2023-10-30 21:18:33', '2023-10-30 21:05:33', '2023-10-30 23:59:59', 15.60, 1, '1', 1, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (132, 3, 24, '2023-10-30 10:02:24', '2023-10-30 10:08:24', '2023-10-30 10:02:24', '2023-10-30 21:30:51', 7.20, 1, '1', 2, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (133, 3, 20, '2023-10-30 23:16:19', '2023-10-30 23:20:19', '2023-10-30 23:16:19', '2023-10-30 23:59:59', 4.80, 1, '1', 5, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (134, 3, 4, '2023-10-30 06:30:11', '2023-10-30 06:53:11', '2023-10-30 06:30:11', '2023-10-30 23:59:59', 27.60, 1, '1', 5, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (135, 2, 15, '2023-10-30 16:51:26', '2023-10-30 17:13:26', '2023-10-30 16:51:26', '2023-10-30 23:59:59', 26.40, 1, '1', 2, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (136, 2, 20, '2023-10-30 18:31:21', '2023-10-30 18:31:21', '2023-10-30 18:31:21', '2023-10-30 20:04:00', 0.00, 1, '1', 3, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (137, 1, 22, '2023-10-30 02:06:06', '2023-10-30 02:14:06', '2023-10-30 02:06:06', '2023-10-30 23:42:04', 9.60, 1, '1', 2, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (138, 3, 13, '2023-10-30 16:59:37', '2023-10-30 17:14:37', '2023-10-30 16:59:37', '2023-10-30 23:59:59', 18.00, 1, '1', 1, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (139, 4, 16, '2023-10-30 06:58:51', '2023-10-30 07:20:51', '2023-10-30 06:58:51', '2023-10-30 19:36:07', 26.40, 1, '1', 8, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (140, 4, 3, '2023-10-30 00:59:00', '2023-10-30 01:15:00', '2023-10-30 00:59:00', '2023-10-30 09:24:45', 19.20, 1, '1', 8, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (141, 2, 13, '2023-10-30 00:46:18', '2023-10-30 01:09:18', '2023-10-30 00:46:18', '2023-10-30 23:23:42', 27.60, 1, '1', 8, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (142, 2, 24, '2023-10-30 05:04:03', '2023-10-30 05:26:03', '2023-10-30 05:04:03', '2023-10-30 05:57:29', 26.40, 1, '1', 8, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (143, 2, 6, '2023-10-30 09:38:10', '2023-10-30 10:04:10', '2023-10-30 09:38:10', '2023-10-30 23:59:59', 31.20, 1, '1', 7, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (144, 2, 21, '2023-10-30 15:50:52', '2023-10-30 15:53:52', '2023-10-30 15:50:52', '2023-10-30 23:59:59', 3.60, 1, '1', 4, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (145, 3, 1, '2023-10-30 13:09:17', '2023-10-30 13:09:17', '2023-10-30 13:09:17', '2023-10-30 23:59:59', 0.00, 1, '1', 7, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (146, 2, 4, '2023-10-30 06:54:44', '2023-10-30 07:18:44', '2023-10-30 06:54:44', '2023-10-30 23:59:59', 28.80, 1, '1', 8, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (147, 4, 10, '2023-10-30 09:22:45', '2023-10-30 09:23:45', '2023-10-30 09:22:45', '2023-10-30 16:59:10', 1.20, 1, '1', 4, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (148, 3, 14, '2023-10-30 18:20:07', '2023-10-30 18:34:07', '2023-10-30 18:20:07', '2023-10-30 23:59:59', 16.80, 1, '1', 3, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (149, 3, 12, '2023-10-30 09:39:41', '2023-10-30 09:39:41', '2023-10-30 09:39:41', '2023-10-30 23:59:59', 0.00, 1, '1', 6, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (150, 4, 20, '2023-10-30 16:55:44', '2023-10-30 17:25:44', '2023-10-30 16:55:44', '2023-10-30 23:59:59', 36.00, 1, '1', 2, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (151, 3, 23, '2023-10-31 09:23:58', '2023-10-31 09:48:58', '2023-10-31 09:23:58', '2023-10-31 10:03:32', 30.00, 1, '1', 4, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (152, 3, 1, '2023-10-31 22:45:42', '2023-10-31 22:48:42', '2023-10-31 22:45:42', '2023-10-31 23:59:59', 3.60, 1, '1', 3, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (153, 3, 16, '2023-10-31 00:29:38', '2023-10-31 00:37:38', '2023-10-31 00:29:38', '2023-10-31 17:19:39', 9.60, 1, '1', 7, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (154, 1, 15, '2023-10-31 02:58:28', '2023-10-31 03:10:28', '2023-10-31 02:58:28', '2023-10-31 04:51:56', 14.40, 1, '1', 6, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (155, 3, 4, '2023-10-31 09:46:00', '2023-10-31 09:57:00', '2023-10-31 09:46:00', '2023-10-31 10:09:20', 13.20, 1, '1', 5, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (156, 3, 14, '2023-10-31 05:47:59', '2023-10-31 06:00:59', '2023-10-31 05:47:59', '2023-10-31 21:03:02', 15.60, 1, '1', 6, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (157, 1, 22, '2023-10-31 15:17:24', '2023-10-31 15:32:24', '2023-10-31 15:17:24', '2023-10-31 23:59:59', 18.00, 1, '1', 3, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (158, 2, 9, '2023-10-31 03:15:25', '2023-10-31 03:35:25', '2023-10-31 03:15:25', '2023-10-31 13:26:05', 24.00, 1, '1', 3, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (159, 4, 23, '2023-10-31 12:12:58', '2023-10-31 12:16:58', '2023-10-31 12:12:58', '2023-10-31 23:59:59', 4.80, 1, '1', 8, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (160, 3, 23, '2023-10-31 10:37:22', '2023-10-31 10:50:22', '2023-10-31 10:37:22', '2023-10-31 23:59:59', 15.60, 1, '1', 8, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (161, 3, 15, '2023-10-31 12:28:14', '2023-10-31 12:47:14', '2023-10-31 12:28:14', '2023-10-31 23:59:59', 22.80, 1, '1', 2, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (162, 2, 2, '2023-10-31 16:16:23', '2023-10-31 16:40:23', '2023-10-31 16:16:23', '2023-10-31 23:59:59', 28.80, 1, '1', 6, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (163, 3, 5, '2023-10-31 09:34:50', '2023-10-31 09:36:50', '2023-10-31 09:34:50', '2023-10-31 23:59:59', 2.40, 1, '1', 3, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (164, 2, 9, '2023-10-31 15:40:19', '2023-10-31 16:10:19', '2023-10-31 15:40:19', '2023-10-31 23:59:59', 36.00, 1, '1', 4, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (165, 1, 24, '2023-10-31 16:36:16', '2023-10-31 17:01:16', '2023-10-31 16:36:16', '2023-10-31 23:59:59', 30.00, 1, '1', 3, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (166, 4, 9, '2023-10-31 09:20:26', '2023-10-31 09:48:26', '2023-10-31 09:20:26', '2023-10-31 23:59:59', 33.60, 1, '1', 8, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (167, 3, 1, '2023-10-31 21:16:50', '2023-10-31 21:23:50', '2023-10-31 21:16:50', '2023-10-31 23:59:59', 8.40, 1, '1', 5, 4);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (168, 3, 12, '2023-10-31 11:19:22', '2023-10-31 11:41:22', '2023-10-31 11:19:22', '2023-10-31 23:59:59', 26.40, 1, '1', 1, 8);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (169, 1, 20, '2023-10-31 22:16:53', '2023-10-31 22:46:53', '2023-10-31 22:16:53', '2023-10-31 23:55:51', 36.00, 1, '1', 2, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (170, 1, 12, '2023-10-31 21:30:21', '2023-10-31 21:42:21', '2023-10-31 21:30:21', '2023-10-31 21:56:32', 14.40, 1, '1', 2, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (171, 4, 4, '2023-11-01 19:54:34', '2023-11-01 20:18:34', '2023-11-01 19:54:34', '2023-11-01 23:59:59', 28.80, 1, '1', 4, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (172, 4, 15, '2023-11-01 17:34:25', '2023-11-01 17:58:25', '2023-11-01 17:34:25', '2023-11-01 23:59:59', 28.80, 1, '1', 3, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (173, 3, 9, '2023-11-01 00:42:04', '2023-11-01 01:03:04', '2023-11-01 00:42:04', '2023-11-01 02:19:32', 25.20, 1, '1', 8, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (174, 4, 20, '2023-11-01 11:01:07', '2023-11-01 11:30:07', '2023-11-01 11:01:07', '2023-11-01 11:41:27', 34.80, 1, '1', 5, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (175, 1, 13, '2023-11-01 17:22:44', '2023-11-01 17:41:44', '2023-11-01 17:22:44', '2023-11-01 19:04:26', 22.80, 1, '1', 6, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (176, 1, 20, '2023-11-01 23:49:17', '2023-11-01 23:55:17', '2023-11-01 23:49:17', '2023-11-01 23:59:59', 7.20, 1, '1', 4, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (177, 1, 21, '2023-11-01 06:04:52', '2023-11-01 06:31:52', '2023-11-01 06:04:52', '2023-11-01 16:26:11', 32.40, 1, '1', 7, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (178, 4, 20, '2023-11-01 01:52:18', '2023-11-01 02:17:18', '2023-11-01 01:52:18', '2023-11-01 03:43:31', 30.00, 1, '1', 6, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (179, 1, 21, '2023-11-01 14:03:07', '2023-11-01 14:04:07', '2023-11-01 14:03:07', '2023-11-01 23:59:59', 1.20, 1, '1', 6, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (180, 3, 4, '2023-11-01 02:27:23', '2023-11-01 02:55:23', '2023-11-01 02:27:23', '2023-11-01 16:06:11', 33.60, 1, '1', 7, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (181, 4, 20, '2023-11-01 23:04:56', '2023-11-01 23:26:56', '2023-11-01 23:04:56', '2023-11-01 23:59:59', 26.40, 1, '1', 2, 3);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (182, 1, 21, '2023-11-01 12:39:33', '2023-11-01 12:51:33', '2023-11-01 12:39:33', '2023-11-01 23:59:59', 14.40, 1, '1', 7, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (183, 4, 15, '2023-11-01 01:01:49', '2023-11-01 01:22:49', '2023-11-01 01:01:49', '2023-11-01 20:46:00', 25.20, 1, '1', 7, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (184, 3, 18, '2023-11-01 13:41:58', '2023-11-01 13:56:58', '2023-11-01 13:41:58', '2023-11-01 21:03:21', 18.00, 1, '1', 2, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (185, 3, 19, '2023-11-01 00:34:21', '2023-11-01 00:36:21', '2023-11-01 00:34:21', '2023-11-01 04:33:31', 2.40, 1, '1', 4, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (186, 1, 3, '2023-11-01 04:13:58', '2023-11-01 04:20:58', '2023-11-01 04:13:58', '2023-11-01 11:53:20', 8.40, 1, '1', 2, 2);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (187, 3, 16, '2023-11-01 19:35:49', '2023-11-01 19:38:49', '2023-11-01 19:35:49', '2023-11-01 23:59:59', 3.60, 1, '1', 7, 6);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (188, 3, 23, '2023-11-01 07:51:50', '2023-11-01 08:18:50', '2023-11-01 07:51:50', '2023-11-01 10:05:52', 32.40, 1, '1', 3, 5);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (189, 2, 15, '2023-11-01 00:41:17', '2023-11-01 01:11:17', '2023-11-01 00:41:17', '2023-11-01 23:59:59', 36.00, 1, '1', 4, 1);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (190, 4, 16, '2023-11-01 12:48:07', '2023-11-01 13:13:07', '2023-11-01 12:48:07', '2023-11-01 23:59:59', 30.00, 1, '1', 4, 7);
INSERT INTO `Order` (`orderID`, `renter`, `bike`, `startTime`, `endTime`, `createTime`, `finishTime`, `cost`, `isPaid`, `status`, `startStop`, `endStop`) VALUES (191, 9, 11, '2023-11-01 23:20:32', '2023-11-01 23:20:50', '2023-11-01 23:20:32', '2023-11-01 23:21:28', 0.36, 1, '1', 1, 2);
COMMIT;

-- ----------------------------
-- Table structure for Records
-- ----------------------------
DROP TABLE IF EXISTS `Records`;
CREATE TABLE `Records` (
  `recordID` int NOT NULL COMMENT '维修记录ID',
  `operator` varchar(255) NOT NULL COMMENT '维修人',
  `date` datetime DEFAULT NULL COMMENT '维修时间',
  `bikeID` int NOT NULL COMMENT '维修车辆ID',
  `status` varchar(255) DEFAULT NULL COMMENT '具体操作',
  PRIMARY KEY (`recordID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of Records
-- ----------------------------
BEGIN;
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (1, 'zhangruixian@gmail.com', '2023-10-22 21:42:24', 1, 'change new battery');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (2, 'zhangruixian@gmail.com', '2023-10-22 22:10:19', 4, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (3, 'zhangruixian@gmail.com', '2023-10-22 22:12:35', 4, 'Delete the bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (4, 'zhangruixian@gmail.com', '2023-10-22 22:21:26', 3, 'Change location: 2 to 1');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (5, 'zhangruixian@gmail.com', '2023-10-22 22:24:21', 3, 'Fixing bike: 3');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (6, 'zhangruixian@gmail.com', '2023-10-22 22:46:22', 2, 'Fixing bike is done: 2');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (7, 'zhangruixian@gmail.com', '2023-10-22 22:47:50', 1, 'Fixing bike: 1');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (8, 'zhangruixian@gmail.com', '2023-10-22 22:50:45', 2, 'Fixing bike: 2');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (9, 'zhangruixian@gmail.com', '2023-10-22 22:53:02', 1, 'Fixing bike: 1');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (10, 'zhangruixian@gmail.com', '2023-10-22 22:55:53', 3, 'Fixing bike: 3');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (11, 'zhangruixian@gmail.com', '2023-10-22 22:56:45', 1, 'Fixing bike: 1');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (12, 'zhangruixian@gmail.com', '2023-10-22 22:56:50', 1, 'Fixing bike is done: 1');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (13, 'zhangruixian@gmail.com', '2023-10-28 08:51:19', 4, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (14, 'zhangruixian@gmail.com', '2023-10-28 09:07:07', 4, 'Delete bike id is: 4');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (15, 'zhangruixian@gmail.com', '2023-10-28 11:27:53', 2, 'change new battery');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (16, 'zhangruixian@gmail.com', '2023-10-28 11:34:23', 3, 'Change location: 2 to 1');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (17, 'zhangruixian@gmail.com', '2023-10-28 11:57:36', 2, 'Fixing bike: 2');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (18, 'zhangruixian@gmail.com', '2023-10-28 11:58:22', 2, 'Fixing bike is done: 2');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (19, 'zhangruixian@gmail.com', '2023-10-28 14:02:21', 4, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (20, 'renyuqing@gmail.com', '2023-10-31 17:09:38', 5, 'Delete bike id is: 5');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (21, 'renyuqing@gmail.com', '2023-10-31 17:16:19', 3, 'change new battery');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (22, 'renyuqing@gmail.com', '2023-10-31 17:16:27', 3, 'change new battery');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (23, 'renyuqing@gmail.com', '2023-10-31 20:07:12', 3, 'Delete bike id is: 3');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (24, 'renyuqing@gmail.com', '2023-10-31 20:07:37', 2, 'Change location: 1 to 3');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (25, 'renyuqing@gmail.com', '2023-10-31 20:07:55', 4, 'change new battery');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (26, 'zhangruixian@gmail.com', '2023-10-31 20:58:21', 5, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (27, 'zhangruixian@gmail.com', '2023-10-31 21:01:20', 6, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (28, 'zhangruixian@gmail.com', '2023-10-31 21:01:20', 6, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (29, 'zhangruixian@gmail.com', '2023-10-31 21:01:20', 6, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (30, 'zhangruixian@gmail.com', '2023-10-31 21:01:20', 6, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (31, 'zhangruixian@gmail.com', '2023-10-31 21:01:20', 6, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (32, 'zhangruixian@gmail.com', '2023-10-31 21:01:20', 6, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (33, 'zhangruixian@gmail.com', '2023-10-31 21:01:20', 6, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (34, 'zhangruixian@gmail.com', '2023-10-31 21:01:20', 6, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (35, 'zhangruixian@gmail.com', '2023-10-31 21:01:20', 6, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (36, 'zhangruixian@gmail.com', '2023-10-31 21:01:21', 6, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (37, 'zhangruixian@gmail.com', '2023-10-31 21:02:32', 7, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (38, 'zhangruixian@gmail.com', '2023-10-31 21:02:32', 7, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (39, 'zhangruixian@gmail.com', '2023-10-31 21:02:32', 7, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (40, 'zhangruixian@gmail.com', '2023-10-31 21:02:32', 7, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (41, 'zhangruixian@gmail.com', '2023-10-31 21:02:33', 7, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (42, 'zhangruixian@gmail.com', '2023-10-31 21:02:33', 7, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (43, 'zhangruixian@gmail.com', '2023-10-31 21:02:33', 7, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (44, 'zhangruixian@gmail.com', '2023-10-31 21:02:33', 7, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (45, 'zhangruixian@gmail.com', '2023-10-31 21:02:33', 7, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (46, 'zhangruixian@gmail.com', '2023-10-31 21:02:33', 7, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (47, 'zhangruixian@gmail.com', '2023-10-31 21:03:13', 8, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (48, 'zhangruixian@gmail.com', '2023-10-31 21:03:13', 8, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (49, 'zhangruixian@gmail.com', '2023-10-31 21:03:13', 8, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (50, 'zhangruixian@gmail.com', '2023-10-31 21:03:14', 8, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (51, 'zhangruixian@gmail.com', '2023-10-31 21:03:14', 8, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (52, 'zhangruixian@gmail.com', '2023-10-31 21:03:14', 8, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (53, 'zhangruixian@gmail.com', '2023-10-31 21:03:14', 8, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (54, 'zhangruixian@gmail.com', '2023-10-31 21:03:14', 8, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (55, 'zhangruixian@gmail.com', '2023-10-31 21:03:14', 8, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (56, 'zhangruixian@gmail.com', '2023-10-31 21:03:14', 8, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (57, 'zhangruixian@gmail.com', '2023-10-31 21:05:21', 9, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (58, 'zhangruixian@gmail.com', '2023-10-31 21:05:21', 9, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (59, 'zhangruixian@gmail.com', '2023-10-31 21:05:21', 9, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (60, 'zhangruixian@gmail.com', '2023-10-31 21:05:22', 9, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (61, 'zhangruixian@gmail.com', '2023-10-31 21:05:22', 9, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (62, 'zhangruixian@gmail.com', '2023-10-31 21:05:22', 9, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (63, 'zhangruixian@gmail.com', '2023-10-31 21:05:22', 9, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (64, 'zhangruixian@gmail.com', '2023-10-31 21:05:22', 9, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (65, 'zhangruixian@gmail.com', '2023-10-31 21:05:22', 9, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (66, 'zhangruixian@gmail.com', '2023-10-31 21:05:22', 9, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (67, 'zhangruixian@gmail.com', '2023-10-31 21:05:59', 10, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (68, 'zhangruixian@gmail.com', '2023-10-31 21:05:59', 11, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (69, 'zhangruixian@gmail.com', '2023-10-31 21:06:00', 12, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (70, 'zhangruixian@gmail.com', '2023-10-31 21:06:00', 13, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (71, 'zhangruixian@gmail.com', '2023-10-31 21:06:00', 14, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (72, 'zhangruixian@gmail.com', '2023-10-31 21:06:00', 15, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (73, 'zhangruixian@gmail.com', '2023-10-31 21:06:00', 16, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (74, 'zhangruixian@gmail.com', '2023-10-31 21:06:00', 17, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (75, 'zhangruixian@gmail.com', '2023-10-31 21:06:00', 18, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (76, 'zhangruixian@gmail.com', '2023-10-31 21:06:01', 19, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (77, 'zhangruixian@gmail.com', '2023-10-31 21:06:28', 20, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (78, 'zhangruixian@gmail.com', '2023-10-31 21:06:28', 21, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (79, 'zhangruixian@gmail.com', '2023-10-31 21:06:28', 22, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (80, 'zhangruixian@gmail.com', '2023-10-31 21:06:28', 23, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (81, 'zhangruixian@gmail.com', '2023-10-31 21:06:28', 24, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (82, 'zhangruixian@gmail.com', '2023-10-31 21:06:28', 25, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (83, 'zhangruixian@gmail.com', '2023-10-31 21:06:29', 26, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (84, 'zhangruixian@gmail.com', '2023-10-31 21:06:29', 27, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (85, 'zhangruixian@gmail.com', '2023-10-31 21:06:29', 28, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (86, 'zhangruixian@gmail.com', '2023-10-31 21:06:29', 29, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (87, 'zhangruixian@gmail.com', '2023-10-31 21:06:29', 30, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (88, 'zhangruixian@gmail.com', '2023-10-31 21:06:29', 31, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (89, 'zhangruixian@gmail.com', '2023-10-31 21:06:30', 32, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (90, 'zhangruixian@gmail.com', '2023-10-31 21:06:30', 33, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (91, 'zhangruixian@gmail.com', '2023-10-31 21:06:30', 34, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (92, 'zhangruixian@gmail.com', '2023-10-31 21:06:30', 35, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (93, 'zhangruixian@gmail.com', '2023-10-31 21:06:30', 36, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (94, 'zhangruixian@gmail.com', '2023-10-31 21:06:30', 37, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (95, 'zhangruixian@gmail.com', '2023-10-31 21:06:30', 38, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (96, 'zhangruixian@gmail.com', '2023-10-31 21:06:31', 39, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (97, 'zhangruixian@gmail.com', '2023-10-31 21:09:01', 5, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (98, 'zhangruixian@gmail.com', '2023-10-31 21:09:01', 6, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (99, 'zhangruixian@gmail.com', '2023-10-31 21:09:01', 7, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (100, 'zhangruixian@gmail.com', '2023-10-31 21:09:01', 8, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (101, 'zhangruixian@gmail.com', '2023-10-31 21:09:01', 9, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (102, 'zhangruixian@gmail.com', '2023-10-31 21:09:02', 10, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (103, 'zhangruixian@gmail.com', '2023-10-31 21:09:02', 11, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (104, 'zhangruixian@gmail.com', '2023-10-31 21:09:02', 12, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (105, 'zhangruixian@gmail.com', '2023-10-31 21:09:02', 13, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (106, 'zhangruixian@gmail.com', '2023-10-31 21:09:02', 14, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (107, 'zhangruixian@gmail.com', '2023-10-31 21:09:02', 15, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (108, 'zhangruixian@gmail.com', '2023-10-31 21:09:03', 16, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (109, 'zhangruixian@gmail.com', '2023-10-31 21:09:03', 17, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (110, 'zhangruixian@gmail.com', '2023-10-31 21:09:03', 18, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (111, 'zhangruixian@gmail.com', '2023-10-31 21:09:03', 19, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (112, 'zhangruixian@gmail.com', '2023-10-31 21:09:03', 20, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (113, 'zhangruixian@gmail.com', '2023-10-31 21:09:03', 21, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (114, 'zhangruixian@gmail.com', '2023-10-31 21:09:03', 22, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (115, 'zhangruixian@gmail.com', '2023-10-31 21:09:04', 23, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (116, 'zhangruixian@gmail.com', '2023-10-31 21:09:04', 24, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (117, 'zhangruixian@gmail.com', '2023-10-31 21:09:26', 25, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (118, 'zhangruixian@gmail.com', '2023-10-31 21:09:26', 26, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (119, 'zhangruixian@gmail.com', '2023-10-31 21:09:26', 27, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (120, 'zhangruixian@gmail.com', '2023-10-31 21:09:26', 28, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (121, 'zhangruixian@gmail.com', '2023-10-31 21:09:26', 29, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (122, 'zhangruixian@gmail.com', '2023-10-31 21:09:26', 30, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (123, 'zhangruixian@gmail.com', '2023-10-31 21:09:27', 31, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (124, 'zhangruixian@gmail.com', '2023-10-31 21:09:27', 32, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (125, 'zhangruixian@gmail.com', '2023-10-31 21:09:27', 33, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (126, 'zhangruixian@gmail.com', '2023-10-31 21:09:27', 34, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (127, 'zhangruixian@gmail.com', '2023-10-31 21:09:27', 35, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (128, 'zhangruixian@gmail.com', '2023-10-31 21:09:27', 36, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (129, 'zhangruixian@gmail.com', '2023-10-31 21:09:28', 37, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (130, 'zhangruixian@gmail.com', '2023-10-31 21:09:28', 38, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (131, 'zhangruixian@gmail.com', '2023-10-31 21:09:28', 39, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (132, 'zhangruixian@gmail.com', '2023-10-31 21:09:28', 40, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (133, 'zhangruixian@gmail.com', '2023-10-31 21:09:28', 41, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (134, 'zhangruixian@gmail.com', '2023-10-31 21:09:28', 42, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (135, 'zhangruixian@gmail.com', '2023-10-31 21:09:29', 43, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (136, 'zhangruixian@gmail.com', '2023-10-31 21:09:29', 44, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (137, 'renyuqing@gmail.com', '2023-11-01 00:53:21', 45, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (138, 'renyuqing@gmail.com', '2023-11-01 00:53:41', 45, 'Delete bike id is: 45');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (139, 'renyuqing@gmail.com', '2023-11-01 01:02:26', 45, 'Add a new bike');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (140, 'renyuqing@gmail.com', '2023-11-01 01:02:41', 45, 'Delete bike id is: 45');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (141, 'renyuqing@gmail.com', '2023-11-01 01:05:25', 4, 'change new battery');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (142, 'renyuqing@gmail.com', '2023-11-01 11:20:07', 14, 'Fixing bike: 14');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (143, 'renyuqing@gmail.com', '2023-11-01 11:24:06', 14, 'Fixing bike: 14');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (144, 'renyuqing@gmail.com', '2023-11-01 11:25:39', 33, 'Fixing bike: 33');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (145, 'renyuqing@gmail.com', '2023-11-01 11:25:58', 33, 'Fixing bike is done: 33');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (146, 'renyuqing@gmail.com', '2023-11-01 11:41:49', 33, 'Fixing bike: 33');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (147, 'renyuqing@gmail.com', '2023-11-01 11:42:16', 33, 'Fixing bike is done: 33');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (148, 'renyuqing@gmail.com', '2023-11-01 14:19:41', 33, 'Fixing bike: 33');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (149, 'renyuqing@gmail.com', '2023-11-01 14:19:52', 33, 'Fixing bike is done: 33');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (150, 'renyuqing@gmail.com', '2023-11-01 14:20:03', 1, 'Fixing bike: 1');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (151, 'renyuqing@gmail.com', '2023-11-01 14:20:11', 1, 'Fixing bike is done: 1');
INSERT INTO `Records` (`recordID`, `operator`, `date`, `bikeID`, `status`) VALUES (152, 'renyuqing@gmail.com', '2023-11-01 14:30:07', 1, 'Fixing bike: 1');
COMMIT;

-- ----------------------------
-- Table structure for Report
-- ----------------------------
DROP TABLE IF EXISTS `Report`;
CREATE TABLE `Report` (
  `reportID` int NOT NULL AUTO_INCREMENT COMMENT '报告ID',
  `fromID` int NOT NULL COMMENT '报告人ID',
  `message` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL COMMENT '正文',
  `startTime` datetime NOT NULL COMMENT '时间',
  `endTime` datetime DEFAULT NULL COMMENT '结束时间',
  `status` tinyint(1) NOT NULL COMMENT '报告状态',
  `authen` tinyint(1) NOT NULL COMMENT '报告人类型',
  PRIMARY KEY (`reportID`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of Report
-- ----------------------------
BEGIN;
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (1, 1, 'The 1 bike is broken', '2023-10-18 14:50:45', '2023-10-19 07:51:42', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (2, 1, 'The id of bike 2 is broken', '2023-10-19 07:42:45', '2023-10-19 07:52:18', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (3, 1, 'The id of bike 2 is broken', '2023-10-19 07:46:56', '2023-10-19 07:52:21', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (4, 1, 'Update1j', '2023-10-19 08:06:23', '2023-10-19 07:57:54', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (5, 1, 'The Bike needs to fix, id is : 1', '2023-10-22 10:38:19', '2023-10-22 11:02:49', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (6, 1, 'The Bike needs to fix, id is : 1', '2023-10-22 11:06:01', '2023-10-22 11:06:01', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (7, 2, 'The Bike needs to fix, id is : 2', '2023-10-22 22:46:21', '2023-10-22 22:46:21', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (8, 2, 'The Bike needs to fix, id is : 1', '2023-10-22 22:47:30', '2023-10-22 22:48:10', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (9, 2, 'The Bike needs to fix, id is : 2', '2023-10-22 22:50:35', '2023-10-22 22:50:55', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (10, 2, 'The Bike needs to fix, id is : 1', '2023-10-22 22:52:52', '2023-10-22 22:53:12', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (11, 2, 'The Bike needs to fix, id is : 3', '2023-10-22 22:55:48', '2023-10-22 22:55:58', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (12, 2, 'The Bike needs to fix, id is : 1', '2023-10-22 22:56:40', '2023-10-22 22:56:50', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (13, 1, 'The Bike needs to fix, id is : 2', '2023-10-28 11:55:28', '2023-10-28 11:58:21', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (14, 5, 'The Bike needs to fix, id is : 33', '2023-11-01 11:17:24', '2023-11-01 11:25:58', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (15, 5, 'The Bike needs to fix, id is : 33', '2023-11-01 11:38:59', '2023-11-01 11:42:16', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (16, 6, 'The Bike needs to fix, id is : 33', '2023-11-01 12:27:39', '2023-11-01 14:19:52', 1, 0);
INSERT INTO `Report` (`reportID`, `fromID`, `message`, `startTime`, `endTime`, `status`, `authen`) VALUES (17, 6, 'The Bike needs to fix, id is : 1', '2023-11-01 12:39:57', '2023-11-01 14:20:11', 1, 0);
COMMIT;

-- ----------------------------
-- Table structure for Vehicle
-- ----------------------------
DROP TABLE IF EXISTS `Vehicle`;
CREATE TABLE `Vehicle` (
  `vehicleID` int NOT NULL AUTO_INCREMENT COMMENT '车ID',
  `types` varchar(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '车类型',
  `price` double(10,3) NOT NULL COMMENT '价格',
  `batteryStatus` double(8,2) NOT NULL COMMENT '电池电量',
  `locations` int DEFAULT NULL COMMENT '位置',
  `status` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '车状态',
  `isRented` tinyint(1) NOT NULL COMMENT '租用状态',
  `isLocked` tinyint(1) NOT NULL COMMENT '上锁状态',
  `renter` int DEFAULT NULL COMMENT '租用人ID',
  PRIMARY KEY (`vehicleID`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of Vehicle
-- ----------------------------
BEGIN;
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (1, 'E-bike', 0.020, 99.95, 3, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (2, 'E-bike', 0.020, 100.00, 3, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (3, 'E-bike', 0.020, 100.00, 3, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (4, 'E-bike', 0.030, 100.00, 2, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (5, 'E-bike', 0.020, 100.00, 6, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (6, 'E-bike', 0.020, 100.00, 5, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (7, 'E-bike', 0.020, 100.00, 6, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (8, 'E-bike', 0.020, 100.00, 5, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (9, 'E-bike', 0.020, 99.88, 8, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (10, 'E-bike', 0.020, 99.70, 2, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (11, 'E-bike', 0.020, 99.82, 2, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (12, 'E-bike', 0.020, 100.00, 5, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (13, 'E-bike', 0.020, 100.00, 8, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (14, 'E-bike', 0.020, 100.00, 2, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (15, 'E-bike', 0.020, 100.00, 1, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (16, 'E-bike', 0.020, 100.00, 6, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (17, 'E-bike', 0.020, 100.00, 8, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (18, 'E-bike', 0.020, 100.00, 8, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (19, 'E-bike', 0.020, 100.00, 6, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (20, 'E-bike', 0.020, 100.00, 4, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (21, 'E-bike', 0.020, 100.00, 2, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (22, 'E-bike', 0.020, 100.00, 2, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (23, 'E-bike', 0.020, 100.00, 4, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (24, 'E-bike', 0.020, 100.00, 7, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (25, 'bike', 0.005, 0.00, 5, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (26, 'bike', 0.005, 0.00, 8, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (27, 'bike', 0.005, 0.00, 7, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (28, 'bike', 0.005, 0.00, 6, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (29, 'bike', 0.005, 0.00, 7, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (30, 'bike', 0.005, 0.00, 2, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (31, 'bike', 0.005, 0.00, 2, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (32, 'bike', 0.005, 0.00, 5, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (33, 'bike', 0.005, 0.00, 1, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (34, 'bike', 0.005, 0.00, 3, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (35, 'bike', 0.005, 0.00, 2, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (36, 'bike', 0.005, 0.00, 8, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (37, 'bike', 0.005, 0.00, 3, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (38, 'bike', 0.005, 0.00, 8, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (39, 'bike', 0.005, 0.00, 1, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (40, 'bike', 0.005, 0.00, 3, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (41, 'bike', 0.005, 0.00, 6, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (42, 'bike', 0.005, 0.00, 1, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (43, 'bike', 0.005, 0.00, 2, 'normal', 0, 0, NULL);
INSERT INTO `Vehicle` (`vehicleID`, `types`, `price`, `batteryStatus`, `locations`, `status`, `isRented`, `isLocked`, `renter`) VALUES (44, 'bike', 0.005, 0.00, 8, 'normal', 0, 0, NULL);
COMMIT;

-- ----------------------------
-- Table structure for VehicleStop
-- ----------------------------
DROP TABLE IF EXISTS `VehicleStop`;
CREATE TABLE `VehicleStop` (
  `locationID` int NOT NULL COMMENT '站点ID',
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '站点名称',
  `axis` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '位置',
  `maxCapacity` int NOT NULL COMMENT '最大容量',
  `currentCapacity` int DEFAULT NULL COMMENT '当前可用数目',
  PRIMARY KEY (`locationID`,`axis`) USING BTREE,
  UNIQUE KEY `axis` (`axis`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of VehicleStop
-- ----------------------------
BEGIN;
INSERT INTO `VehicleStop` (`locationID`, `name`, `axis`, `maxCapacity`, `currentCapacity`) VALUES (1, 'University of Glasgow Station 01', '(55.872,-4.289125)', 30, 4);
INSERT INTO `VehicleStop` (`locationID`, `name`, `axis`, `maxCapacity`, `currentCapacity`) VALUES (2, 'Glasgow Queen Station', '(55.86321958869664,-4.249372089102646)', 30, 10);
INSERT INTO `VehicleStop` (`locationID`, `name`, `axis`, `maxCapacity`, `currentCapacity`) VALUES (3, 'Victoria Park Pond Station', '(55.875433101741166,-4.331679589334157)', 20, 6);
INSERT INTO `VehicleStop` (`locationID`, `name`, `axis`, `maxCapacity`, `currentCapacity`) VALUES (4, 'University of Glasgow Station 02', '(55.87355614086009,-4.287083361235061)', 50, 2);
INSERT INTO `VehicleStop` (`locationID`, `name`, `axis`, `maxCapacity`, `currentCapacity`) VALUES (5, 'The Glasgow School of Art Station', '(55.866621088929676,-4.263660691297553)', 30, 5);
INSERT INTO `VehicleStop` (`locationID`, `name`, `axis`, `maxCapacity`, `currentCapacity`) VALUES (6, 'The Glasgow Gallery Station', '(55.86501019006313,-4.2623358477103235)', 30, 6);
INSERT INTO `VehicleStop` (`locationID`, `name`, `axis`, `maxCapacity`, `currentCapacity`) VALUES (7, 'Glasgow Central Station', '(55.85939152634621,-4.258117502247578)', 50, 3);
INSERT INTO `VehicleStop` (`locationID`, `name`, `axis`, `maxCapacity`, `currentCapacity`) VALUES (8, 'Glasgow Caledonian University Station', '(55.867452673787,-4.247292114287026)', 20, 8);
COMMIT;

-- ----------------------------
-- Triggers structure for table Vehicle
-- ----------------------------
DROP TRIGGER IF EXISTS `currentCapacity_U`;
delimiter ;;
CREATE TRIGGER `currentCapacity_U` AFTER UPDATE ON `Vehicle` FOR EACH ROW BEGIN
	UPDATE VehicleStop
	SET currentCapacity = (
		SELECT COUNT(*)
		FROM Vehicle
		WHERE locations = NEW.locations AND isLocked = 0 ANd isRented = 0
	)
	WHERE locationID = NEW.locations;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table Vehicle
-- ----------------------------
DROP TRIGGER IF EXISTS `currentCapacity_I`;
delimiter ;;
CREATE TRIGGER `currentCapacity_I` AFTER INSERT ON `Vehicle` FOR EACH ROW BEGIN
    UPDATE VehicleStop
    SET currentCapacity = (
        SELECT COUNT(*)
        FROM Vehicle
        WHERE locations = NEW.locations AND isLocked = 0 AND isRented = 0
    )
    WHERE locationID = NEW.locations;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table Vehicle
-- ----------------------------
DROP TRIGGER IF EXISTS `currentCapacity_D`;
delimiter ;;
CREATE TRIGGER `currentCapacity_D` AFTER DELETE ON `Vehicle` FOR EACH ROW BEGIN
    UPDATE VehicleStop
    SET currentCapacity = (
        SELECT COUNT(*)
        FROM Vehicle
        WHERE locations = OLD.locations AND isLocked = 0 AND isRented = 0
    )
    WHERE locationID = OLD.locations;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
