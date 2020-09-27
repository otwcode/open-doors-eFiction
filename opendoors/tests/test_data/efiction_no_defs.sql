# Dump of table fanfiction_authorfields
# Dump DATE : 20-Apr-2020
INSERT INTO fanfiction_authorfields VALUES ("1","4","lj","Live Journal","http://{info}.livejournal.com","","","0");
INSERT INTO fanfiction_authorfields VALUES ("2","1","website","Web Site","","","","1");
INSERT INTO fanfiction_authorfields VALUES ("6","5","Yahoo","Yahoo IM","","$output .= \"<div><label for=\'AOL\'>\".$field[\'field_title\'].\":</label><INPUT type=\'text\' class=\'textbox\'  name=\'af_\".$field[\'field_name\'].\"\' maxlength=\'40\' value=\'\".(!empty($user[\'af_\'.$field[\'field_id\']]) ? $user[\'af_\'.$field[\'field_id\']] : \"\").\"\' size=\'20\'></div>\";','$thisfield = \"<a href=\\\"http://edit.yahoo.com/config/send_webmesg?.target=\".$field[\'info\'].\"&.src=pg\\\"><img border=\'0\' src=\\\"http://opi.yahoo.com/online?u=\".$field[\'info\'].\"&m=g&t=1\\\"> \".format_email($field[\'info\']).\"</a>\";","1");


# Dump of table fanfiction_authorinfo
# Dump DATE : 20-Apr-2020
INSERT INTO fanfiction_authorinfo VALUES ("3","2","http://example.com");
INSERT INTO fanfiction_authorinfo VALUES ("4","3","0");
INSERT INTO fanfiction_authorinfo VALUES ("1","8","No");
INSERT INTO fanfiction_authorinfo VALUES ("5","8","No");
INSERT INTO fanfiction_authorinfo VALUES ("0","2","http://example.com");


# Dump of table fanfiction_authorprefs
# Dump DATE : 20-Apr-2020
INSERT INTO fanfiction_authorprefs VALUES	("1","0","0","1","0","0","0","0","0","test","1","0","1","0");
INSERT INTO fanfiction_authorprefs VALUES	("5","1","0","1","1","0","0","0","1","BillBob","2","0","1","77");

# Dump of table fanfiction_authors
# Dump DATE : 20-Apr-2020
INSERT INTO fanfiction_authors VALUES	("1","Author1","Author1","A1@example.com","","","","2006-01-06 01:02:13","0","xfghtu");
INSERT INTO fanfiction_authors VALUES	("2","B Author 2","B Author 2","B2@example.com","","","bauthor2","2006-02-09 01:37:24","1","xfghtu");
INSERT INTO fanfiction_authors VALUES	("3","C Author 3","C Author 3","C3@example.com","http://example.com","An author bio with some text in it","","2006-02-16 22:58:02","1","xfghtu");
INSERT INTO fanfiction_authors VALUES	("4","D Author 4","D Author 4","D4@example.com","","","","2006-02-15 23:00:00","1","xfghtu");
INSERT INTO fanfiction_authors VALUES	("5","E Author 5","E Author 5","E5@example.com","www.example.com","","eauthor5","2006-02-16 23:00:00","1","xfghtu");

# Dump of table fanfiction_blocks
# Dump DATE : 20-Apr-2020
INSERT INTO fanfiction_blocks VALUES ("1","categories","Story Categories","categories/categories.php","1","a:2:{s:7:\"columns\";s:1:\"0\";s:8:\"template\";s:38:\"{image} {link} [{count}] {description}\";}");
INSERT INTO fanfiction_blocks VALUES ("3","info","About Efiction Test","info/info.php","1","a:1:{s:5:\"style\";s:1:\"1\";}");
INSERT INTO fanfiction_blocks VALUES ("5","menu","Main Menu","menu/menu.php","1","a:1:{s:7:\"content\";a:14:{i:0;s:4:\"home\";i:1;s:6:\"recent\";i:2;s:6:\"titles\";i:3;s:8:\"catslink\";i:4;s:6:\"series\";i:5;s:7:\"authors\";i:6;s:10:\"challenges\";i:7;s:6:\"search\";i:8;s:4:\"tens\";i:9;s:4:\"help\";i:10;s:9:\"contactus\";i:11;s:5:\"login\";i:12;s:6:\"logout\";i:13;s:9:\"adminarea\";}}");
INSERT INTO fanfiction_blocks VALUES ("9","news","Latest News","news/news.php","1","a:1:{s:3:\"num\";s:1:\"2\";}");

