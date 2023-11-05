import datetime
from unittest import TestCase

from efiction.tests.test_utils import load_fixtures, create_efiction_converter
from opendoors.utils import remove_output_files


class TestEFictionConverter(TestCase):
    # Set up full test database with tables we don't use and "normal", foreign key (id-based) ratings
    efiction_converter = create_efiction_converter("efiction")

    # Before and after steps and utility methods
    def setUp(self) -> None:
        """ Load test data and create the Open Doors tables for the normal eFiction tests """
        load_fixtures(self.efiction_converter.config, self.efiction_converter.sql)
        self.efiction_converter.create_open_doors_db("test_path")

    def tearDown(self) -> None:
        """ Remove files created during the tests """
        remove_output_files('efiction/tests/test_output')
        remove_output_files('test_path')

    # Tests
    def test_for_coauthor_none(self):
        """ Test checking for coauthors where no coauthors are present """
        fake_story = {"id": 2}
        assert not self.efiction_converter.fetch_coauthors(fake_story)

    def test_for_coauthor_existing(self):
        """ Test checking for coauthor where there is a coauthor """
        # Assert list > 0
        fake_story = {"id": 1}
        assert self.efiction_converter.fetch_coauthors(fake_story)

    def test_convert_authors(self):
        old_authors = [
            {'uid': 1, 'penname': 'Author1', 'realname': 'Author1', 'email': 'A1@example.com', 'website': '', 'bio': '',
             'image': '', 'date': datetime.datetime(2006, 1, 6, 1, 2, 13), 'admincreated': '0', 'password': 'xfghtu'},
            {'uid': 2, 'penname': 'B Author 2', 'realname': 'B Author 2', 'email': 'B2@example.com', 'website': '',
             'bio': '', 'image': 'bauthor2', 'date': datetime.datetime(2006, 2, 9, 1, 37, 24), 'admincreated': '1',
             'password': 'xfghtu'},
            {'uid': 3, 'penname': 'C Author 3', 'realname': 'C Author 3', 'email': 'C3@example.com',
             'website': 'http://example.com', 'bio': 'An author bio with some text in it', 'image': '',
             'date': datetime.datetime(2006, 2, 16, 22, 58, 2), 'admincreated': '1', 'password': 'xfghtu'},
            {'uid': 4, 'penname': 'D Author 4', 'realname': 'D Author 4', 'email': 'D4@example.com', 'website': '',
             'bio': '', 'image': '', 'date': datetime.datetime(2006, 2, 15, 23, 0), 'admincreated': '1',
             'password': 'xfghtu'},
            {'uid': 5, 'penname': 'E Author 5', 'realname': 'E Author 5', 'email': 'E5@example.com',
             'website': 'www.example.com', 'bio': '', 'image': 'eauthor5',
             'date': datetime.datetime(2006, 2, 16, 23, 0), 'admincreated': '1', 'password': 'xfghtu'}]
        authors = self.efiction_converter._convert_authors(old_authors)
        self.assertEqual(5, len(authors), "there should be 5 authors")

    def test_convert_characters(self):
        old_characters = [{'charid': 1, 'catid': -1, 'charname': "Bill O'Connell", 'bio': '', 'image': ''},
                          {'charid': 2, 'catid': -1, 'charname': 'Bob Billson', 'bio': '', 'image': ''},
                          {'charid': 3, 'catid': -1, 'charname': 'Fatima Habibi', 'bio': '', 'image': ''},
                          {'charid': 4, 'catid': -1, 'charname': 'Václav', 'bio': '', 'image': ''},
                          {'charid': 5, 'catid': -1, 'charname': 'Spyros Papadopoulos', 'bio': '', 'image': ''},
                          {'charid': 6, 'catid': -1, 'charname': 'Olu Adebayo', 'bio': '', 'image': ''},
                          {'charid': 7, 'catid': -1, 'charname': 'Samia Ben Abdel', 'bio': '', 'image': ''},
                          {'charid': 8, 'catid': -1, 'charname': 'Einar Rønquist', 'bio': '', 'image': ''},
                          {'charid': 9, 'catid': -1, 'charname': 'Aisha Johnson', 'bio': '', 'image': ''},
                          {'charid': 10, 'catid': -1, 'charname': 'Mikhael Antonov', 'bio': '', 'image': ''},
                          {'charid': 11, 'catid': -1, 'charname': 'Liam Habibi', 'bio': '', 'image': ''},
                          {'charid': 12, 'catid': -1, 'charname': 'Bernard', 'bio': '', 'image': ''},
                          {'charid': 13, 'catid': -1, 'charname': 'Vincent Corentin', 'bio': '', 'image': ''},
                          {'charid': 14, 'catid': -1, 'charname': 'Other', 'bio': '', 'image': ''}]
        characters = self.efiction_converter._convert_characters(old_characters)
        self.assertEqual(14, len(characters), "there should be 14 characters")

    def test_convert_story_tags_normal_ratings(self):
        """
        Check that the test data in efiction.sql is correctly converted, including the "normal" (foreign key) ratings.
        """
        self.efiction_converter.convert_all_tags()
        old_stories = [
            {'sid': 1, 'title': 'Bacon ipsum', 'summary': '&nbsp;<p> &nbsp;</p>Meat-related text.', 'storynotes': None,
             'catid': '1', 'classes': '3,10,16,26', 'charid': '2,1', 'rid': '3',
             'date': datetime.datetime(2006, 2, 9, 22, 21, 35), 'updated': datetime.datetime(2006, 2, 9, 22, 21, 35),
             'uid': 2, 'coauthors': None, 'featured': '', 'validated': '1', 'completed': '1', 'rr': '',
             'wordcount': 3992, 'rating': 0, 'reviews': 2, 'count': 2872, 'challenges': '0'}]
        result = self.efiction_converter._convert_story_tags(old_stories[0])
        self.assertEqual({
            'categories': [6],
            'characters': [106, 107],
            'classes': [70, 77, 83, 94],
            'rating': [3]
        }, result)

    def test_convert_story_tags_string_ratings(self):
        """
        Check that the test data in efiction_string_ratings.sql is correctly converted, including the "normal" (foreign
        key) ratings.
        """
        # Set up test data with string ratings
        efiction_converter_string_ratings = create_efiction_converter("efiction_string_ratings")
        # Create databases for this test
        load_fixtures(efiction_converter_string_ratings.config, efiction_converter_string_ratings.sql)
        efiction_converter_string_ratings.create_open_doors_db("test_path")

        # Now convert the tags and set ratings_nonstandard
        efiction_converter_string_ratings.convert_all_tags()
        old_stories = [
            {'sid': 1, 'title': 'Bacon ipsum', 'summary': '&nbsp;<p> &nbsp;</p>Meat-related text.', 'storynotes': None,
             'catid': '1', 'classes': '3,10,16,26', 'charid': '2,1', 'rid': 'Teen',
             'date': datetime.datetime(2006, 2, 9, 22, 21, 35), 'updated': datetime.datetime(2006, 2, 9, 22, 21, 35),
             'uid': 2, 'coauthors': None, 'featured': '', 'validated': '1', 'completed': '1', 'rr': '',
             'wordcount': 3992, 'rating': 0, 'reviews': 2, 'count': 2872, 'challenges': '0'}]
        result = efiction_converter_string_ratings._convert_story_tags(old_stories[0])
        self.assertEqual({'categories': [6], 'characters': [8], 'classes': [], 'rating': [3]}, result)
        # Remove test files created during this test
        remove_output_files('efiction/tests/test_output')

    def test_convert_stories(self):
        self.efiction_converter.convert_all_tags()
        result = self.efiction_converter.convert_stories('de')
        self.assertEqual(15, len(result))
        self.assertEqual(
            {'ao3_url': None,
             'categories': None,
             'characters': '',
             'date': datetime.datetime(2006, 2, 9, 22, 21, 35),
             'do_not_import': 0,
             'fandoms': '',
             'id': 1,
             'import_notes': '',
             'imported': 0,
             'notes': '',
             'rating': None,
             'relationships': '',
             'summary': '<p>  </p>Meat-related text.',
             'tags': '',
             'title': 'Bacon ipsum',
             'updated': datetime.datetime(2006, 2, 9, 22, 21, 35),
             'language_code': 'de',
             'url': None,
             'warnings': ''}, result[0], "Entities should be unencoded and leading and trailing spaces stripped")
        self.assertEqual(
            [{'ao3_url': None,
              'categories': None,
              'characters': '',
              'date': datetime.datetime(2006, 3, 4, 13, 0, 45),
              'do_not_import': 0,
              'fandoms': '',
              'id': 3,
              'import_notes': '',
              'imported': 0,
              'notes': '',
              'rating': None,
              'relationships': '',
              'summary': 'Short, and no tricky characters.',
              'tags': '',
              'title': 'Lorem ipsum',
              'updated': datetime.datetime(2006, 3, 4, 13, 0, 45),
              'language_code': 'de',
              'url': None,
              'warnings': ''},
             {'ao3_url': None,
              'categories': None,
              'characters': '',
              'date': datetime.datetime(2006, 3, 4, 13, 16, 12),
              'do_not_import': 0,
              'fandoms': '',
              'id': 4,
              'import_notes': '',
              'imported': 0,
              'notes': '',
              'rating': None,
              'relationships': '',
              'summary': 'Email-related story.',
              'tags': '',
              'title': 'Email story',
              'updated': datetime.datetime(2006, 3, 4, 13, 16, 12),
              'language_code': 'de',
              'url': None,
              'warnings': ''},
             {'ao3_url': None,
              'categories': None,
              'characters': '',
              'date': datetime.datetime(2006, 3, 5, 17, 12, 16),
              'do_not_import': 0,
              'fandoms': '',
              'id': 50,
              'import_notes': '',
              'imported': 0,
              'notes': '',
              'rating': None,
              'relationships': '',
              'summary': 'Meow all night chew iPad power cord.',
              'tags': '',
              'title': 'Cat-related ipsum',
              'updated': datetime.datetime(2006, 3, 5, 17, 12, 16),
              'language_code': 'de',
              'url': None,
              'warnings': ''}], result[1:4])
        self.assertEqual(
            [{'ao3_url': None,
              'categories': None,
              'characters': '',
              'date': datetime.datetime(2006, 3, 5, 17, 20, 38),
              'do_not_import': 0,
              'fandoms': '',
              'id': 51,
              'import_notes': '',
              'imported': 0,
              'notes': '',
              'rating': None,
              'relationships': '',
              'summary': 'Biscuit candy cake candy macaroon. Soufflé marzipan croissant '
                         'gummi bears. Wafer lollipop tart topping. Bonbon danish dragée '
                         'lemon drops lemon drops caramels jelly. Tootsie roll chocolate '
                         'cookie cake. Topping cheesecake lollipop halvah jujubes brownie '
                         'bear claw.',
              'tags': '',
              'title': 'Cupcake ipsum',
              'updated': datetime.datetime(2006, 3, 5, 17, 20, 38),
              'language_code': 'de',
              'url': None,
              'warnings': ''},
             {'ao3_url': None,
              'categories': None,
              'characters': '',
              'date': datetime.datetime(2006, 3, 18, 12, 56, 43),
              'do_not_import': 0,
              'fandoms': '',
              'id': 835,
              'import_notes': '',
              'imported': 0,
              'notes': '',
              'rating': None,
              'relationships': '',
              'summary': 'Eôs in ipsum ocûrrëret.',
              'tags': '',
              'title': 'Windows 1252 Story',
              'updated': datetime.datetime(2006, 3, 18, 12, 56, 43),
              'language_code': 'de',
              'url': None,
              'warnings': ''}], [result[4], result[8]], "Unicode characters should be normalized")
        self.assertEqual(
            [{'ao3_url': None,
              'categories': None,
              'characters': '',
              'date': datetime.datetime(2006, 3, 5, 17, 27, 5),
              'do_not_import': 0,
              'fandoms': '',
              'id': 54,
              'import_notes': '',
              'imported': 0,
              'notes': '',
              'rating': None,
              'relationships': '',
              'summary': 'Only shorter.',
              'tags': '',
              'title': 'Carl Sagan ipsum',
              'updated': datetime.datetime(2006, 3, 5, 17, 27, 5),
              'language_code': 'de',
              'url': None,
              'warnings': ''},
             {'ao3_url': None,
              'categories': None,
              'characters': '',
              'date': datetime.datetime(2006, 3, 6, 15, 42, 57),
              'do_not_import': 0,
              'fandoms': '',
              'id': 108,
              'import_notes': '',
              'imported': 0,
              'notes': '',
              'rating': None,
              'relationships': '',
              'summary': 'Lots and lots of cakes.',
              'tags': '',
              'title': 'A lot of cakes',
              'updated': datetime.datetime(2006, 3, 6, 15, 42, 57),
              'language_code': 'de',
              'url': None,
              'warnings': ''},
             {'ao3_url': None,
              'categories': None,
              'characters': '',
              'date': datetime.datetime(2006, 3, 17, 15, 26, 36),
              'do_not_import': 0,
              'fandoms': '',
              'id': 741,
              'import_notes': '',
              'imported': 0,
              'notes': '',
              'rating': None,
              'relationships': '',
              'summary': 'This is a story containing only a link to another location.',
              'tags': '',
              'title': 'Actually a bookmark',
              'updated': datetime.datetime(2006, 3, 17, 15, 26, 36),
              'language_code': 'de',
              'url': None,
              'warnings': ''}], result[5:8])
        self.assertEqual(
            [{'ao3_url': None,
              'categories': None,
              'characters': '',
              'date': datetime.datetime(2006, 3, 18, 13, 42, 27),
              'do_not_import': 0,
              'fandoms': '',
              'id': 838,
              'import_notes': '',
              'imported': 0,
              'notes': '',
              'rating': None,
              'relationships': '',
              'summary': 'Things happen.',
              'tags': '',
              'title': 'Another story in series',
              'updated': datetime.datetime(2006, 3, 18, 13, 42, 27),
              'language_code': 'de',
              'url': None,
              'warnings': ''},
             {'ao3_url': None,
              'categories': None,
              'characters': '',
              'date': datetime.datetime(2008, 2, 11, 13, 32, 43),
              'do_not_import': 0,
              'fandoms': '',
              'id': 3519,
              'import_notes': '',
              'imported': 0,
              'notes': "Written for someone's birthday as a small thank you for all their "
                       'hard work and dedication here on Efiction Test archive and the '
                       "Testing Solutions website.  Moderator, you're a star!",
              'rating': None,
              'relationships': '',
              'summary': 'More vegetables.',
              'tags': '',
              'title': 'Beans and other vegetables',
              'updated': datetime.datetime(2008, 2, 11, 13, 33, 2),
              'language_code': 'de',
              'url': None,
              'warnings': ''},
             {'ao3_url': None,
              'categories': None,
              'characters': '',
              'date': datetime.datetime(2008, 10, 8, 20, 58, 26),
              'do_not_import': 0,
              'fandoms': '',
              'id': 3721,
              'import_notes': '',
              'imported': 0,
              'notes': '',
              'rating': None,
              'relationships': '',
              'summary': "Database is Latin-1 and doesn't support Japanese text.",
              'tags': '',
              'title': 'Japanese',
              'updated': datetime.datetime(2008, 10, 8, 20, 58, 29),
              'language_code': 'de',
              'url': None,
              'warnings': ''},
             {'ao3_url': None,
              'categories': None,
              'characters': '',
              'date': datetime.datetime(2008, 11, 28, 14, 10, 56),
              'do_not_import': 0,
              'fandoms': '',
              'id': 3745,
              'import_notes': '',
              'imported': 0,
              'notes': '',
              'rating': None,
              'relationships': '',
              'summary': 'A nice little summary.',
              'tags': '',
              'title': 'Accented lorem ipsum',
              'updated': datetime.datetime(2008, 11, 28, 14, 10, 59),
              'language_code': 'de',
              'url': None,
              'warnings': ''},
             {'ao3_url': None,
              'categories': None,
              'characters': '',
              'date': datetime.datetime(2008, 12, 27, 7, 18, 6),
              'do_not_import': 0,
              'fandoms': '',
              'id': 3785,
              'import_notes': '',
              'imported': 0,
              'notes': 'Some story notes about Zombies.',
              'rating': None,
              'relationships': '',
              'summary': 'Zombie-related lorem ipsum.',
              'tags': '',
              'title': 'Zombies',
              'updated': datetime.datetime(2008, 12, 27, 7, 18, 9),
              'language_code': 'de',
              'url': None,
              'warnings': ''},
             {'ao3_url': None,
              'categories': None,
              'characters': '',
              'date': datetime.datetime(2010, 1, 3, 10, 4, 12),
              'do_not_import': 0,
              'fandoms': '',
              'id': 4035,
              'import_notes': '',
              'imported': 0,
              'notes': 'Thanks to betas.',
              'rating': None,
              'relationships': '',
              'summary': 'Bushwick man braid vaporware hot chicken yuccie snackwave '
                         'cold-pressed +1 3 wolf moon.',
              'tags': '',
              'title': 'Hipster ipsum',
              'updated': datetime.datetime(2010, 1, 3, 10, 4, 16),
              'language_code': 'de',
              'url': None,
              'warnings': ''}],
            result[9:])
