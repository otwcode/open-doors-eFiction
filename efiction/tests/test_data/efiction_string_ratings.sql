# ************************************************************
# EFICTION ORIGINAL WITH STRING RATINGS IN STORIES TABLE
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT = @@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS = @@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION = @@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS = 0 */;
/*!40101 SET @OLD_SQL_MODE = @@SQL_MODE, SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES = @@SQL_NOTES, SQL_NOTES = 0 */;


CREATE DATABASE test_efiction_original_database_name_we_dont_want;
USE test_efiction_original_database_name_we_dont_want;

# Dump of table fanfiction_authors
# ------------------------------------------------------------

DROP TABLE IF EXISTS `fanfiction_authors`;

CREATE TABLE `fanfiction_authors`
(
    `uid`          int(11)      NOT NULL AUTO_INCREMENT,
    `penname`      varchar(200) NOT NULL DEFAULT '',
    `realname`     varchar(200) NOT NULL DEFAULT '',
    `email`        varchar(200) NOT NULL DEFAULT '',
    `website`      varchar(200) NOT NULL DEFAULT '',
    `bio`          text,
    `image`        varchar(200) NOT NULL DEFAULT '',
    `date`         datetime     NOT NULL DEFAULT '0000-00-00 00:00:00',
    `admincreated` char(1)      NOT NULL DEFAULT '0',
    `password`     varchar(40)  NOT NULL DEFAULT '0',
    PRIMARY KEY (`uid`),
    KEY `penname` (`penname`),
    KEY `admincreated` (`admincreated`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;

LOCK TABLES `fanfiction_authors` WRITE;
/*!40000 ALTER TABLE `fanfiction_authors`
    DISABLE KEYS */;

INSERT INTO `fanfiction_authors` (`uid`, `penname`, `realname`, `email`, `website`, `bio`, `image`, `date`,
                                  `admincreated`, `password`)
VALUES (1, 'Author1', 'Author1', 'A1@example.com', '', '', '', '2006-01-06 01:02:13', '0', 'xfghtu');

/*!40000 ALTER TABLE `fanfiction_authors`
    ENABLE KEYS */;
UNLOCK TABLES;

# Dump of table fanfiction_categories
# ------------------------------------------------------------

DROP TABLE IF EXISTS `fanfiction_categories`;

CREATE TABLE `fanfiction_categories`
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

LOCK TABLES `fanfiction_categories` WRITE;
/*!40000 ALTER TABLE `fanfiction_categories`
    DISABLE KEYS */;

INSERT INTO `fanfiction_categories` (`catid`, `parentcatid`, `category`, `description`, `image`, `locked`, `leveldown`,
                                     `displayorder`, `numitems`)
VALUES (1, -1, 'General', '', 'categoryfp.gif', '0', 0, 1, 1310);

/*!40000 ALTER TABLE `fanfiction_categories`
    ENABLE KEYS */;
UNLOCK TABLES;

# Dump of table fanfiction_chapters
# ------------------------------------------------------------

DROP TABLE IF EXISTS `fanfiction_chapters`;

CREATE TABLE `fanfiction_chapters`
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

LOCK TABLES `fanfiction_chapters` WRITE;
/*!40000 ALTER TABLE `fanfiction_chapters`
    DISABLE KEYS */;

INSERT INTO `fanfiction_chapters` (`chapid`, `title`, `inorder`, `notes`, `storytext`, `endnotes`, `validated`,
                                   `wordcount`, `rating`, `reviews`, `sid`, `uid`, `count`)
VALUES (1, 'Chapter 1', 1, 'Bacon-related notes.', '', NULL, '1', 3992, 0, 2, 1, 2, 2872);

/*!40000 ALTER TABLE `fanfiction_chapters`
    ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table fanfiction_characters
# ------------------------------------------------------------

DROP TABLE IF EXISTS `fanfiction_characters`;

CREATE TABLE `fanfiction_characters`
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

LOCK TABLES `fanfiction_characters` WRITE;
/*!40000 ALTER TABLE `fanfiction_characters`
    DISABLE KEYS */;

INSERT INTO `fanfiction_characters` (`charid`, `catid`, `charname`, `bio`, `image`)
VALUES (1, -1, 'Bill O\'Connell', '', '');

/*!40000 ALTER TABLE `fanfiction_characters`
    ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table fanfiction_classes
# ------------------------------------------------------------

DROP TABLE IF EXISTS `fanfiction_classes`;

CREATE TABLE `fanfiction_classes`
(
    `class_id`   int(11)      NOT NULL AUTO_INCREMENT,
    `class_type` int(11)      NOT NULL DEFAULT '0',
    `class_name` varchar(100) NOT NULL DEFAULT '',
    PRIMARY KEY (`class_id`),
    KEY `byname` (`class_type`, `class_name`, `class_id`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;

LOCK TABLES `fanfiction_classes` WRITE;
/*!40000 ALTER TABLE `fanfiction_classes`
    DISABLE KEYS */;

INSERT INTO `fanfiction_classes` (`class_id`, `class_type`, `class_name`)
VALUES (1, 1, 'Action/Adventure');

/*!40000 ALTER TABLE `fanfiction_classes`
    ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table fanfiction_classtypes
# ------------------------------------------------------------

DROP TABLE IF EXISTS `fanfiction_classtypes`;

CREATE TABLE `fanfiction_classtypes`
(
    `classtype_id`    int(11)     NOT NULL AUTO_INCREMENT,
    `classtype_name`  varchar(50) NOT NULL DEFAULT '',
    `classtype_title` varchar(50) NOT NULL DEFAULT '',
    PRIMARY KEY (`classtype_id`),
    UNIQUE KEY `classtype_name` (`classtype_name`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;

LOCK TABLES `fanfiction_classtypes` WRITE;
/*!40000 ALTER TABLE `fanfiction_classtypes`
    DISABLE KEYS */;

INSERT INTO `fanfiction_classtypes` (`classtype_id`, `classtype_name`, `classtype_title`)
VALUES (1, 'genres', 'Genres'),
       (2, 'warnings', 'Warnings');

/*!40000 ALTER TABLE `fanfiction_classtypes`
    ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table fanfiction_coauthors
# ------------------------------------------------------------
#
# DROP TABLE IF EXISTS `fanfiction_coauthors`;
#
# CREATE TABLE `fanfiction_coauthors`
# (
#     `sid` int(11) NOT NULL DEFAULT '0',
#     `uid` int(11) NOT NULL DEFAULT '0',
#     PRIMARY KEY (`sid`, `uid`)
# ) ENGINE = MyISAM
#   DEFAULT CHARSET = latin1;
#
# LOCK TABLES `fanfiction_coauthors` WRITE;
# /*!40000 ALTER TABLE `fanfiction_coauthors`
#     DISABLE KEYS */;
#
# INSERT INTO `fanfiction_coauthors` (`sid`, `uid`)
# VALUES (1, 5),
#        (108, 5);
#
# /*!40000 ALTER TABLE `fanfiction_coauthors`
#     ENABLE KEYS */;
# UNLOCK TABLES;


# Dump of table fanfiction_codeblocks
# ------------------------------------------------------------
#
# DROP TABLE IF EXISTS `fanfiction_codeblocks`;
#
# CREATE TABLE `fanfiction_codeblocks`
# (
#     `code_id`     int(11) NOT NULL AUTO_INCREMENT,
#     `code_text`   text    NOT NULL,
#     `code_type`   varchar(20) DEFAULT NULL,
#     `code_module` varchar(60) DEFAULT NULL,
#     PRIMARY KEY (`code_id`),
#     KEY `code_type` (`code_type`)
# ) ENGINE = MyISAM
#   DEFAULT CHARSET = latin1;
#


# Dump of table fanfiction_comments
# ------------------------------------------------------------
#
# DROP TABLE IF EXISTS `fanfiction_comments`;
#
# CREATE TABLE `fanfiction_comments`
# (
#     `cid`     int(11)  NOT NULL AUTO_INCREMENT,
#     `nid`     int(11)  NOT NULL DEFAULT '0',
#     `uid`     int(11)  NOT NULL DEFAULT '0',
#     `comment` text     NOT NULL,
#     `time`    datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
#     PRIMARY KEY (`cid`),
#     KEY `commentlist` (`nid`, `time`)
# ) ENGINE = MyISAM
#   DEFAULT CHARSET = latin1;
#
# LOCK TABLES `fanfiction_comments` WRITE;
# /*!40000 ALTER TABLE `fanfiction_comments`
#     DISABLE KEYS */;
#
# INSERT INTO `fanfiction_comments` (`cid`, `nid`, `uid`, `comment`, `time`)
# VALUES (1, 1, 3, 'The new archive is amazing :)', '2006-04-03 18:12:00'),
#        (2, 1, 305, 'The site looks *stupendous*!', '2006-04-05 18:37:36'),
#        (3, 1, 360, 'Looks great!  ', '2006-08-01 23:42:32');
#
# /*!40000 ALTER TABLE `fanfiction_comments`
#     ENABLE KEYS */;
# UNLOCK TABLES;


# Dump of table fanfiction_favorites
# ------------------------------------------------------------
#
# DROP TABLE IF EXISTS `fanfiction_favorites`;
#
# CREATE TABLE `fanfiction_favorites`
# (
#     `uid`      int(11) NOT NULL DEFAULT '0',
#     `item`     int(11) NOT NULL DEFAULT '0',
#     `type`     char(2) NOT NULL DEFAULT '',
#     `comments` text    NOT NULL,
#     UNIQUE KEY `byitem` (`item`, `type`, `uid`),
#     UNIQUE KEY `byuid` (`uid`, `type`, `item`)
# ) ENGINE = MyISAM
#   DEFAULT CHARSET = latin1;
#
# LOCK TABLES `fanfiction_favorites` WRITE;
# /*!40000 ALTER TABLE `fanfiction_favorites`
#     DISABLE KEYS */;
#
# INSERT INTO `fanfiction_favorites` (`uid`, `item`, `type`, `comments`)
# VALUES (1, 1, 'ST', ''),
#        (0, 2559, 'ST', ''),
#        (0, 2277, 'ST', ''),
#        (0, 1386, 'ST', ''),
#        (0, 2331, 'ST', ''),
#        (0, 2540, 'ST', ''),
#        (0, 71, 'ST', ''),
#        (0, 72, 'ST', ''),
#        (0, 73, 'ST', ''),
#        (0, 2084, 'ST', ''),
#        (0, 2, 'AU', ''),
#        (0, 24, 'AU', ''),
#        (2, 2694, 'ST', ''),
#        (2, 1961, 'ST', ''),
#        (2, 3176, 'ST', ''),
#        (2, 1881, 'ST', ''),
#        (2, 248, 'ST', ''),
#        (2, 342, 'ST', ''),
#        (2, 2934, 'ST', ''),
#        (2, 322, 'ST', ''),
#        (2, 375, 'ST', ''),
#        (2, 3525, 'ST', ''),
#        (2, 2411, 'ST', ''),
#        (2, 2414, 'ST', ''),
#        (2, 2645, 'ST', ''),
#        (2, 308, 'ST', ''),
#        (2, 3540, 'ST', ''),
#        (2, 1090, 'ST', ''),
#        (2, 2442, 'ST', ''),
#        (2, 2034, 'ST', ''),
#        (2, 2697, 'ST', ''),
#        (2, 3472, 'ST', ''),
#        (2, 2868, 'ST', ''),
#        (2, 3161, 'ST', ''),
#        (2, 2795, 'ST', ''),
#        (2, 2126, 'ST', ''),
#        (2, 3308, 'ST', ''),
#        (2, 236, 'ST', ''),
#        (2, 2679, 'ST', ''),
#        (2, 2791, 'ST', ''),
#        (2, 746, 'ST', ''),
#        (2, 2327, 'ST', ''),
#        (2, 800, 'ST', ''),
#        (2, 3491, 'ST', ''),
#        (2, 2984, 'ST', ''),
#        (2, 2285, 'ST', ''),
#        (2, 588, 'ST', ''),
#        (2, 3209, 'ST', ''),
#        (2, 3467, 'ST', ''),
#        (2, 1926, 'ST', '');
#
# /*!40000 ALTER TABLE `fanfiction_favorites`
#     ENABLE KEYS */;
# UNLOCK TABLES;


# Dump of table fanfiction_inseries
# ------------------------------------------------------------
#
# DROP TABLE IF EXISTS `fanfiction_inseries`;
#
# CREATE TABLE `fanfiction_inseries`
# (
#     `seriesid`    int(11) NOT NULL DEFAULT '0',
#     `sid`         int(11) NOT NULL DEFAULT '0',
#     `subseriesid` int(11) NOT NULL DEFAULT '0',
#     `confirmed`   int(11) NOT NULL DEFAULT '0',
#     `inorder`     int(11) NOT NULL DEFAULT '0',
#     PRIMARY KEY (`sid`, `seriesid`, `subseriesid`),
#     KEY `seriesid` (`seriesid`, `inorder`)
# ) ENGINE = MyISAM
#   DEFAULT CHARSET = latin1;
#
# LOCK TABLES `fanfiction_inseries` WRITE;
# /*!40000 ALTER TABLE `fanfiction_inseries`
#     DISABLE KEYS */;
#
# INSERT INTO `fanfiction_inseries` (`seriesid`, `sid`, `subseriesid`, `confirmed`, `inorder`)
# VALUES (169, 108, 0, 1, 19),
#        (118, 838, 0, 1, 2),
#        (118, 835, 0, 1, 1),
#        (224, 3721, 0, 1, 5);
#
# /*!40000 ALTER TABLE `fanfiction_inseries`
#     ENABLE KEYS */;
# UNLOCK TABLES;


# Dump of table fanfiction_log
# ------------------------------------------------------------
#
# DROP TABLE IF EXISTS `fanfiction_log`;
#
# CREATE TABLE `fanfiction_log`
# (
#     `log_id`        int(11)    NOT NULL AUTO_INCREMENT,
#     `log_action`    varchar(255)        DEFAULT NULL,
#     `log_uid`       int(11)    NOT NULL,
#     `log_ip`        int(11) unsigned    DEFAULT NULL,
#     `log_timestamp` timestamp  NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#     `log_type`      varchar(2) NOT NULL,
#     PRIMARY KEY (`log_id`)
# ) ENGINE = MyISAM
#   DEFAULT CHARSET = latin1;
#


# Dump of table fanfiction_messages
# ------------------------------------------------------------
#
# DROP TABLE IF EXISTS `fanfiction_messages`;
#
# CREATE TABLE `fanfiction_messages`
# (
#     `message_id`    int(11)      NOT NULL AUTO_INCREMENT,
#     `message_name`  varchar(50)  NOT NULL DEFAULT '',
#     `message_title` varchar(200) NOT NULL DEFAULT '',
#     `message_text`  text         NOT NULL,
#     PRIMARY KEY (`message_id`),
#     KEY `message_name` (`message_name`)
# ) ENGINE = MyISAM
#   DEFAULT CHARSET = latin1;
#
# LOCK TABLES `fanfiction_messages` WRITE;
# /*!40000 ALTER TABLE `fanfiction_messages`
#     DISABLE KEYS */;
#
# INSERT INTO `fanfiction_messages` (`message_id`, `message_name`, `message_title`, `message_text`)
# VALUES (1, 'copyright', 'Copyright Footer',
#         '<div align=\"center\" style= \"font-size: .8em\">\r\nThis site is powered by <a href=\"http://efiction.org/index.php\">eFiction 3.5.3</a>. Skin design by Moderator.'),
#        (9, 'welcome', 'Welcome', 'Welcome to Efiction Test!'),
#        (13, 'rules', 'EFiction Submission Rules', ''),
#        (14, 'tos', 'Terms of Service', '');
#
# /*!40000 ALTER TABLE `fanfiction_messages`
#     ENABLE KEYS */;
# UNLOCK TABLES;


# Dump of table fanfiction_modules
# ------------------------------------------------------------
#
# DROP TABLE IF EXISTS `fanfiction_modules`;
#
# CREATE TABLE `fanfiction_modules`
# (
#     `id`      int(11)                                                     NOT NULL AUTO_INCREMENT,
#     `name`    varchar(100) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL DEFAULT 'Test Module',
#     `version` varchar(10) CHARACTER SET latin1 COLLATE latin1_general_ci  NOT NULL DEFAULT '1.0',
#     PRIMARY KEY (`id`),
#     KEY `name_version` (`name`, `version`)
# ) ENGINE = MyISAM
#   DEFAULT CHARSET = latin1;
#


# Dump of table fanfiction_news
# ------------------------------------------------------------
#
# DROP TABLE IF EXISTS `fanfiction_news`;
#
# CREATE TABLE `fanfiction_news`
# (
#     `nid`      int(11)      NOT NULL AUTO_INCREMENT,
#     `author`   varchar(60)  NOT NULL DEFAULT '',
#     `title`    varchar(255) NOT NULL DEFAULT '',
#     `story`    text         NOT NULL,
#     `time`     datetime              DEFAULT NULL,
#     `comments` int(11)      NOT NULL DEFAULT '0',
#     PRIMARY KEY (`nid`)
# ) ENGINE = MyISAM
#   DEFAULT CHARSET = latin1;
#
# LOCK TABLES `fanfiction_news` WRITE;
# /*!40000 ALTER TABLE `fanfiction_news`
#     DISABLE KEYS */;
#
# INSERT INTO `fanfiction_news` (`nid`, `author`, `title`, `story`, `time`, `comments`)
# VALUES (1, 'Moderator', 'New Archive Open for Business!', 'Welcome to the new Efiction Test archive!',
#         '2006-04-03 13:21:07', 3);
#
# /*!40000 ALTER TABLE `fanfiction_news`
#     ENABLE KEYS */;
# UNLOCK TABLES;


# Dump of table fanfiction_pagelinks
# ------------------------------------------------------------
#
# DROP TABLE IF EXISTS `fanfiction_pagelinks`;
#
# CREATE TABLE `fanfiction_pagelinks`
# (
#     `link_id`     int(11)      NOT NULL AUTO_INCREMENT,
#     `link_name`   varchar(50)  NOT NULL DEFAULT '',
#     `link_text`   varchar(100) NOT NULL DEFAULT '',
#     `link_key`    char(1)               DEFAULT NULL,
#     `link_url`    varchar(250) NOT NULL DEFAULT '',
#     `link_target` char(1)      NOT NULL DEFAULT '0',
#     `link_access` tinyint(4)   NOT NULL DEFAULT '0',
#     PRIMARY KEY (`link_id`),
#     KEY `link_name` (`link_name`)
# ) ENGINE = MyISAM
#   DEFAULT CHARSET = latin1;
#
# LOCK TABLES `fanfiction_pagelinks` WRITE;
# /*!40000 ALTER TABLE `fanfiction_pagelinks`
#     DISABLE KEYS */;
#
# INSERT INTO `fanfiction_pagelinks` (`link_id`, `link_name`, `link_text`, `link_key`, `link_url`, `link_target`,
#                                     `link_access`)
# VALUES (1, 'home', 'Home', NULL, 'index.php', '0', 0),
#        (9, 'authors', 'Authors', NULL, 'authors.php?list=authors', '0', 0),
#        (12, 'series', 'Series', NULL, 'browse.php?type=series', '0', 0),
#        (15, 'contactus', 'Contact Us', NULL, 'contact.php', '0', 0);
#
# /*!40000 ALTER TABLE `fanfiction_pagelinks`
#     ENABLE KEYS */;
# UNLOCK TABLES;


# Dump of table fanfiction_panels
# ------------------------------------------------------------
#
# DROP TABLE IF EXISTS `fanfiction_panels`;
#
# CREATE TABLE `fanfiction_panels`
# (
#     `panel_id`     int(11)      NOT NULL AUTO_INCREMENT,
#     `panel_name`   varchar(50)  NOT NULL DEFAULT 'unknown',
#     `panel_title`  varchar(100) NOT NULL DEFAULT 'Unnamed Panel',
#     `panel_url`    varchar(100)          DEFAULT NULL,
#     `panel_level`  tinyint(4)   NOT NULL DEFAULT '3',
#     `panel_order`  tinyint(4)   NOT NULL DEFAULT '0',
#     `panel_hidden` tinyint(1)   NOT NULL DEFAULT '0',
#     `panel_type`   varchar(20)  NOT NULL DEFAULT 'A',
#     PRIMARY KEY (`panel_id`),
#     KEY `panel_type` (`panel_type`, `panel_name`)
# ) ENGINE = MyISAM
#   DEFAULT CHARSET = latin1;
#
# LOCK TABLES `fanfiction_panels` WRITE;
# /*!40000 ALTER TABLE `fanfiction_panels`
#     DISABLE KEYS */;
#
# INSERT INTO `fanfiction_panels` (`panel_id`, `panel_name`, `panel_title`, `panel_url`, `panel_level`, `panel_order`,
#                                  `panel_hidden`, `panel_type`)
# VALUES (1, 'submitted', 'Submissions', '', 3, 5, 0, 'A'),
#        (2, 'versioncheck', 'Version Check', '', 3, 8, 0, 'A'),
#        (3, 'newstory', 'Add New Story', 'stories.php?action=newstory&admin=1', 3, 2, 0, 'A'),
#        (4, 'addseries', 'Add New Series', 'series.php?action=add', 3, 1, 0, 'A'),
#        (5, 'news', 'News', '', 3, 4, 0, 'A'),
#        (6, 'featured', 'Featured Stories', '', 3, 3, 0, 'A'),
#        (7, 'characters', 'Characters', '', 2, 2, 0, 'A'),
#        (8, 'ratings', 'Ratings', '', 2, 3, 0, 'A'),
#        (9, 'members', 'Members', '', 2, 5, 0, 'A'),
#        (10, 'mailusers', 'Mail Users', '', 2, 6, 0, 'A'),
#        (11, 'settings', 'Settings', '', 1, 2, 0, 'A'),
#        (12, 'blocks', 'Blocks', '', 1, 3, 0, 'A'),
#        (13, 'censor', 'Censor', '', 1, 0, 1, 'A'),
#        (14, 'admins', 'Admins', '', 1, 6, 0, 'A'),
#        (15, 'classifications', 'Classifications', '', 2, 4, 0, 'A'),
#        (16, 'categories', 'Categories', '', 2, 1, 0, 'A');
#
# /*!40000 ALTER TABLE `fanfiction_panels`
#     ENABLE KEYS */;
# UNLOCK TABLES;
#

# Dump of table fanfiction_ratings
# ------------------------------------------------------------

DROP TABLE IF EXISTS `fanfiction_ratings`;

CREATE TABLE `fanfiction_ratings`
(
    `rid`           int(11)     NOT NULL AUTO_INCREMENT,
    `rating`        varchar(60) NOT NULL DEFAULT '',
    `ratingwarning` char(1)     NOT NULL DEFAULT '0',
    `warningtext`   text        NOT NULL,
    PRIMARY KEY (`rid`),
    KEY `rating` (`rating`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;

LOCK TABLES `fanfiction_ratings` WRITE;
/*!40000 ALTER TABLE `fanfiction_ratings`
    DISABLE KEYS */;

INSERT INTO `fanfiction_ratings` (`rid`, `rating`, `ratingwarning`, `warningtext`)
VALUES (1, 'All Ages', '', ''),
       (2, 'Pre-Teen', '', ''),
       (3, 'Teen', '', ''),
       (4, 'Mature', '', ''),
       (5, 'Adult', '', '');

/*!40000 ALTER TABLE `fanfiction_ratings`
    ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table fanfiction_stories
# ------------------------------------------------------------

DROP TABLE IF EXISTS `fanfiction_stories`;

CREATE TABLE `fanfiction_stories`
(
    `sid`        int(11)      NOT NULL AUTO_INCREMENT,
    `title`      varchar(200) NOT NULL DEFAULT '',
    `summary`    text,
    `storynotes` text,
    `catid`      varchar(100) NOT NULL DEFAULT '0',
    `classes`    varchar(200)          DEFAULT NULL,
    `charid`     varchar(250) NOT NULL DEFAULT '0',
    `rid`        varchar(25)  NOT NULL DEFAULT '0',
    `date`       datetime     NOT NULL DEFAULT '0000-00-00 00:00:00',
    `updated`    datetime     NOT NULL DEFAULT '0000-00-00 00:00:00',
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

LOCK TABLES `fanfiction_stories` WRITE;
/*!40000 ALTER TABLE `fanfiction_stories`
    DISABLE KEYS */;

INSERT INTO `fanfiction_stories` (`sid`, `title`, `summary`, `storynotes`, `catid`, `classes`, `charid`, `rid`, `date`,
                                  `updated`, `uid`, `coauthors`, `featured`, `validated`, `completed`, `rr`,
                                  `wordcount`, `rating`, `reviews`, `count`, `challenges`)
VALUES (1, 'Bacon ipsum', '&nbsp;<p> &nbsp;</p>Meat-related text.', NULL, '1', '3,10,16,26', '2,1', 'Mature',
        '2006-02-09 22:21:35', '2006-02-09 22:21:35', 2, '3,5', '', '1', '1', '', 3992, 0, 2, 2872, '0'),
       (3, 'Lorem ipsum', 'Short, and no tricky characters.', NULL, '6', '3,10,12,15,25', '2,1,3,4', 'Mature',
        '2006-03-04 13:00:45', '2006-03-04 13:00:45', 4, NULL, '', '1', '1', '', 8482, 0, 7, 4615, '0');

/*!40000 ALTER TABLE `fanfiction_stories`
    ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES = @OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE = @OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT = @OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS = @OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION = @OLD_COLLATION_CONNECTION */;