# Dump of table fanfiction_categories
# Dump DATE : 20-Apr-2020
INSERT INTO fanfiction_categories VALUES ("1",-1,"General","","categoryfp.gif","0","0","1","1310");
INSERT INTO fanfiction_categories VALUES ("2",-1,"Slash Pairings","","categoryfp.gif","1","0","2","2332");
INSERT INTO fanfiction_categories VALUES ("3",-1,"Het Pairings","","categoryfp.gif","1","0","3","229");
INSERT INTO fanfiction_categories VALUES ("5",-1,"Threesomes, Moresomes","","categoryfp.gif","0","0","4","29");
INSERT INTO fanfiction_categories VALUES ("6","2","Bill/Bob","","category.gif","0","1","7","2227");
INSERT INTO fanfiction_categories VALUES ("7","2","Bill/Václav","","category.gif","0","1","8","6");
INSERT INTO fanfiction_categories VALUES ("8","2","Bill/Olu","","category.gif","0","1","9","1");
INSERT INTO fanfiction_categories VALUES ("9","2","Bill/Other Male","","category.gif","0","1","10","17");
INSERT INTO fanfiction_categories VALUES ("10","2","Bob/Václav","","category.gif","0","1","11","8");
INSERT INTO fanfiction_categories VALUES ("11","2","Bob/Olu","","category.gif","0","1","12","11");
INSERT INTO fanfiction_categories VALUES ("12","2","Bob/Other Male","","category.gif","0","1","14","42");
INSERT INTO fanfiction_categories VALUES ("13","2","Olu/Václav","","category.gif","0","1","15","4");
INSERT INTO fanfiction_categories VALUES ("14","2","Olu/Other Male","","category.gif","0","1","16","1");
INSERT INTO fanfiction_categories VALUES ("15","2","Václav/Other Male","","category.gif","0","1","17","1");
INSERT INTO fanfiction_categories VALUES ("16","2","Fatima/Aisha","","category.gif","0","1","18","56");
INSERT INTO fanfiction_categories VALUES ("17","2","Fatima/Samia","","category.gif","0","1","19","3");
INSERT INTO fanfiction_categories VALUES ("18","2","Fatima/Other Female","","category.gif","0","1","20","4");
INSERT INTO fanfiction_categories VALUES ("19","2","Aisha/Other Female","","category.gif","0","1","21","0");
INSERT INTO fanfiction_categories VALUES ("20","2","Samia/Other Female","","category.gif","0","1","22","0");
INSERT INTO fanfiction_categories VALUES ("21","2","Other Slash Pairing","","category.gif","0","1","23","0");
INSERT INTO fanfiction_categories VALUES ("22","2","Multiple Slash Pairings","","category.gif","0","1","24","0");
INSERT INTO fanfiction_categories VALUES ("23","3","Bill/Fatima","","category.gif","0","1","2","53");
INSERT INTO fanfiction_categories VALUES ("24","3","Bill/Sara","","category.gif","0","1","3","14");
INSERT INTO fanfiction_categories VALUES ("25","3","Bill/Aisha","","category.gif","0","1","4","2");
INSERT INTO fanfiction_categories VALUES ("26","3","Bill/Other Female","","category.gif","0","1","5","14");
INSERT INTO fanfiction_categories VALUES ("27","3","Bob/Don","","category.gif","0","1","6","60");
INSERT INTO fanfiction_categories VALUES ("28","3","Bob/Fatima","","category.gif","0","1","7","30");
INSERT INTO fanfiction_categories VALUES ("29","3","Bob/Aisha","","category.gif","0","1","9","20");
INSERT INTO fanfiction_categories VALUES ("30","3","Bob/Other Female","","category.gif","0","1","10","12");
INSERT INTO fanfiction_categories VALUES ("31","3","Václav/Fatima","","category.gif","0","1","11","18");
INSERT INTO fanfiction_categories VALUES ("32","3","Václav/Aisha","","category.gif","0","1","12","2");
INSERT INTO fanfiction_categories VALUES ("33","3","Václav/Isabelle","","category.gif","0","1","13","1");
INSERT INTO fanfiction_categories VALUES ("34","3","Václav/Other Female","","category.gif","0","1","14","1");
INSERT INTO fanfiction_categories VALUES ("35","3","Olu/Fatima","","category.gif","0","1","15","1");
INSERT INTO fanfiction_categories VALUES ("36","3","Olu/Samia","","category.gif","0","1","16","0");
INSERT INTO fanfiction_categories VALUES ("37","3","Bob/Samia","","category.gif","0","1","8","22");
INSERT INTO fanfiction_categories VALUES ("38","3","Olu/Other Female","","category.gif","0","1","17","0");
INSERT INTO fanfiction_categories VALUES ("39","3","Fatima/Peter","","category.gif","0","1","18","8");
INSERT INTO fanfiction_categories VALUES ("40","3","Fatima/Other Male","","category.gif","0","1","19","10");
INSERT INTO fanfiction_categories VALUES ("43","2","Bob/Vincent","","category.gif","0","1","13","23");
INSERT INTO fanfiction_categories VALUES ("44","3","John Billson/Jane Billson","","category.gif","0","1","20","4");
INSERT INTO fanfiction_categories VALUES ("45","3","Don/Other Male","","category.gif","0","1","21","1");
INSERT INTO fanfiction_categories VALUES ("47","3","Vincent Corentin/Aisha Johnson","","category.gif","0","1","22","2");
INSERT INTO fanfiction_categories VALUES ("49","3","Other Male/Other Female","","category.gif","0","1","1","2");
INSERT INTO fanfiction_categories VALUES ("50","2","Other Male/Other Male","","category.gif","0","1","6","7");
INSERT INTO fanfiction_categories VALUES ("52","2","Clone Bill/Clone Bob","","category.gif","0","1","5","8");
INSERT INTO fanfiction_categories VALUES ("53","2","AU Bill/AU Bob","","category.gif","0","1","4","7");
INSERT INTO fanfiction_categories VALUES ("54","2","Liam/Vincent Corentin","","category.gif","0","1","3","1");
INSERT INTO fanfiction_categories VALUES ("55","2","Ben/Brad - Other Fandom","","category.gif","0","1","2","7");
INSERT INTO fanfiction_categories VALUES ("56","2","Lisa White/Tania","","category.gif","0","1","1","1");
INSERT INTO fanfiction_categories VALUES ("57","5","Bill/Bob/Olu","","category.gif","0","1","12","1");
INSERT INTO fanfiction_categories VALUES ("58","5","Bill/Bob/Fatima","","category.gif","0","1","4","7");
INSERT INTO fanfiction_categories VALUES ("59","5","Bill/Bob/Other Male","","category.gif","0","1","11","4");
INSERT INTO fanfiction_categories VALUES ("60","5","Bill/Fatima/Aisha","","category.gif","0","1","7","1");
INSERT INTO fanfiction_categories VALUES ("61","5","Bill/Bob/Václav","","category.gif","0","1","10","6");
INSERT INTO fanfiction_categories VALUES ("62","5","Bob/Fatima/Aisha","","category.gif","0","1","6","1");
INSERT INTO fanfiction_categories VALUES ("63","5","Bill/Bob/Vincent Corentin","","category.gif","0","1","9","3");
INSERT INTO fanfiction_categories VALUES ("64","5","Bill/Bob/Mikhael","","category.gif","0","1","8","1");
INSERT INTO fanfiction_categories VALUES ("66","5","Bill/Fatima/Václav","","category.gif","0","1","5","1");
INSERT INTO fanfiction_categories VALUES ("68","5","Bill/Bob/Don","","category.gif","0","1","2","1");
INSERT INTO fanfiction_categories VALUES ("69","5","Bill/Bob/Fatima/Aisha","","category.gif","0","1","3","1");
INSERT INTO fanfiction_categories VALUES ("70","5","Bill/Bob/Samia","","","0","1","1","2");


