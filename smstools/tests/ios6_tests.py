# -*- coding: utf-8 -*-
import unittest, sys, os, sqlite3, time
##include smstools/ directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import core, ios6, core_tests

class IOS6Tests(core_tests.BaseTests):

    def setUp(self):
        self.db = self.get_empty_db_in_memory(ios6)


    def test_write_parse(self):
        true_texts = core.getTestTexts()
        cursor = self.db.cursor()

        ios6.IOS6().write_cursor(true_texts, cursor)
        parsed_texts = ios6.IOS6().parse_cursor(cursor)

        for i in range(len(true_texts)):
            self.assertTextsEqual(true_texts[i], parsed_texts[i])

    def test_something(self):
        files = self.get_test_db_files(for_parser=ios6.IOS6)
        for file in files:
            print file


if __name__ == '__main__':
    unittest.main()
