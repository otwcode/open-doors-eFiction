DROP DATABASE IF EXISTS `efictiontest_test_step_original_efiction_edited`;
CREATE DATABASE `efictiontest_test_step_original_efiction_edited`;
USE `efictiontest_test_step_original_efiction_edited`;

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
INSERT INTO `authors` (`uid`, `penname`, `realname`, `email`, `website`, `bio`, `image`, `date`, `admincreated`,
                       `password`)
VALUES (1, 'Author1', 'Author1', 'A1@example.com', '', '', '', '2006-01-06 01:02:13', '0', 'xfghtu'),
       (2, 'B Author 2', 'B Author 2', 'B2@example.com', '', '', 'bauthor2', '2006-02-09 01:37:24', '1', 'xfghtu'),
       (3, 'C Author 3', 'C Author 3', 'C3@example.com', 'http://example.com', 'An author bio with some text in it', '',
        '2006-02-16 22:58:02', '1', 'xfghtu'),
       (4, 'D Author 4', 'D Author 4', 'D4@example.com', '', '', '', '2006-02-15 23:00:00', '1', 'xfghtu'),
       (5, 'E Author 5', 'E Author 5', 'E5@example.com', 'www.example.com', '', 'eauthor5', '2006-02-16 23:00:00', '1',
        'xfghtu');
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
VALUES (1, -1, 'General', '', 'categoryfp.gif', '0', 0, 1, 1310),
       (2, -1, 'Slash Pairings', '', 'categoryfp.gif', '1', 0, 2, 2332),
       (3, -1, 'Het Pairings', '', 'categoryfp.gif', '1', 0, 3, 229),
       (5, -1, 'Threesomes, Moresomes', '', 'categoryfp.gif', '0', 0, 4, 29),
       (6, 2, 'Bill/Bob', '', 'category.gif', '0', 1, 7, 2227),
       (7, 2, 'Bill/Václav', '', 'category.gif', '0', 1, 8, 6),
       (8, 2, 'Bill/Olu', '', 'category.gif', '0', 1, 9, 1),
       (9, 2, 'Bill/Other Male', '', 'category.gif', '0', 1, 10, 17),
       (10, 2, 'Bob/Václav', '', 'category.gif', '0', 1, 11, 8),
       (11, 2, 'Bob/Olu', '', 'category.gif', '0', 1, 12, 11),
       (12, 2, 'Bob/Other Male', '', 'category.gif', '0', 1, 14, 42),
       (13, 2, 'Olu/Václav', '', 'category.gif', '0', 1, 15, 4),
       (14, 2, 'Olu/Other Male', '', 'category.gif', '0', 1, 16, 1),
       (15, 2, 'Václav/Other Male', '', 'category.gif', '0', 1, 17, 1),
       (16, 2, 'Fatima/Aisha', '', 'category.gif', '0', 1, 18, 56),
       (17, 2, 'Fatima/Samia', '', 'category.gif', '0', 1, 19, 3),
       (18, 2, 'Fatima/Other Female', '', 'category.gif', '0', 1, 20, 4),
       (19, 2, 'Aisha/Other Female', '', 'category.gif', '0', 1, 21, 0),
       (20, 2, 'Samia/Other Female', '', 'category.gif', '0', 1, 22, 0),
       (21, 2, 'Other Slash Pairing', '', 'category.gif', '0', 1, 23, 0),
       (22, 2, 'Multiple Slash Pairings', '', 'category.gif', '0', 1, 24, 0),
       (23, 3, 'Bill/Fatima', '', 'category.gif', '0', 1, 2, 53),
       (24, 3, 'Bill/Sara', '', 'category.gif', '0', 1, 3, 14),
       (25, 3, 'Bill/Aisha', '', 'category.gif', '0', 1, 4, 2),
       (26, 3, 'Bill/Other Female', '', 'category.gif', '0', 1, 5, 14),
       (27, 3, 'Bob/Don', '', 'category.gif', '0', 1, 6, 60),
       (28, 3, 'Bob/Fatima', '', 'category.gif', '0', 1, 7, 30),
       (29, 3, 'Bob/Aisha', '', 'category.gif', '0', 1, 9, 20),
       (30, 3, 'Bob/Other Female', '', 'category.gif', '0', 1, 10, 12),
       (31, 3, 'Václav/Fatima', '', 'category.gif', '0', 1, 11, 18),
       (32, 3, 'Václav/Aisha', '', 'category.gif', '0', 1, 12, 2),
       (33, 3, 'Václav/Isabelle', '', 'category.gif', '0', 1, 13, 1),
       (34, 3, 'Václav/Other Female', '', 'category.gif', '0', 1, 14, 1),
       (35, 3, 'Olu/Fatima', '', 'category.gif', '0', 1, 15, 1),
       (36, 3, 'Olu/Samia', '', 'category.gif', '0', 1, 16, 0),
       (37, 3, 'Bob/Samia', '', 'category.gif', '0', 1, 8, 22),
       (38, 3, 'Olu/Other Female', '', 'category.gif', '0', 1, 17, 0),
       (39, 3, 'Fatima/Peter', '', 'category.gif', '0', 1, 18, 8),
       (40, 3, 'Fatima/Other Male', '', 'category.gif', '0', 1, 19, 10),
       (43, 2, 'Bob/Vincent', '', 'category.gif', '0', 1, 13, 23),
       (44, 3, 'John Billson/Jane Billson', '', 'category.gif', '0', 1, 20, 4),
       (45, 3, 'Don/Other Male', '', 'category.gif', '0', 1, 21, 1),
       (47, 3, 'Vincent Corentin/Aisha Johnson', '', 'category.gif', '0', 1, 22, 2),
       (49, 3, 'Other Male/Other Female', '', 'category.gif', '0', 1, 1, 2),
       (50, 2, 'Other Male/Other Male', '', 'category.gif', '0', 1, 6, 7),
       (52, 2, 'Clone Bill/Clone Bob', '', 'category.gif', '0', 1, 5, 8),
       (53, 2, 'AU Bill/AU Bob', '', 'category.gif', '0', 1, 4, 7),
       (54, 2, 'Liam/Vincent Corentin', '', 'category.gif', '0', 1, 3, 1),
       (55, 2, 'Ben/Brad - Other Fandom', '', 'category.gif', '0', 1, 2, 7),
       (56, 2, 'Lisa White/Tania', '', 'category.gif', '0', 1, 1, 1),
       (57, 5, 'Bill/Bob/Olu', '', 'category.gif', '0', 1, 12, 1),
       (58, 5, 'Bill/Bob/Fatima', '', 'category.gif', '0', 1, 4, 7),
       (59, 5, 'Bill/Bob/Other Male', '', 'category.gif', '0', 1, 11, 4),
       (60, 5, 'Bill/Fatima/Aisha', '', 'category.gif', '0', 1, 7, 1),
       (61, 5, 'Bill/Bob/Václav', '', 'category.gif', '0', 1, 10, 6),
       (62, 5, 'Bob/Fatima/Aisha', '', 'category.gif', '0', 1, 6, 1),
       (63, 5, 'Bill/Bob/Vincent Corentin', '', 'category.gif', '0', 1, 9, 3),
       (64, 5, 'Bill/Bob/Mikhael', '', 'category.gif', '0', 1, 8, 1),
       (66, 5, 'Bill/Fatima/Václav', '', 'category.gif', '0', 1, 5, 1),
       (68, 5, 'Bill/Bob/Don', '', 'category.gif', '0', 1, 2, 1),
       (69, 5, 'Bill/Bob/Fatima/Aisha', '', 'category.gif', '0', 1, 3, 1),
       (70, 5, 'Bill/Bob/Samia', '', '', '0', 1, 1, 2);
