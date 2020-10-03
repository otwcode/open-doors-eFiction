table_definitions = {
    'authors': [
        """\nDROP TABLE IF EXISTS `authors`;""",
        """CREATE TABLE `authors` (
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
        ) ENGINE=MyISAM;"""
    ],
    'categories': [
        """\nDROP TABLE IF EXISTS `categories`;""",
        """CREATE TABLE `categories` (
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
          ) ENGINE=MyISAM;"""
    ],
    'challenges': [
        """\nDROP TABLE IF EXISTS `challenges`;""",
        """CREATE TABLE `challenges` (
          `chalid` int(11) NOT NULL AUTO_INCREMENT,
          `challenger` varchar(200) NOT NULL DEFAULT '',
          `uid` int(11) NOT NULL DEFAULT 0,
          `title` varchar(250) NOT NULL DEFAULT '',
          `catid` varchar(200) NOT NULL DEFAULT '',
          `characters` varchar(200) NOT NULL DEFAULT '',
          `summary` text NOT NULL,
          `responses` int(11) NOT NULL DEFAULT 0,
          PRIMARY KEY (`chalid`)
          ) ENGINE=MyISAM;"""
    ],
    'chapters': [
        """\nDROP TABLE IF EXISTS `chapters`;""",
        """CREATE TABLE `chapters` (
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
          ) ENGINE=MyISAM;"""
    ],
    'characters': [
        """\nDROP TABLE IF EXISTS `characters`;""",
        """CREATE TABLE `characters` (
          `charid` int(11) NOT NULL AUTO_INCREMENT,
          `catid` int(11) NOT NULL DEFAULT 0,
          `charname` varchar(60) NOT NULL DEFAULT '',
          `bio` text NOT NULL,
          `image` varchar(200) NOT NULL DEFAULT '',
          PRIMARY KEY (`charid`)
          ) ENGINE=MyISAM;"""
    ],
    'classes': [
        """\nDROP TABLE IF EXISTS `classes`;""",
        """CREATE TABLE `classes` (
          `class_id` int(11) NOT NULL AUTO_INCREMENT,
          `class_type` int(11) NOT NULL DEFAULT 0,
          `class_name` varchar(100) NOT NULL DEFAULT '',
          PRIMARY KEY (`class_id`)
          ) ENGINE=MyISAM;"""
    ],
    'classtypes': [
        """\nDROP TABLE IF EXISTS `classtypes`;""",
        """CREATE TABLE `classtypes` (
          `classtype_id` int(11) NOT NULL AUTO_INCREMENT,
          `classtype_name` varchar(50) NOT NULL DEFAULT '',
          `classtype_title` varchar(50) NOT NULL DEFAULT '',
          PRIMARY KEY (`classtype_id`)
          ) ENGINE=MyISAM;"""
    ],
    'coauthors': [
        """\nDROP TABLE IF EXISTS `coauthors`;""",
        """CREATE TABLE `coauthors` (
          `sid` int(11) NOT NULL DEFAULT 0,
          `uid` int(11) NOT NULL DEFAULT 0,
          PRIMARY KEY (`sid`,`uid`)
          ) ENGINE=MyISAM;"""
    ],
    'inseries': [
        """\nDROP TABLE IF EXISTS `inseries`;""",
        """CREATE TABLE `inseries` (
          `seriesid` int(11) NOT NULL DEFAULT 0,
          `sid` int(11) NOT NULL DEFAULT 0,
          `subseriesid` int(11) NOT NULL DEFAULT 0,
          `confirmed` int(11) NOT NULL DEFAULT 0,
          `inorder` int(11) NOT NULL DEFAULT 0,
          PRIMARY KEY (`sid`,`seriesid`,`subseriesid`),
          KEY `seriesid` (`seriesid`,`inorder`)
          ) ENGINE=MyISAM;"""
    ],
    'ratings': [
        """\nDROP TABLE IF EXISTS `ratings`;""",
        """CREATE TABLE `ratings` (
          `rid` int(11) NOT NULL AUTO_INCREMENT,
          `rating` varchar(60) NOT NULL DEFAULT '',
          `ratingwarning` char(1) NOT NULL DEFAULT '0',
          `warningtext` text NOT NULL,
          PRIMARY KEY (`rid`)
          ) ENGINE=MyISAM;"""
    ],
    'series': [
        """\nDROP TABLE IF EXISTS `series`;""",
        """CREATE TABLE `series` (
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
          ) ENGINE=MyISAM;"""
    ],
    'stories': [
        """\nDROP TABLE IF EXISTS `stories`;""",
        """CREATE TABLE `stories` (
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
    ]
}


def create_def(tablename):
    return table_definitions[tablename]