# Dump of table fanfiction_challenges
# Dump DATE : 20-Apr-2020


# Dump of table fanfiction_chapters
# Dump DATE : 20-Apr-2020
INSERT INTO fanfiction_chapters VALUES ("1","Chapter 1","1","Bacon-related notes.","",NULL,"1","3992","0","2","1","2","2872");
INSERT INTO fanfiction_chapters VALUES ("3","Chapter One","1","","",NULL,"1","8482","0","7","3","4","4615");
INSERT INTO fanfiction_chapters VALUES ("4","Chapter Two","2","","",NULL,"1","1625","0","1","3","4","2390");
INSERT INTO fanfiction_chapters VALUES ("50","Cat Lorem Ipsum 1","1","","",NULL,"1","2135","0","1","50","2","5340");
INSERT INTO fanfiction_chapters VALUES ("51","Chapter 1","1","","",NULL,"1","4809","0","1","51","2","4474");
INSERT INTO fanfiction_chapters VALUES ("52","Chapter 2","2","","",NULL,"1","2254","0","0","51","2","1567");
INSERT INTO fanfiction_chapters VALUES ("53","Chapter 3","1","","",NULL,"1","5169","0","0","51","2","2238");
INSERT INTO fanfiction_chapters VALUES ("54","Chapter 1","1","","",NULL,"1","2426","0","0","54","2","2018");
INSERT INTO fanfiction_chapters VALUES ("109","Cakes","1","","",NULL,"1","13","0","0","108","3","2020");
INSERT INTO fanfiction_chapters VALUES ("748","Bookmark","1","","",NULL,"1","12","0","0","741","5","2080");
INSERT INTO fanfiction_chapters VALUES ("842","Windows 1252","1","Eôs in ipsum ocûrrëret. Also first in series.","",NULL,"1","12","0","0","835","5","2066");
INSERT INTO fanfiction_chapters VALUES ("845","Part 2","1","Second story in the series.","",NULL,"1","11","0","0","838","5","1310");
INSERT INTO fanfiction_chapters VALUES ("3906","A chapter","1","",NULL,"","1","12","0","1","3519","3","3408");
INSERT INTO fanfiction_chapters VALUES ("4265","Japanese text","1","",NULL,"Note about the story from the author.","1","9","0","2","3721","5","3273");
INSERT INTO fanfiction_chapters VALUES ("4290","Chapter 1","1","Accented lorem ipsum.",NULL,"","1","33225","0","7","3745","2","2303");
INSERT INTO fanfiction_chapters VALUES ("4340","Zombies!","1","",NULL,"","1","2828","0","1","3785","2","3225");
INSERT INTO fanfiction_chapters VALUES ("4687","Chapter 1","1","Slightly longer text.",NULL,"","1","4849","0","2","4035","2","2767");