DROP TABLE IF EXISTS `challenges`;
CREATE TABLE `challenges`
(
    `chalid`     int(11)      NOT NULL AUTO_INCREMENT,
    `challenger` varchar(200) NOT NULL DEFAULT '',
    `uid`        int(11)      NOT NULL DEFAULT '0',
    `title`      varchar(250) NOT NULL DEFAULT '',
    `catid`      varchar(200) NOT NULL DEFAULT '',
    `characters` varchar(200) NOT NULL DEFAULT '',
    `summary`    text         NOT NULL,
    PRIMARY KEY (`chalid`),
    KEY `title` (`catid`),
    KEY `uid` (`uid`),
    KEY `title_2` (`title`),
    KEY `characters` (`characters`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;
INSERT INTO challenges
VALUES (1, 'admin', 1, 'Legends of K/S', '1', '', '<p>Stories of the legendary heroes shared around the campfire.</p>'),
       (2, 'User1', 868, '10 Lines Never Used in a Film', '1,2', '',
        '<p>Use 1 or more of the then 10 sentences&nbsp;from the Youtube clip in a story.</p>'),
       (3, 'User2', 1044, 'kirk not the captain', '-1', '',
        '"<p></p>\r\n<p class=\"MsoNormal\">1 kirk is not the Captain spock is.</p>\r\n"');
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
INSERT INTO `chapters` (`chapid`, `title`, `inorder`, `notes`, `storytext`, `endnotes`, `validated`, `wordcount`,
                        `rating`, `reviews`, `sid`, `uid`, `count`)
VALUES (1, 'Chapter 1', 1, 'Bacon-related notes.', '', NULL, '1', 3992, 0, 2, 1, 2, 2872),
       (3, 'Chapter One', 1, '', '', NULL, '1', 8482, 0, 7, 3, 4, 4615),
       (4, 'Chapter Two', 2, '', '', NULL, '1', 1625, 0, 1, 3, 4, 2390),
       (50, 'Cat Lorem Ipsum 1', 1, '', '', NULL, '1', 2135, 0, 1, 50, 2, 5340),
       (51, 'Chapter 1', 1, '', '', NULL, '1', 4809, 0, 1, 51, 2, 4474),
       (52, 'Chapter 2', 2, '', '', NULL, '1', 2254, 0, 0, 51, 2, 1567),
       (53, 'Chapter 3', 1, '', '', NULL, '1', 5169, 0, 0, 51, 2, 2238),
       (54, 'Chapter 1', 1, '', '', NULL, '1', 2426, 0, 0, 54, 2, 2018),
       (109, 'Cakes', 1, '', '', NULL, '1', 13, 0, 0, 108, 3, 2020),
       (748, 'Bookmark', 1, '', '', NULL, '1', 12, 0, 0, 741, 5, 2080),
       (842, 'Windows 1252', 1, 'Eôs in ipsum ocûrrëret. Also first in series.', '', NULL, '1', 12, 0, 0, 835, 5, 2066),
       (845, 'Part 2', 1, 'Second story in the series.', '', NULL, '1', 11, 0, 0, 838, 5, 1310),
       (3906, 'A chapter', 1, '', NULL, '', '1', 12, 0, 1, 3519, 3, 3408),
       (4265, 'Japanese text', 1, '', NULL, 'Note about the story from the author.', '1', 9, 0, 2, 3721, 5, 3273),
       (4290, 'Chapter 1', 1, 'Accented lorem ipsum.', NULL, '', '1', 33225, 0, 7, 3745, 2, 2303),
       (4340, 'Zombies!', 1, '', NULL, '', '1', 2828, 0, 1, 3785, 2, 3225),
       (4687, 'Chapter 1', 1, 'Slightly longer text.', NULL, '', '1', 4849, 0, 2, 4035, 2, 2767);
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
VALUES (1, -1, 'Bill O\'Connell', '', ''),
       (2, -1, 'Bob Billson', '', ''),
       (3, -1, 'Fatima Habibi', '', ''),
       (4, -1, 'Václav', '', ''),
       (5, -1, 'Spyros Papadopoulos', '', ''),
       (6, -1, 'Olu Adebayo', '', ''),
       (7, -1, 'Samia Ben Abdel', '', ''),
       (8, -1, 'Einar Rønquist', '', ''),
       (9, -1, 'Aisha Johnson', '', ''),
       (10, -1, 'Mikhael Antonov', '', ''),
       (11, -1, 'Liam Habibi', '', ''),
       (12, -1, 'Bernard', '', ''),
       (13, -1, 'Vincent Corentin', '', ''),
       (14, -1, 'Other', '', '');
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
VALUES (1, 1, 'Action/Adventure'),
       (2, 1, 'Alternate Universe'),
       (3, 1, 'Angst'),
       (4, 1, 'Badfic'),
       (6, 1, 'Challenge'),
       (7, 1, 'Character Study'),
       (8, 1, 'Crossover'),
       (5, 1, 'Dark'),
       (9, 1, 'Drabble'),
       (10, 1, 'Drama'),
       (11, 1, 'Established Relationship'),
       (12, 1, 'First Time'),
       (13, 1, 'Friendship'),
       (14, 1, 'Holiday'),
       (15, 1, 'Humor'),
       (16, 1, 'Hurt/Comfort'),
       (17, 1, 'Jammies'),
       (42, 1, 'Kidfic'),
       (18, 1, 'Meridian Fix'),
       (19, 1, 'Missing Scene/Episode-Related'),
       (20, 1, 'Parody'),
       (21, 1, 'Poem/Limerick/Filk'),
       (22, 1, 'Pre-Relationship (het)'),
       (23, 1, 'Pre-Slash'),
       (24, 1, 'PWP - Plot, What Plot?'),
       (25, 1, 'Romance'),
       (26, 1, 'Smarm'),
       (29, 1, 'Songfic'),
       (27, 1, 'Team'),
       (28, 1, 'Vignette'),
       (30, 2, 'Adult Themes'),
       (31, 2, 'BDSM -- Bondage, Kink, etc.'),
       (32, 2, 'Character Death'),
       (35, 2, 'Language'),
       (33, 2, 'Non-Consensual Sex Acts'),
       (34, 2, 'Partner Betrayal'),
       (36, 2, 'Sexual Situations'),
       (37, 2, 'Violence');
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
DROP TABLE IF EXISTS `coauthors`;
CREATE TABLE `coauthors`
(
    `sid` int(11) NOT NULL DEFAULT '0',
    `uid` int(11) NOT NULL DEFAULT '0',
    PRIMARY KEY (`sid`, `uid`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;
INSERT INTO `coauthors` (`sid`, `uid`)
VALUES (1, 5),
       (108, 5);
DROP TABLE IF EXISTS `inseries`;
CREATE TABLE `inseries`
(
    `seriesid`    int(11) NOT NULL DEFAULT '0',
    `sid`         int(11) NOT NULL DEFAULT '0',
    `subseriesid` int(11) NOT NULL DEFAULT '0',
    `confirmed`   int(11) NOT NULL DEFAULT '0',
    `inorder`     int(11) NOT NULL DEFAULT '0',
    PRIMARY KEY (`sid`, `seriesid`, `subseriesid`),
    KEY `seriesid` (`seriesid`, `inorder`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;
INSERT INTO `inseries` (`seriesid`, `sid`, `subseriesid`, `confirmed`, `inorder`)
VALUES (169, 108, 0, 1, 19),
       (118, 838, 0, 1, 2),
       (118, 835, 0, 1, 1),
       (224, 3721, 0, 1, 5);
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
DROP TABLE IF EXISTS `series`;
CREATE TABLE `series`
(
    `seriesid`   int(11)      NOT NULL AUTO_INCREMENT,
    `title`      varchar(200) NOT NULL DEFAULT '',
    `summary`    text,
    `uid`        int(11)      NOT NULL DEFAULT '0',
    `isopen`     tinyint(4)   NOT NULL DEFAULT '0',
    `catid`      varchar(200) NOT NULL DEFAULT '0',
    `classes`    varchar(200)          DEFAULT NULL,
    `rating`     tinyint(4)   NOT NULL DEFAULT '0',
    `warnings`   varchar(250) NOT NULL DEFAULT '',
    `genres`     varchar(250) NOT NULL DEFAULT '',
    `characters` varchar(250) NOT NULL DEFAULT '',
    `reviews`    smallint(6)  NOT NULL DEFAULT '0',
    `challenges` varchar(200) NOT NULL DEFAULT '',
    `numstories` int(11)      NOT NULL DEFAULT '0',
    PRIMARY KEY (`seriesid`),
    KEY `catid` (`catid`),
    KEY `challenges` (`challenges`),
    KEY `warnings` (`warnings`),
    KEY `characters` (`characters`),
    KEY `genres` (`genres`),
    KEY `owner` (`uid`, `title`)
) ENGINE = MyISAM
  DEFAULT CHARSET = latin1;
INSERT INTO `series` (`seriesid`, `title`, `summary`, `uid`, `isopen`, `catid`, `classes`, `rating`, `warnings`,
                      `genres`, `characters`, `reviews`, `challenges`, `numstories`)
VALUES (118, 'Windows 1252',
        'This series takes place several months after the episode Need and deals with the aftermath of certain events - how they have affected Bob and what happens to the friendship between Bill and Bob as a result of Bill discovering his \'secret\'.',
        5, 0, '1', '3,7,10,13,26,30', 0, 'Adult Themes', 'Angst,Character Study,Drama,Friendship,Smarm', '2,1', 1, '',
        5),
       (169, 'Cakes', 'A challenge about cakes.', 3, 0, '6', '1,3,7,10,12,13,14,15,16,17,19,25', 0, '',
        'Action/Adventure,Angst,Character Study,Drama,First Time,Friendship,Holiday,Humor,Hurt/Comfort,Jammies,Missing Scene/Episode-Related,Romance',
        '2,5,1,11,9,13,3,4', 7, '', 24),
       (224, 'Japanese series', 'Chapter is in Japanese anyway.', 5, 0, '6', '3,11,14,15,25', 0, '',
        'Angst,Established Relationship,Holiday,Humor,Romance', '2,1,3', 4, '', 5);
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
INSERT INTO `stories` (`sid`, `title`, `summary`, `storynotes`, `catid`, `classes`, `charid`, `rid`, `date`, `updated`,
                       `uid`, `coauthors`, `featured`, `validated`, `completed`, `rr`, `wordcount`, `rating`, `reviews`,
                       `count`, `challenges`)
VALUES (1, 'Bacon ipsum', '&nbsp;<p> &nbsp;</p>Meat-related text.', NULL, '1', '3,10,16,26', '2,1', '3', '2006-02-09 22:21:35',
        '2006-02-09 22:21:35', 2, NULL, '', '1', '1', '', 3992, 0, 2, 2872, '0'),
       (3, 'Lorem ipsum', 'Short, and no tricky characters.', NULL, '6', '3,10,12,15,25', '2,1,3,4', '5',
        '2006-03-04 13:00:45', '2006-03-04 13:00:45', 4, NULL, '', '1', '1', '', 8482, 0, 7, 4615, '0'),
       (4, 'Email story', 'Email-related story.', NULL, '6', '15', '2,1', '3', '2006-03-04 13:16:12',
        '2006-03-04 13:16:12', 4, NULL, '', '1', '1', '', 1625, 0, 1, 2390, '0'),
       (50, 'Cat-related ipsum', 'Meow all night chew iPad power cord.', NULL, '6', '3,10,11,14', '2,1', '2',
        '2006-03-05 17:12:16', '2006-03-05 17:12:16', 2, NULL, '', '1', '1', '0', 2135, 0, 1, 5340, '0'),
       (51, 'Cupcake ipsum',
        'Biscuit candy cake candy macaroon. Soufflé marzipan croissant gummi bears. Wafer lollipop tart topping. Bonbon danish dragée lemon drops lemon drops caramels jelly. Tootsie roll chocolate cookie cake. Topping cheesecake lollipop halvah jujubes brownie bear claw. ',
        NULL, '6', '3,10,11,16', '2,1', '3', '2006-03-05 17:20:38', '2006-03-05 17:20:38', 2, NULL, '', '1', '1', '0',
        4809, 0, 1, 4474, '0'),
       (54, 'Carl Sagan ipsum', 'Only shorter.', NULL, '6', '11,16', '2,1', '3', '2006-03-05 17:27:05',
        '2006-03-05 17:27:05', 2, NULL, '', '1', '1', '0', 2426, 0, 0, 2018, '0'),
       (108, 'A lot of cakes', 'Lots and lots of cakes.', NULL, '6', '7,12,25', '2,1,4', '5', '2006-03-06 15:42:57',
        '2006-03-06 15:42:57', 3, NULL, '', '1', '1', '', 13, 0, 0, 2020, '0'),
       (741, 'Actually a bookmark', 'This is a story containing only a link to another location.', NULL, '1',
        '3,7,13,19', '2,1', '1', '2006-03-17 15:26:36', '2006-03-17 15:26:36', 5, NULL, '', '1', '1', '', 12, 0, 0,
        2080, '0'),
       (835, 'Windows 1252 Story', 'Eôs in ipsum ocûrrëret.', NULL, '1', '3,7,13,19,30', '2,1', '3',
        '2006-03-18 12:56:43', '2006-03-18 12:56:43', 5, NULL, '', '1', '1', '0', 12, 0, 0, 2066, '0'),
       (838, 'Another story in series', 'Things happen.', NULL, '1', '3,7,13,19', '2,1,14', '3', '2006-03-18 13:42:27',
        '2006-03-18 13:42:27', 5, NULL, '', '1', '1', '', 11, 0, 0, 1310, '0'),
       (3519, 'Beans and other vegetables', 'More vegetables.',
        'Written for someone\'s birthday as a small thank you for all their hard work and dedication here on Efiction Test archive and the Testing Solutions website.  Moderator, you\'re a star!',
        '6', '3,7,12,25', '2,1', '4', '2008-02-11 13:32:43', '2008-02-11 13:33:02', 3, '1', '0', '1', '1', '0', 12, 0,
        1, 3408, '0'),
       (3721, 'Japanese', 'Database is Latin-1 and doesn\'t support Japanese text.', '', '6',
        '37,1,2,3,7,10,11,14,15,16,25', '2,5,1,9,14,3,4', '4', '2008-10-08 20:58:26', '2008-10-08 20:58:29', 5, '1',
        '1', '1', '1', '0', 9, 0, 2, 3273, '0'),
       (3745, 'Accented lorem ipsum', 'A nice little summary.', '', '27', '2,3,13,16', '2,1,3,4', '3',
        '2008-11-28 14:10:56', '2008-11-28 14:10:59', 2, '1', '0', '1', '1', '0', 33225, 0, 7, 2303, '0'),
       (3785, 'Zombies', 'Zombie-related lorem ipsum.', 'Some story notes about Zombies.', '1', '13,14,27', '2,1,3,4',
        '1', '2008-12-27 07:18:06', '2008-12-27 07:18:09', 2, '1', '0', '1', '1', '0', 2828, 0, 1, 3225, '0'),
       (4035, 'Hipster ipsum', 'Bushwick man braid vaporware hot chicken yuccie snackwave cold-pressed +1 3 wolf moon.',
        'Thanks to betas.', '6', '16', '2,1,11,9,3,4', '3', '2010-01-03 10:04:12', '2010-01-03 10:04:16', 2, '0', '0',
        '1', '1', '0', 4849, 0, 2, 2767, '0');