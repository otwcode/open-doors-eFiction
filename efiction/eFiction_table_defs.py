"""
eFiction table definitions
table names are replaced on the fly as the prefix may vary in different eFiction archives.
"""
import re

table_definitions = {
    'authorfields':
        """CREATE TABLE `{0}` (
           `field_id`       int(11)      NOT NULL AUTO_INCREMENT,
           `field_type`     tinyint(4)   NOT NULL DEFAULT '0',
           `field_name`     varchar(30)  NOT NULL DEFAULT ' ',
           `field_title`    varchar(255) NOT NULL DEFAULT ' ',
           `field_options`  text,
           `field_code_in`  text,
           `field_code_out` text,
           `field_on`       tinyint(1)   NOT NULL DEFAULT '0',
           PRIMARY KEY (`field_id`)
            ) ENGINE = MyISAM;""",
    'authorinfo':
        """CREATE TABLE `{0}` (
          `uid`   int(11)      NOT NULL DEFAULT '0',
          `field` int(11)      NOT NULL DEFAULT '0',
          `info`  varchar(255) NOT NULL DEFAULT ' ',
          PRIMARY KEY (`uid`, `field`),
          KEY `uid` (`uid`)
          ) ENGINE = MyISAM;""",
    'authorprefs':
        """CREATE TABLE `{0}` (
            `uid`        int(11)      NOT NULL DEFAULT '0',
            `newreviews` tinyint(1)   NOT NULL DEFAULT '0',
            `newrespond` tinyint(1)   NOT NULL DEFAULT '0',
            `ageconsent` tinyint(1)   NOT NULL DEFAULT '0',
            `alertson`   tinyint(1)   NOT NULL DEFAULT '0',
            `tinyMCE`    tinyint(1)   NOT NULL DEFAULT '0',
            `sortby`     tinyint(1)   NOT NULL DEFAULT '0',
            `storyindex` tinyint(1)   NOT NULL DEFAULT '0',
            `validated`  tinyint(1)   NOT NULL DEFAULT '0',
            `userskin`   varchar(60)  NOT NULL DEFAULT 'default',
            `level`      tinyint(1)   NOT NULL DEFAULT '0',
            `categories` varchar(200) NOT NULL DEFAULT '0',
            `contact`    tinyint(1)   NOT NULL DEFAULT '0',
            `stories`    int(11)      NOT NULL DEFAULT '0',
            PRIMARY KEY (`uid`)
        ) ENGINE = MyISAM""",
    'authors':
        """CREATE TABLE `{0}` (
          `uid` int(11) NOT NULL AUTO_INCREMENT,
          `penname` varchar(200) NOT NULL DEFAULT '',
          `realname` varchar(200) NOT NULL DEFAULT '',
          `email` varchar(200) NOT NULL DEFAULT '',
          `website` varchar(200) NOT NULL DEFAULT '',
          `bio` text DEFAULT NULL,
          `image` varchar(200) NOT NULL DEFAULT '',
          `date` datetime DEFAULT NULL,
          `admincreated` char(1) NOT NULL DEFAULT '0',
          `password` varchar(40) NOT NULL DEFAULT '0',
          PRIMARY KEY (`uid`)
        ) ENGINE=MyISAM;""",
    'blocks':
        """CREATE TABLE `{0}` (
            `block_id`        int(11)      NOT NULL AUTO_INCREMENT,
            `block_name`      varchar(30)  NOT NULL DEFAULT '',
            `block_title`     varchar(150) NOT NULL DEFAULT '',
            `block_file`      varchar(200) NOT NULL DEFAULT '',
            `block_status`    tinyint(1)   NOT NULL DEFAULT '0',
            `block_variables` text         NOT NULL,
            PRIMARY KEY (`block_id`),
            KEY `block_name` (`block_name`)
        ) ENGINE = MyISAM;""",
    'categories':
        """CREATE TABLE `{0}` (
          `catid` int(11) NOT NULL AUTO_INCREMENT,
          `parentcatid` int(11) NOT NULL DEFAULT -1,
          `category` varchar(60) NOT NULL DEFAULT '',
          `description` text NOT NULL,
          `image` varchar(100) NOT NULL DEFAULT '',
          `locked` char(1) NOT NULL DEFAULT '0',
          `leveldown` tinyint(4) NOT NULL DEFAULT 0,
          `displayorder` int(11) NOT NULL DEFAULT 0,
          `numitems` int(11) NOT NULL DEFAULT 0,
          PRIMARY KEY (`catid`)
          ) ENGINE=MyISAM;""",
    'challenges':
        """CREATE TABLE `{0}` (
          `chalid` int(11) NOT NULL AUTO_INCREMENT,
          `challenger` varchar(200) NOT NULL DEFAULT '',
          `uid` int(11) NOT NULL DEFAULT 0,
          `title` varchar(250) NOT NULL DEFAULT '',
          `catid` varchar(200) NOT NULL DEFAULT '',
          `characters` varchar(200) NOT NULL DEFAULT '',
          `summary` text NOT NULL,
          `responses` int(11) NOT NULL DEFAULT 0,
          PRIMARY KEY (`chalid`)
          ) ENGINE=MyISAM;""",
    'chapters':
        """CREATE TABLE `{0}` (
          `chapid` int(11) NOT NULL AUTO_INCREMENT,
          `title` varchar(250) NOT NULL DEFAULT '',
          `inorder` int(11) NOT NULL DEFAULT 0,
          `notes` text NOT NULL,
          `storytext` text,
          `endnotes` text DEFAULT NULL,
          `validated` char(1) NOT NULL DEFAULT '0',
          `wordcount` int(11) NOT NULL DEFAULT 0,
          `rating` tinyint(4) NOT NULL DEFAULT 0,
          `reviews` smallint(6) NOT NULL DEFAULT 0,
          `sid` int(11) NOT NULL DEFAULT 0,
          `uid` int(11) NOT NULL DEFAULT 0,
          `count` int(11) NOT NULL DEFAULT 0,
          PRIMARY KEY (`chapid`)
          ) ENGINE=MyISAM;""",
    'characters':
        """CREATE TABLE `{0}` (
          `charid` int(11) NOT NULL AUTO_INCREMENT,
          `catid` int(11) NOT NULL DEFAULT 0,
          `charname` varchar(60) NOT NULL DEFAULT '',
          `bio` text NOT NULL,
          `image` varchar(200) NOT NULL DEFAULT '',
          PRIMARY KEY (`charid`)
          ) ENGINE=MyISAM;""",
    'classes':
        """CREATE TABLE `{0}` (
          `class_id` int(11) NOT NULL AUTO_INCREMENT,
          `class_type` int(11) NOT NULL DEFAULT 0,
          `class_name` varchar(100) NOT NULL DEFAULT '',
          PRIMARY KEY (`class_id`)
          ) ENGINE=MyISAM;""",
    'classtypes':
        """CREATE TABLE `{0}` (
          `classtype_id` int(11) NOT NULL AUTO_INCREMENT,
          `classtype_name` varchar(50) NOT NULL DEFAULT '',
          `classtype_title` varchar(50) NOT NULL DEFAULT '',
          PRIMARY KEY (`classtype_id`)
          ) ENGINE=MyISAM;""",
    'coauthors':
        """CREATE TABLE `{0}` (
          `sid` int(11) NOT NULL DEFAULT 0,
          `uid` int(11) NOT NULL DEFAULT 0,
          PRIMARY KEY (`sid`,`uid`)
          ) ENGINE=MyISAM;""",
    'codeblocks':
        """CREATE TABLE `{0}` (
            `code_id`     int(11) NOT NULL AUTO_INCREMENT,
            `code_text`   text    NOT NULL,
            `code_type`   varchar(20) DEFAULT NULL,
            `code_module` varchar(60) DEFAULT NULL,
            PRIMARY KEY (`code_id`),
            KEY `code_type` (`code_type`)
        ) ENGINE = MyISAM;
        """,
    'comments':
        """CREATE TABLE `{0}` (
            `cid`     int(11)  NOT NULL AUTO_INCREMENT,
            `nid`     int(11)  NOT NULL DEFAULT '0',
            `uid`     int(11)  NOT NULL DEFAULT '0',
            `comment` text     NOT NULL,
            `time`    datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
            PRIMARY KEY (`cid`),
            KEY `commentlist` (`nid`, `time`)
        ) ENGINE = MyISAM;""",
    'favorites':
        """CREATE TABLE `{0}` (
            `uid`      int(11) NOT NULL DEFAULT '0',
            `item`     int(11) NOT NULL DEFAULT '0',
            `type`     char(2) NOT NULL DEFAULT '',
            `comments` text    NOT NULL,
            UNIQUE KEY `byitem` (`item`, `type`, `uid`),
            UNIQUE KEY `byuid` (`uid`, `type`, `item`)
        ) ENGINE = MyISAM;""",
    'inseries':
        """CREATE TABLE `{0}` (
          `seriesid` int(11) NOT NULL DEFAULT 0,
          `sid` int(11) NOT NULL DEFAULT 0,
          `subseriesid` int(11) NOT NULL DEFAULT 0,
          `confirmed` int(11) NOT NULL DEFAULT 0,
          `inorder` int(11) NOT NULL DEFAULT 0,
          PRIMARY KEY (`sid`,`seriesid`,`subseriesid`),
          KEY `seriesid` (`seriesid`,`inorder`)
          ) ENGINE=MyISAM;""",
    'log':
        """CREATE TABLE `{0}` (
              `log_id`        int(11)    NOT NULL AUTO_INCREMENT,
              `log_action`    varchar(255)        DEFAULT NULL,
              `log_uid`       int(11)    NOT NULL,
              `log_ip`        int(11) unsigned    DEFAULT NULL,
              `log_timestamp` timestamp  NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
              `log_type`      varchar(2) NOT NULL,
              PRIMARY KEY (`log_id`)
          ) ENGINE = MyISAM;""",
    'messages':
        """CREATE TABLE `{0}` (
          `message_id`    int(11)      NOT NULL AUTO_INCREMENT,
          `message_name`  varchar(50)  NOT NULL DEFAULT '',
          `message_title` varchar(200) NOT NULL DEFAULT '',
          `message_text`  text         NOT NULL,
          PRIMARY KEY (`message_id`),
          KEY `message_name` (`message_name`)
      ) ENGINE = MyISAM;""",
    'modules':
        """CREATE TABLE `{0}` (
          `id`      int(11)                                                     NOT NULL AUTO_INCREMENT,
          `name`    varchar(100) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL DEFAULT 'Test Module',
          `version` varchar(10) CHARACTER SET latin1 COLLATE latin1_general_ci  NOT NULL DEFAULT '1.0',
          PRIMARY KEY (`id`),
          KEY `name_version` (`name`, `version`)
          ) ENGINE = MyISAM;""",
    'news': """CREATE TABLE `{0}` (
          `nid`      int(11)      NOT NULL AUTO_INCREMENT,
          `author`   varchar(60)  NOT NULL DEFAULT '',
          `title`    varchar(255) NOT NULL DEFAULT '',
          `story`    text         NOT NULL,
          `time`     datetime              DEFAULT NULL,
          `comments` int(11)      NOT NULL DEFAULT '0',
          PRIMARY KEY (`nid`)
      ) ENGINE = MyISAM;""",
    'pagelinks':
        """CREATE TABLE `{0}` (
          `link_id`     int(11)      NOT NULL AUTO_INCREMENT,
          `link_name`   varchar(50)  NOT NULL DEFAULT '',
          `link_text`   varchar(100) NOT NULL DEFAULT '',
          `link_key`    char(1)               DEFAULT NULL,
          `link_url`    varchar(250) NOT NULL DEFAULT '',
          `link_target` char(1)      NOT NULL DEFAULT '0',
          `link_access` tinyint(4)   NOT NULL DEFAULT '0',
          PRIMARY KEY (`link_id`),
          KEY `link_name` (`link_name`)
      ) ENGINE = MyISAM;""",
    'panels':
        """CREATE TABLE `{0}` (
            `panel_id`     int(11)      NOT NULL AUTO_INCREMENT,
            `panel_name`   varchar(50)  NOT NULL DEFAULT 'unknown',
            `panel_title`  varchar(100) NOT NULL DEFAULT 'Unnamed Panel',
            `panel_url`    varchar(100)          DEFAULT NULL,
            `panel_level`  tinyint(4)   NOT NULL DEFAULT '3',
            `panel_order`  tinyint(4)   NOT NULL DEFAULT '0',
            `panel_hidden` tinyint(1)   NOT NULL DEFAULT '0',
            `panel_type`   varchar(20)  NOT NULL DEFAULT 'A',
            PRIMARY KEY (`panel_id`),
            KEY `panel_type` (`panel_type`, `panel_name`)
        ) ENGINE = MyISAM;""",
    'ratings':
        """CREATE TABLE `{0}` (
          `rid` int(11) NOT NULL AUTO_INCREMENT,
          `rating` varchar(60) NOT NULL DEFAULT '',
          `ratingwarning` char(1) NOT NULL DEFAULT '0',
          `warningtext` text NOT NULL,
          PRIMARY KEY (`rid`)
          ) ENGINE=MyISAM;""",
    'reviews': """CREATE TABLE `{0}` (
        `reviewid` int(11)     NOT NULL AUTO_INCREMENT,
        `item`     int(11)     NOT NULL DEFAULT '0',
        `chapid`   int(11)     NOT NULL DEFAULT '0',
        `reviewer` varchar(60) NOT NULL DEFAULT '0',
        `uid`      int(11)     NOT NULL DEFAULT '0',
        `review`   text        NOT NULL,
        `date`     datetime    NOT NULL DEFAULT '0000-00-00 00:00:00',
        `rating`   int(11)     NOT NULL DEFAULT '0',
        `respond`  char(1)     NOT NULL DEFAULT '0',
        `type`     varchar(2)  NOT NULL DEFAULT 'ST',
        PRIMARY KEY (`reviewid`),
        KEY `psid` (`chapid`),
        KEY `rating` (`rating`),
        KEY `respond` (`respond`),
        KEY `avgrating` (`type`, `item`, `rating`),
        KEY `bychapter` (`chapid`, `rating`),
        KEY `byuid` (`uid`, `item`, `type`)
    ) ENGINE = MyISAM;""",
    'series': """CREATE TABLE `{0}` (
          `seriesid` int(11) NOT NULL AUTO_INCREMENT,
          `title` varchar(200) NOT NULL DEFAULT '',
          `summary` text DEFAULT NULL,
          `uid` int(11) NOT NULL DEFAULT 0,
          `isopen` tinyint(4) NOT NULL DEFAULT 0,
          `catid` varchar(200) NOT NULL DEFAULT '0',
          `classes` varchar(200) DEFAULT NULL,
          `rating` tinyint(4) NOT NULL DEFAULT 0,
          `warnings` varchar(250) NOT NULL DEFAULT '',
          `genres` varchar(250) NOT NULL DEFAULT '',
          `characters` varchar(250) NOT NULL DEFAULT '',
          `reviews` smallint(6) NOT NULL DEFAULT 0,
          `challenges` varchar(200) NOT NULL DEFAULT '0',
          `numstories` int(11) NOT NULL DEFAULT 0,
          PRIMARY KEY (`seriesid`)
          ) ENGINE=MyISAM;""",
    'settings': """CREATE TABLE `{0}` (
            `sitekey`        varchar(50)  NOT NULL DEFAULT '1',
            `sitename`       varchar(200) NOT NULL DEFAULT 'Your Site',
            `slogan`         varchar(200) NOT NULL DEFAULT 'It''s a cool site!',
            `url`            varchar(200) NOT NULL DEFAULT 'http://www.yoursite.com',
            `siteemail`      varchar(200) NOT NULL DEFAULT 'you@yoursite.com',
            `tableprefix`    varchar(50)  NOT NULL DEFAULT '',
            `skin`           varchar(50)  NOT NULL DEFAULT 'default',
            `hiddenskins`    varchar(255)          DEFAULT '',
            `language`       varchar(10)  NOT NULL DEFAULT 'en',
            `submissionsoff` tinyint(1)   NOT NULL DEFAULT '0',
            `storiespath`    varchar(20)  NOT NULL DEFAULT 'stories',
            `store`          varchar(5)   NOT NULL DEFAULT 'files',
            `autovalidate`   tinyint(1)   NOT NULL DEFAULT '0',
            `coauthallowed`  int(1)       NOT NULL DEFAULT '0',
            `maxwords`       int(11)      NOT NULL DEFAULT '0',
            `minwords`       int(11)      NOT NULL DEFAULT '0',
            `imageupload`    tinyint(1)   NOT NULL DEFAULT '0',
            `imageheight`    int(11)      NOT NULL DEFAULT '200',
            `imagewidth`     int(11)      NOT NULL DEFAULT '200',
            `roundrobins`    tinyint(1)   NOT NULL DEFAULT '0',
            `allowseries`    tinyint(4)   NOT NULL DEFAULT '2',
            `tinyMCE`        tinyint(1)   NOT NULL DEFAULT '0',
            `allowed_tags`   varchar(200) NOT NULL DEFAULT '<b><i><u><center><hr><p><br /><br><blockquote><ol><ul><li><img><strong><em>',
            `favorites`      tinyint(1)   NOT NULL DEFAULT '0',
            `multiplecats`   tinyint(1)   NOT NULL DEFAULT '0',
            `newscomments`   tinyint(1)   NOT NULL DEFAULT '0',
            `logging`        tinyint(1)   NOT NULL DEFAULT '0',
            `maintenance`    tinyint(1)   NOT NULL DEFAULT '0',
            `debug`          tinyint(1)   NOT NULL DEFAULT '0',
            `captcha`        tinyint(1)   NOT NULL DEFAULT '0',
            `dateformat`     varchar(20)  NOT NULL DEFAULT 'd/m/y',
            `timeformat`     varchar(20)  NOT NULL DEFAULT '- h:i a',
            `recentdays`     tinyint(2)   NOT NULL DEFAULT '7',
            `displaycolumns` tinyint(1)   NOT NULL DEFAULT '1',
            `itemsperpage`   tinyint(2)   NOT NULL DEFAULT '25',
            `extendcats`     tinyint(1)   NOT NULL DEFAULT '0',
            `displayindex`   tinyint(1)   NOT NULL DEFAULT '0',
            `defaultsort`    tinyint(1)   NOT NULL DEFAULT '0',
            `displayprofile` tinyint(1)   NOT NULL DEFAULT '0',
            `linkstyle`      tinyint(1)   NOT NULL DEFAULT '0',
            `linkrange`      tinyint(2)   NOT NULL DEFAULT '5',
            `reviewsallowed` tinyint(1)   NOT NULL DEFAULT '0',
            `ratings`        tinyint(1)   NOT NULL DEFAULT '0',
            `anonreviews`    tinyint(1)   NOT NULL DEFAULT '0',
            `revdelete`      tinyint(1)   NOT NULL DEFAULT '0',
            `rateonly`       tinyint(1)   NOT NULL DEFAULT '0',
            `pwdsetting`     tinyint(1)   NOT NULL DEFAULT '0',
            `alertson`       tinyint(1)   NOT NULL DEFAULT '0',
            `disablepopups`  tinyint(1)   NOT NULL DEFAULT '0',
            `agestatement`   tinyint(1)   NOT NULL DEFAULT '0',
            `words`          text,
            `version`        varchar(10)  NOT NULL DEFAULT '3.3',
            `smtp_host`      varchar(200)          DEFAULT NULL,
            `smtp_username`  varchar(50)           DEFAULT NULL,
            `smtp_password`  varchar(50)           DEFAULT NULL,
            PRIMARY KEY (`sitekey`)
        ) ENGINE = MyISAM;""",
    'stats':
        """CREATE TABLE `{0}` (
            `sitekey`      varchar(50) NOT NULL DEFAULT '0',
            `stories`      int(11)     NOT NULL DEFAULT '0',
            `chapters`     int(11)     NOT NULL DEFAULT '0',
            `series`       int(11)     NOT NULL DEFAULT '0',
            `reviews`      int(11)     NOT NULL DEFAULT '0',
            `wordcount`    int(11)     NOT NULL DEFAULT '0',
            `authors`      int(11)     NOT NULL DEFAULT '0',
            `members`      int(11)     NOT NULL DEFAULT '0',
            `reviewers`    int(11)     NOT NULL DEFAULT '0',
            `newestmember` int(11)     NOT NULL DEFAULT '0'
        ) ENGINE = MyISAM;""",
    'stories':
        """CREATE TABLE `{0}` (
          `sid` int(11) NOT NULL AUTO_INCREMENT,
          `title` varchar(200) NOT NULL DEFAULT '',
          `summary` text,
          `storynotes` text,
          `catid` varchar(100) NOT NULL DEFAULT '0',
          `classes` varchar(200) DEFAULT NULL,
          `charid` varchar(250) NOT NULL DEFAULT '0',
          `rid` varchar(25) NOT NULL DEFAULT '0',
          `date` datetime DEFAULT NULL,
          `updated` datetime DEFAULT NULL,
          `uid` int(11) NOT NULL DEFAULT '0',
          `coauthors` varchar(200) DEFAULT NULL,
          `featured` char(1) NOT NULL DEFAULT '0',
          `validated` char(1) NOT NULL DEFAULT '0',
          `completed` char(1) NOT NULL DEFAULT '0',
          `rr` char(1) NOT NULL DEFAULT '0',
          `wordcount` int(11) NOT NULL DEFAULT '0',
          `rating` tinyint(4) NOT NULL DEFAULT '0',
          `reviews` smallint(6) NOT NULL DEFAULT '0',
          `count` int(11) NOT NULL DEFAULT '0',
          `challenges` varchar(200) NOT NULL DEFAULT '0',
          PRIMARY KEY (`sid`)
        ) ENGINE=MyISAM;
        """
}


def create_def(table_name):
    """
    Strip prefix from table name and generate DROP TABLE and CREATE TABlE statements
    :param table_name: the original table name (eg: fanfiction_stories)
    :return: the DROP and CREATE statements for this table
    """
    key = re.sub(r'\S+_', '', table_name)
    if key:
        drop_table_def = f"\nDROP TABLE IF EXISTS `{table_name}`;"
        create_table_def = table_definitions[key].format(table_name)
        return [drop_table_def, create_table_def]
    else:
        return []