# Dump of table fanfiction_characters
# Dump DATE : 20-Apr-2020
INSERT INTO fanfiction_characters VALUES ("1",-1,"Bill O\'Connell","","");
INSERT INTO fanfiction_characters VALUES ("2",-1,"Bob Billson","","");
INSERT INTO fanfiction_characters VALUES ("3",-1,"Fatima Habibi","","");
INSERT INTO fanfiction_characters VALUES ("4",-1,"Václav","","");
INSERT INTO fanfiction_characters VALUES ("5",-1,"Spyros Papadopoulos","","");
INSERT INTO fanfiction_characters VALUES ("6",-1,"Olu Adebayo","","");
INSERT INTO fanfiction_characters VALUES ("7",-1,"Samia Ben Abdel","","");
INSERT INTO fanfiction_characters VALUES ("8",-1,"Einar Rønquist","","");
INSERT INTO fanfiction_characters VALUES ("9",-1,"Aisha Johnson","","");
INSERT INTO fanfiction_characters VALUES ("10",-1,"Mikhael Antonov","","");
INSERT INTO fanfiction_characters VALUES ("11",-1,"Liam Habibi","","");
INSERT INTO fanfiction_characters VALUES ("12",-1,"Bernard","","");
INSERT INTO fanfiction_characters VALUES ("13",-1,"Vincent Corentin","","");
INSERT INTO fanfiction_characters VALUES ("14",-1,"Other","","");


# Dump of table fanfiction_classes
# Dump DATE : 20-Apr-2020

