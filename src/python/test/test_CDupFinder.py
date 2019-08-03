from unittest import TestCase
import os.path as path

from dupfinder import CDupFinder


class TestCDupFinder(TestCase):
    def test_duplicate_files_list_list(self):
        expected_num_duplicate_lists = 1
        expected_num_duplicates = 4
        expected_duplicate_file_list = list()
        test_directory = path.join(path.dirname(path.realpath(__file__)), 'resources')
        expected_duplicate_file_list.append(path.join(test_directory, 'file_1.txt'))
        expected_duplicate_file_list.append(path.join(test_directory, 'file_2.txt'))
        expected_duplicate_file_list.append(path.join(test_directory, 'sub_dir', 'file_4.txt'))
        expected_duplicate_file_list.append(path.join(test_directory, 'sub_dir', 'file_5.txt'))

        test_dup_finder = CDupFinder()
        test_dup_finder.scan_directory(test_directory)
        test_duplicate_list = test_dup_finder.duplicate_files_list_list[0]

        self.assertEqual(expected_num_duplicate_lists, len(test_dup_finder.duplicate_files_list_list))
        self.assertEqual(expected_num_duplicates, len(test_duplicate_list))

        for file_name in expected_duplicate_file_list:
            self.assertTrue(file_name in test_duplicate_list)
