from unittest import TestCase, main

from lazysplit import lazysplit


class LazysplitTestCase(TestCase):

    def test__lazysplit__on_default__splits_by_consecutive_whitespace(self):

        # Arrange
        strings = [
            "ala ma kota",
            "different  \twhitespace\n combinations",
            "some\u2007exotic\u2028Unicode\u2003whitespace\u1680characters"
        ]

        # Act and assert
        for string in strings:
            with self.subTest(string=string):
                self.assertEqual(string.split(), list(lazysplit(string)))


    def test__lazysplit__on_default__removes_leading_and_trailing_whitespace(self):

        # Arrange
        string = "   not much here\r\n"

        # Act and assert
        self.assertEqual(string.split(), list(lazysplit(string)))


    def test__lazysplit__on_sep_given__splits_by_given_sep(self):

        # Arrange
        string = '1<>2<>3'

        # Act and assert
        self.assertEqual(string.split('<>'), list(lazysplit(string, '<>')))


    def test__lazysplit__on_sep_given__leading_and_trailing_sep_delimits_empty_string(self):
        
        # Arrange
        string = '<>1<>2<>3<>'

        # Act and assert
        self.assertEqual(string.split('<>'), list(lazysplit(string, '<>')))


    def test__lazysplit__consecutive_seps_in_string__delimit_empty_string(self):
        
        # Arrange
        from collections import namedtuple

        StringAndSep = namedtuple('StringAndSep', 'string,sep')

        strings = [
            StringAndSep('1<><>2', '<>'),
            StringAndSep('1;;;;2', ';;'),
        ]

        # Act and assert
        for string, sep in strings:
            with self.subTest(string=string, sep=sep):
                self.assertEqual(
                        string.split(sep), 
                        list(lazysplit(string, sep)))


    def test__lazysplit__on_maxsplit_given__max_maxsplit_splits_are_done(self):

        # Arrange
        # Trailing whitespace is left untouched if split ends earlier due to 
        # maxsplit.
        strings = [
            ('1.2.3.4.5   ', '.'), 
            ('a  b\nc', None),
        ]
        maxsplits = [-10, 0, 1, 3, 10]

        # Act and assert
        for string, sep in strings:
            for maxsplit in maxsplits:
                with self.subTest(string=string, sep=sep, maxsplit=maxsplit):
                    self.assertEqual(
                            string.split(sep, maxsplit), 
                            list(lazysplit(string, sep, maxsplit)))


    def test__lazysplit__on_empty_sep__raises_exception(self):

        # Act and assert
        with self.assertRaises(ValueError, msg='Empty separator'):
            list(lazysplit('a;b;c;', ''))


    def test__lazy_split__sep_not_str__raises_exception(self):

        # Act and assert
        with self.assertRaises(
                TypeError, msg="Can't convert 'int' object ot str implicitly"):
            list(lazysplit('a;b;c;', 1))


if __name__ == '__main__':
    main()