INSERT INTO fanfiction_classes VALUES ("1","1","Action/Adventure");
INSERT INTO fanfiction_classes VALUES ("2","1","Alternate Universe");
INSERT INTO fanfiction_classes VALUES ("3","1","Angst");
INSERT INTO fanfiction_classes VALUES ("4","1","Badfic");
INSERT INTO fanfiction_classes VALUES ("6","1","Challenge");
INSERT INTO fanfiction_classes VALUES ("7","1","Character Study");
INSERT INTO fanfiction_classes VALUES ("8","1","Crossover");
INSERT INTO fanfiction_classes VALUES ("5","1","Dark");
INSERT INTO fanfiction_classes VALUES ("9","1","Drabble");
INSERT INTO fanfiction_classes VALUES ("10","1","Drama");
INSERT INTO fanfiction_classes VALUES ("11","1","Established Relationship");
INSERT INTO fanfiction_classes VALUES ("12","1","First Time");
INSERT INTO fanfiction_classes VALUES ("13","1","Friendship");
INSERT INTO fanfiction_classes VALUES ("14","1","Holiday");
INSERT INTO fanfiction_classes VALUES ("15","1","Humor");
INSERT INTO fanfiction_classes VALUES ("16","1","Hurt/Comfort");
INSERT INTO fanfiction_classes VALUES ("17","1","Jammies");
INSERT INTO fanfiction_classes VALUES ("42","1","Kidfic");
INSERT INTO fanfiction_classes VALUES ("18","1","Meridian Fix");
INSERT INTO fanfiction_classes VALUES ("19","1","Missing Scene/Episode-Related");
INSERT INTO fanfiction_classes VALUES ("20","1","Parody");
INSERT INTO fanfiction_classes VALUES ("21","1","Poem/Limerick/Filk");
INSERT INTO fanfiction_classes VALUES ("22","1","Pre-Relationship (het)");
INSERT INTO fanfiction_classes VALUES ("23","1","Pre-Slash");
INSERT INTO fanfiction_classes VALUES ("24","1","PWP - Plot, What Plot?");
INSERT INTO fanfiction_classes VALUES ("25","1","Romance");
INSERT INTO fanfiction_classes VALUES ("26","1","Smarm");
INSERT INTO fanfiction_classes VALUES ("29","1","Songfic");
INSERT INTO fanfiction_classes VALUES ("27","1","Team");
INSERT INTO fanfiction_classes VALUES ("28","1","Vignette");
INSERT INTO fanfiction_classes VALUES ("30","2","Adult Themes");
INSERT INTO fanfiction_classes VALUES ("31","2","BDSM -- Bondage, Kink, etc.");
INSERT INTO fanfiction_classes VALUES ("32","2","Character Death");
INSERT INTO fanfiction_classes VALUES ("35","2","Language");
INSERT INTO fanfiction_classes VALUES ("33","2","Non-Consensual Sex Acts");
INSERT INTO fanfiction_classes VALUES ("34","2","Partner Betrayal");
INSERT INTO fanfiction_classes VALUES ("36","2","Sexual Situations");
INSERT INTO fanfiction_classes VALUES ("37","2","Violence");




# Dump of table fanfiction_classtypes
# Dump DATE : 20-Apr-2020

INSERT INTO fanfiction_classtypes VALUES ("1","genres","Genres");
INSERT INTO fanfiction_classtypes VALUES ("2","warnings","Warnings");


# Dump of table fanfiction_coauthors
# Dump DATE : 20-Apr-2020
INSERT INTO fanfiction_coauthors VALUES ("1","5");
INSERT INTO fanfiction_coauthors VALUES ("108","5");


# Dump of table fanfiction_codeblocks
# Dump DATE : 20-Apr-2020


# Dump of table fanfiction_comments
# Dump DATE : 20-Apr-2020

INSERT INTO fanfiction_comments VALUES ("1","1","3","The new archive is amazing :)","2006-04-03 18:12:00");
INSERT INTO fanfiction_comments VALUES ("2","1","305","The site looks *stupendous*!","2006-04-05 18:37:36");
INSERT INTO fanfiction_comments VALUES ("3","1","360","Looks great!  ","2006-08-01 23:42:32");


# Dump of table fanfiction_favorites
# Dump DATE : 20-Apr-2020

INSERT INTO fanfiction_favorites VALUES ("1","1","ST","");
INSERT INTO fanfiction_favorites VALUES ("0","2559","ST","");
INSERT INTO fanfiction_favorites VALUES ("0","2277","ST","");
INSERT INTO fanfiction_favorites VALUES ("0","1386","ST","");
INSERT INTO fanfiction_favorites VALUES ("0","2331","ST","");
INSERT INTO fanfiction_favorites VALUES ("0","2540","ST","");
INSERT INTO fanfiction_favorites VALUES ("0","71","ST","");
INSERT INTO fanfiction_favorites VALUES ("0","72","ST","");
INSERT INTO fanfiction_favorites VALUES ("0","73","ST","");
INSERT INTO fanfiction_favorites VALUES ("0","2084","ST","");
INSERT INTO fanfiction_favorites VALUES ("0","2","AU","");
INSERT INTO fanfiction_favorites VALUES ("0","24","AU","");
INSERT INTO fanfiction_favorites VALUES ("2","2694","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","1961","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","3176","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","1881","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","248","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","342","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","2934","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","322","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","375","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","3525","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","2411","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","2414","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","2645","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","308","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","3540","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","1090","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","2442","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","2034","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","2697","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","3472","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","2868","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","3161","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","2795","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","2126","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","3308","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","236","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","2679","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","2791","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","746","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","2327","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","800","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","3491","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","2984","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","2285","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","588","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","3209","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","3467","ST","");
INSERT INTO fanfiction_favorites VALUES ("2","1926","ST","");




