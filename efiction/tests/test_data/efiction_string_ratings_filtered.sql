# ************************************************************
# EFICTION FILTERED WITH STRING RATINGS IN STORIES TABLE
# ************************************************************

CREATE DATABASE efictiontest_string_ratings_test_step_original_efiction_edited;
USE efictiontest_string_ratings_test_step_original_efiction_edited;

DROP TABLE IF EXISTS `authors`;

CREATE TABLE `authors`
(
    `uid`          int(11)      NOT NULL AUTO_INCREMENT,
    `penname`      varchar(200) NOT NULL DEFAULT '',
    `realname`     varchar(200) NOT NULL DEFAULT '',
    `email`        varchar(200) NOT NULL DEFAULT '',
    `website`      varchar(200) NOT NULL DEFAULT '',
    `bio`          text,
    `image`        varchar(200) NOT NULL DEFAULT '',
    `date`         datetime     DEFAULT NULL,
    `admincreated` char(1)      NOT NULL DEFAULT '0',
    `password`     varchar(40)  NOT NULL DEFAULT '0',
    PRIMARY KEY (`uid`),
    KEY `penname` (`penname`),
    KEY `admincreated` (`admincreated`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;
INSERT INTO `authors` (`uid`, `penname`, `realname`, `email`, `website`, `bio`, `image`, `date`,
                                  `admincreated`, `password`)
VALUES (1, 'Author1', 'Author1', 'A1@example.com', '', '', '', '2006-01-06 01:02:13', '0', 'xfghtu');

DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories`
(
    `catid`        int(11)      NOT NULL AUTO_INCREMENT,
    `parentcatid`  int(11)      NOT NULL DEFAULT '-1',
    `category`     varchar(60)  NOT NULL DEFAULT '',
    `description`  text         NOT NULL,
    `image`        varchar(100) NOT NULL DEFAULT '',
    `locked`       char(1)      NOT NULL DEFAULT '0',
    `leveldown`    tinyint(4)   NOT NULL DEFAULT '0',
    `displayorder` int(11)      NOT NULL DEFAULT '0',
    `numitems`     int(11)      NOT NULL DEFAULT '0',
    PRIMARY KEY (`catid`),
    KEY `byparent` (`parentcatid`, `displayorder`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;
INSERT INTO `categories` (`catid`, `parentcatid`, `category`, `description`, `image`, `locked`, `leveldown`,
                                     `displayorder`, `numitems`)
VALUES (1, -1, 'General', '', 'categoryfp.gif', '0', 0, 1, 1310);

DROP TABLE IF EXISTS `chapters`;
CREATE TABLE `chapters`
(
    `chapid`    int(11)      NOT NULL AUTO_INCREMENT,
    `title`     varchar(250) NOT NULL DEFAULT '',
    `inorder`   int(11)      NOT NULL DEFAULT '0',
    `notes`     text         NOT NULL,
    `storytext` text,
    `endnotes`  text,
    `validated` char(1)      NOT NULL DEFAULT '0',
    `wordcount` int(11)      NOT NULL DEFAULT '0',
    `rating`    tinyint(4)   NOT NULL DEFAULT '0',
    `reviews`   smallint(6)  NOT NULL DEFAULT '0',
    `sid`       int(11)      NOT NULL DEFAULT '0',
    `uid`       int(11)      NOT NULL DEFAULT '0',
    `count`     int(11)      NOT NULL DEFAULT '0',
    PRIMARY KEY (`chapid`),
    KEY `sid` (`sid`),
    KEY `uid` (`uid`),
    KEY `inorder` (`inorder`),
    KEY `title` (`title`),
    KEY `validated` (`validated`),
    KEY `forstoryblock` (`sid`, `validated`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;
INSERT INTO `chapters` (`chapid`, `title`, `inorder`, `notes`, `storytext`, `endnotes`, `validated`,
                                   `wordcount`, `rating`, `reviews`, `sid`, `uid`, `count`)
VALUES (1, 'Chapter 1', 1, 'Bacon-related notes.', '', NULL, '1', 3992, 0, 2, 1, 2, 2872);


DROP TABLE IF EXISTS `characters`;
CREATE TABLE `characters`
(
    `charid`   int(11)      NOT NULL AUTO_INCREMENT,
    `catid`    int(11)      NOT NULL DEFAULT '0',
    `charname` varchar(60)  NOT NULL DEFAULT '',
    `bio`      text         NOT NULL,
    `image`    varchar(200) NOT NULL DEFAULT '',
    PRIMARY KEY (`charid`),
    KEY `catid` (`catid`),
    KEY `charname` (`charname`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;
INSERT INTO `characters` (`charid`, `catid`, `charname`, `bio`, `image`)
VALUES (1, -1, 'Bill O\'Connell', '', '');

DROP TABLE IF EXISTS `classes`;
CREATE TABLE `classes`
(
    `class_id`   int(11)      NOT NULL AUTO_INCREMENT,
    `class_type` int(11)      NOT NULL DEFAULT '0',
    `class_name` varchar(100) NOT NULL DEFAULT '',
    PRIMARY KEY (`class_id`),
    KEY `byname` (`class_type`, `class_name`, `class_id`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;
INSERT INTO `classes` (`class_id`, `class_type`, `class_name`)
VALUES (1, 1, 'Action/Adventure');

DROP TABLE IF EXISTS `classtypes`;

CREATE TABLE `classtypes`
(
    `classtype_id`    int(11)     NOT NULL AUTO_INCREMENT,
    `classtype_name`  varchar(50) NOT NULL DEFAULT '',
    `classtype_title` varchar(50) NOT NULL DEFAULT '',
    PRIMARY KEY (`classtype_id`),
    UNIQUE KEY `classtype_name` (`classtype_name`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;
INSERT INTO `classtypes` (`classtype_id`, `classtype_name`, `classtype_title`)
VALUES (1, 'genres', 'Genres'),
       (2, 'warnings', 'Warnings');

DROP TABLE IF EXISTS `ratings`;
CREATE TABLE `ratings`
(
    `rid`           int(11)     NOT NULL AUTO_INCREMENT,
    `rating`        varchar(60) NOT NULL DEFAULT '',
    `ratingwarning` char(1)     NOT NULL DEFAULT '0',
    `warningtext`   text        NOT NULL,
    PRIMARY KEY (`rid`),
    KEY `rating` (`rating`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;
INSERT INTO `ratings` (`rid`, `rating`, `ratingwarning`, `warningtext`)
VALUES (1, 'All Ages', '', ''),
       (2, 'Pre-Teen', '', ''),
       (3, 'Teen', '', ''),
       (4, 'Mature', '', ''),
       (5, 'Adult', '', '');


DROP TABLE IF EXISTS `stories`;
CREATE TABLE `stories`
(
    `sid`        int(11)      NOT NULL AUTO_INCREMENT,
    `title`      varchar(200) NOT NULL DEFAULT '',
    `summary`    text,
    `storynotes` text,
    `catid`      varchar(100) NOT NULL DEFAULT '0',
    `classes`    varchar(200)          DEFAULT NULL,
    `charid`     varchar(250) NOT NULL DEFAULT '0',
    `rid`        varchar(25)  NOT NULL DEFAULT '0',
    `date`       datetime     DEFAULT NULL,
    `updated`    datetime     DEFAULT NULL,
    `uid`        int(11)      NOT NULL DEFAULT '0',
    `coauthors`  varchar(200)          DEFAULT NULL,
    `featured`   char(1)      NOT NULL DEFAULT '0',
    `validated`  char(1)      NOT NULL DEFAULT '0',
    `completed`  char(1)      NOT NULL DEFAULT '0',
    `rr`         char(1)      NOT NULL DEFAULT '0',
    `wordcount`  int(11)      NOT NULL DEFAULT '0',
    `rating`     tinyint(4)   NOT NULL DEFAULT '0',
    `reviews`    smallint(6)  NOT NULL DEFAULT '0',
    `count`      int(11)      NOT NULL DEFAULT '0',
    `challenges` varchar(200) NOT NULL DEFAULT '0',
    PRIMARY KEY (`sid`),
    KEY `title` (`title`),
    KEY `catid` (`catid`),
    KEY `charid` (`charid`),
    KEY `rid` (`rid`),
    KEY `uid` (`uid`),
    KEY `featured` (`featured`),
    KEY `completed` (`completed`),
    KEY `rr` (`rr`),
    KEY `challenges` (`challenges`),
    KEY `validateduid` (`validated`, `uid`),
    KEY `recent` (`updated`, `validated`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;
INSERT INTO `stories` (`sid`, `title`, `summary`, `storynotes`, `catid`, `classes`, `charid`, `rid`, `date`,
                                  `updated`, `uid`, `coauthors`, `featured`, `validated`, `completed`, `rr`,
                                  `wordcount`, `rating`, `reviews`, `count`, `challenges`)
VALUES (1, 'Bacon ipsum', '&nbsp;<p> &nbsp;</p>Meat-related text.', NULL, '1', '3,10,16,26', '2,1', 'Mature',
        '2006-02-09 22:21:35', '2006-02-09 22:21:35', 2, '3,5', '', '1', '1', '', 3992, 0, 2, 2872, '0'),
       (3, 'Lorem ipsum', 'Short, and no tricky characters.', NULL, '6', '3,10,12,15,25', '2,1,3,4', 'Mature',
        '2006-03-04 13:00:45', '2006-03-04 13:00:45', 4, NULL, '', '1', '1', '', 8482, 0, 7, 4615, '0');
