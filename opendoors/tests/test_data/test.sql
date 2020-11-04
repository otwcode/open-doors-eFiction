DROP DATABASE IF EXISTS od_test_sql;
CREATE DATABASE od_test_sql;
USE od_test_sql;
CREATE TABLE od_table
(
    `id`    int(11)      NOT NULL AUTO_INCREMENT,
    `name`  varchar(25) NOT NULL DEFAULT '',
    `thing` varchar(25),
    PRIMARY KEY (`id`),
    UNIQUE KEY `id_UNIQUE` (`id`)
);
INSERT INTO od_table (id, name, thing)
VALUES (1, 'Name1\'s "stringé"', NULL),
       (2, 'Name2', 'thing');
CREATE TABLE od_table2
(
    `id`    int(11)      NOT NULL AUTO_INCREMENT,
    `column`  varchar(25) NOT NULL DEFAULT '',
    PRIMARY KEY (`id`),
    UNIQUE KEY `id_UNIQUE` (`id`)
);
INSERT INTO od_table2 (id, `column`)
VALUES (1, 'thing1');