# Dump of table fanfiction_inseries
# Dump DATE : 20-Apr-2020

INSERT INTO fanfiction_inseries VALUES ("169","108","0","1","19");
INSERT INTO fanfiction_inseries VALUES ("118","838","0","1","2");
INSERT INTO fanfiction_inseries VALUES ("118","835","0","1","1");
INSERT INTO fanfiction_inseries VALUES ("224","3721","0","1","5");




# Dump of table fanfiction_log
# Dump DATE : 20-Apr-2020


# Dump of table fanfiction_messages
# Dump DATE : 20-Apr-2020

INSERT INTO fanfiction_messages VALUES ("1","copyright","Copyright Footer","<div align=\"center\" style= \"font-size: .8em\">\r\nThis site is powered by <a href=\"http://efiction.org/index.php\">eFiction 3.5.3</a>. Skin design by Moderator.");
INSERT INTO fanfiction_messages VALUES ("9","welcome","Welcome","Welcome to Efiction Test!");
INSERT INTO fanfiction_messages VALUES ("13","rules","EFiction Submission Rules","");
INSERT INTO fanfiction_messages VALUES ("14","tos","Terms of Service","");




# Dump of table fanfiction_modules
# Dump DATE : 20-Apr-2020


# Dump of table fanfiction_news
# Dump DATE : 20-Apr-2020

INSERT INTO fanfiction_news VALUES ("1","Moderator","New Archive Open for Business!","Welcome to the new Efiction Test archive!","2006-04-03 13:21:07","3");

# Dump of table fanfiction_pagelinks
# Dump DATE : 20-Apr-2020

INSERT INTO fanfiction_pagelinks VALUES ("1","home","Home",NULL,"index.php","0","0");
INSERT INTO fanfiction_pagelinks VALUES ("9","authors","Authors",NULL,"authors.php?list=authors","0","0");
INSERT INTO fanfiction_pagelinks VALUES ("12","series","Series",NULL,"browse.php?type=series","0","0");
INSERT INTO fanfiction_pagelinks VALUES ("15","contactus","Contact Us",NULL,"contact.php","0","0");


# Dump of table fanfiction_panels
# Dump DATE : 20-Apr-2020

INSERT INTO fanfiction_panels VALUES ("1","submitted","Submissions","","3","5","0","A");
INSERT INTO fanfiction_panels VALUES ("2","versioncheck","Version Check","","3","8","0","A");
INSERT INTO fanfiction_panels VALUES ("3","newstory","Add New Story","stories.php?action=newstory&admin=1","3","2","0","A");
INSERT INTO fanfiction_panels VALUES ("4","addseries","Add New Series","series.php?action=add","3","1","0","A");
INSERT INTO fanfiction_panels VALUES ("5","news","News","","3","4","0","A");
INSERT INTO fanfiction_panels VALUES ("6","featured","Featured Stories","","3","3","0","A");
INSERT INTO fanfiction_panels VALUES ("7","characters","Characters","","2","2","0","A");
INSERT INTO fanfiction_panels VALUES ("8","ratings","Ratings","","2","3","0","A");
INSERT INTO fanfiction_panels VALUES ("9","members","Members","","2","5","0","A");
INSERT INTO fanfiction_panels VALUES ("10","mailusers","Mail Users","","2","6","0","A");
INSERT INTO fanfiction_panels VALUES ("11","settings","Settings","","1","2","0","A");
INSERT INTO fanfiction_panels VALUES ("12","blocks","Blocks","","1","3","0","A");
INSERT INTO fanfiction_panels VALUES ("13","censor","Censor","","1","0","1","A");
INSERT INTO fanfiction_panels VALUES ("14","admins","Admins","","1","6","0","A");
INSERT INTO fanfiction_panels VALUES ("15","classifications","Classifications","","2","4","0","A");
INSERT INTO fanfiction_panels VALUES ("16","categories","Categories","","2","1","0","A");

# Dump of table fanfiction_ratings
# Dump DATE : 20-Apr-2020

