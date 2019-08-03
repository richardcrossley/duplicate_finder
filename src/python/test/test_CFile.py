from unittest import TestCase
import os.path as path

from dupfinder import CFile


def create_cfile():
    file = CFile()
    file.file_path = path.join(path.dirname(path.realpath(__file__)), 'resources', 'file_1.txt')
    return file


class TestCFile(TestCase):
    def test_file_path_setter(self):
        expected_file_path = path.join(path.dirname(path.realpath(__file__)), 'resources', 'file_1.txt')
        test_file = create_cfile()
        self.assertEqual(expected_file_path, test_file.file_path)

    def test_digest(self):
        # Digest generated from sha256sum resources/file_1.txt
        expected_digest = bytearray(b'\x69\x97\x33\xa2\x2a\xf6\x3e\x4a\xe4\xbd\x67\x4d\x8d\x61\x5f\x25\x4a\xa1\xd1\x81\x8b\x6d\xb4\x94\xc7\xd4\x1b\xbf\x68\x16\xec\xd1')
        test_file = create_cfile()
        self.assertEqual(expected_digest, test_file.digest)