INSERT INTO fanfiction_ratings VALUES ("1","All Ages","","");
INSERT INTO fanfiction_ratings VALUES ("2","Pre-Teen","","");
INSERT INTO fanfiction_ratings VALUES ("3","Teen","","");
INSERT INTO fanfiction_ratings VALUES ("4","Mature","","");
INSERT INTO fanfiction_ratings VALUES ("5","Adult","","");

# Dump of table fanfiction_reviews
# Dump DATE : 20-Apr-2020

INSERT INTO fanfiction_reviews VALUES ("1","54","117","Reviewer 3","3","Magical :)","2006-03-12 16:43:50","0","1","ST");
INSERT INTO fanfiction_reviews VALUES ("8","3","2120","Reviewer 1","7","Absolutely beautiful! ","2006-03-28 17:36:50","0","0","ST");
INSERT INTO fanfiction_reviews VALUES ("10","4","932","Reviewer 2","0","Awesome!!!  This was so much fun to read :)<br><br><i>Author\'s Response: Glad you liked it!</i>","2006-04-03 19:34:02","0","1","ST");
INSERT INTO fanfiction_reviews VALUES ("13","54","650","Reviewer 4","0","MUUUUUCH better than the actual episode. :-) Thanks!","2006-04-04 01:19:24","0","0","ST");
INSERT INTO fanfiction_reviews VALUES ("14","741","2087","Reviewer 1","316","More ! More!  ^___^","2006-04-04 03:09:28","0","0","ST");
INSERT INTO fanfiction_reviews VALUES ("15","741","2623","Reviewer 2","0","Oh. Ow. Wow! <br />","2006-04-04 05:55:36","0","1","ST");

# Dump of table fanfiction_series
# Dump DATE : 20-Apr-2020

INSERT INTO fanfiction_series VALUES ("118","Windows 1252","This series takes place several months after the episode Need and deals with the aftermath of certain events - how they have affected Bob and what happens to the friendship between Bill and Bob as a result of Bill discovering his \'secret\'.","5","0","1","3,7,10,13,26,30","0","Adult Themes","Angst,Character Study,Drama,Friendship,Smarm","2,1","1","","5");
INSERT INTO fanfiction_series VALUES ("169","Cakes","A challenge about cakes.","3","0","6","1,3,7,10,12,13,14,15,16,17,19,25","0","","Action/Adventure,Angst,Character Study,Drama,First Time,Friendship,Holiday,Humor,Hurt/Comfort,Jammies,Missing Scene/Episode-Related,Romance","2,5,1,11,9,13,3,4","7","","24");
INSERT INTO fanfiction_series VALUES ("224","Japanese series","Chapter is in Japanese anyway.","5","0","6","3,11,14,15,25","0","","Angst,Established Relationship,Holiday,Humor,Romance","2,1,3","4","","5");

# Dump of table fanfiction_settings
# Dump DATE : 20-Apr-2020

INSERT INTO fanfiction_settings VALUES ("VxDE9ij5nX","Efiction Test","A Testing Fan Fiction Archive","http://www.example.com","admin@example.com","","classicsg1","CSSZen","en","0","storiesef","files","0","1","0","0","1","200","300","0","2","0","<b><i><u><center><hr><p><br /><br><blockquote><ol><ul><li><img><strong><em><a>","1","1","0","1","0","0","1","d M Y","h:i a","127","1","20","0","0","0","1","2","5","1","0","0","2","0","1","1","1","1","","3.5.3","mail.test.com","agsender@example.com","!BillBob!");

# Dump of table fanfiction_stats
# Dump DATE : 20-Apr-2020
INSERT INTO fanfiction_stats VALUES ("VxDE9ij5nX","3835","4556","249","4505","23176094","378","1138","1684","1613");

# Dump of table fanfiction_stories
# Dump DATE : 20-Apr-2020

INSERT INTO fanfiction_stories VALUES ("1","Bacon ipsum","&nbsp;<p> &nbsp;</p>Meat-related text.",NULL,"1","3,10,16,26","2,1","3","2006-02-09 22:21:35","2006-02-09 22:21:35","2",NULL,"","1","1","","3992","0","2","2872","0");
INSERT INTO fanfiction_stories VALUES ("3","Lorem ipsum","Short, and no tricky characters.",NULL,"6","3,10,12,15,25","2,1,3,4","5","2006-03-04 13:00:45","2006-03-04 13:00:45","4",NULL,"","1","1","","8482","0","7","4615","0");
INSERT INTO fanfiction_stories VALUES ("4","Email story","Email-related story.",NULL,"6","15","2,1","3","2006-03-04 13:16:12","2006-03-04 13:16:12","4",NULL,"","1","1","","1625","0","1","2390","0");
INSERT INTO fanfiction_stories VALUES ("50","Cat-related ipsum","Meow all night chew iPad power cord.",NULL,"6","3,10,11,14","2,1","2","2006-03-05 17:12:16","2006-03-05 17:12:16","2",NULL,"","1","1","0","2135","0","1","5340","0");
INSERT INTO fanfiction_stories VALUES ("51","Cupcake ipsum","Biscuit candy cake candy macaroon. Soufflé marzipan croissant gummi bears. Wafer lollipop tart topping. Bonbon danish dragée lemon drops lemon drops caramels jelly. Tootsie roll chocolate cookie cake. Topping cheesecake lollipop halvah jujubes brownie bear claw. ",NULL,"6","3,10,11,16","2,1","3","2006-03-05 17:20:38","2006-03-05 17:20:38","2",NULL,"","1","1","0","4809","0","1","4474","0");
INSERT INTO fanfiction_stories VALUES ("54","Carl Sagan ipsum","Only shorter.",NULL,"6","11,16","2,1","3","2006-03-05 17:27:05","2006-03-05 17:27:05","2",NULL,"","1","1","0","2426","0","0","2018","0");
INSERT INTO fanfiction_stories VALUES ("108","A lot of cakes","Lots and lots of cakes.",NULL,"6","7,12,25","2,1,4","5","2006-03-06 15:42:57","2006-03-06 15:42:57","3",NULL,"","1","1","","13","0","0","2020","0");
INSERT INTO fanfiction_stories VALUES ("741","Actually a bookmark","This is a story containing only a link to another location.",NULL,"1","3,7,13,19","2,1","1","2006-03-17 15:26:36","2006-03-17 15:26:36","5",NULL,"","1","1","","12","0","0","2080","0");
INSERT INTO fanfiction_stories VALUES ("835","Windows 1252 Story","Eôs in ipsum ocûrrëret.",NULL,"1","3,7,13,19,30","2,1","3","2006-03-18 12:56:43","2006-03-18 12:56:43","5",NULL,"","1","1","0","12","0","0","2066","0");
INSERT INTO fanfiction_stories VALUES ("838","Another story in series","Things happen.",NULL,"1","3,7,13,19","2,1,14","3","2006-03-18 13:42:27","2006-03-18 13:42:27","5",NULL,"","1","1","","11","0","0","1310","0");
INSERT INTO fanfiction_stories VALUES ("3519","Beans and other vegetables","More vegetables.","Written for someone\'s birthday as a small thank you for all their hard work and dedication here on Efiction Test archive and the Testing Solutions website.  Moderator, you\'re a star!","6","3,7,12,25","2,1","4","2008-02-11 13:32:43","2008-02-11 13:33:02","3","1","0","1","1","0","12","0","1","3408","0");
INSERT INTO fanfiction_stories VALUES ("3721","Japanese","Database is Latin-1 and doesn\'t support Japanese text.","","6","37,1,2,3,7,10,11,14,15,16,25","2,5,1,9,14,3,4","4","2008-10-08 20:58:26","2008-10-08 20:58:29","5","1","1","1","1","0","9","0","2","3273","0");
INSERT INTO fanfiction_stories VALUES ("3745","Accented lorem ipsum","A nice little summary.","","27","2,3,13,16","2,1,3,4","3","2008-11-28 14:10:56","2008-11-28 14:10:59","2","1","0","1","1","0","33225","0","7","2303","0");
INSERT INTO fanfiction_stories VALUES ("3785","Zombies","Zombie-related lorem ipsum.","Some story notes about Zombies.","1","13,14,27","2,1,3,4","1","2008-12-27 07:18:06","2008-12-27 07:18:09","2","1","0","1","1","0","2828","0","1","3225","0");
INSERT INTO fanfiction_stories VALUES ("4035","Hipster ipsum","Bushwick man braid vaporware hot chicken yuccie snackwave cold-pressed +1 3 wolf moon.","Thanks to betas.","6","16","2,1,11,9,3,4","3","2010-01-03 10:04:12","2010-01-03 10:04:16","2","0","0","1","1","0","4849","0","2","2767","0");
