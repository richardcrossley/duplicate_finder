#!/usr/bin/env python3

import os
import sys
import hashlib

g_hash_name = 'sha256'


class CFile:
    def __init__(self):
        self._file_path = None
        self._digest = None

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        global g_hash_name
        self._file_path = file_path

        with open(self._file_path, 'rb') as f:
            m = hashlib.new(g_hash_name, f.read())

        f.close()
        self._digest = m.digest()
        
    @property
    def digest(self):
        return self._digest


class CDupFinder:
    def __init__(self):
        self._files_list = dict()

    def scan_directory(self, directory_path):
        for root_dir, dir_list, files_list in os.walk(directory_path):
            for file_path in files_list:
                abs_file_path = os.path.join(root_dir, file_path)

                if not os.path.islink(abs_file_path):
                    a_file = CFile()
                    a_file.file_path = abs_file_path

                    if a_file.digest in self._files_list.keys():
                        duplicate_files_list = self._files_list[a_file.digest]
                        duplicate_files_list.append(a_file.file_path)
                    else:
                        duplicate_files_list = list()
                        duplicate_files_list.append(a_file.file_path)
                        self._files_list[a_file.digest] = duplicate_files_list

    @property
    def duplicate_files_list_list(self):
        l_duplicate_files_list_list = list()

        for digest, duplicate_files_list in self._files_list.items():
            if len(duplicate_files_list) > 1:
                l_duplicate_files_list_list.append(duplicate_files_list)

        return l_duplicate_files_list_list


def show_help(script_path):
    print("Usage:")
    print("    " + script_path[script_path.rfind("/")+1:] + " [directory_name_1] [directory_name_2] ...")
    exit(1)


def main():
    dir_list = list()

    if len(sys.argv) == 1:
        dir_list.append(os.getcwd())
    else:
        for dir_name in sys.argv:
            if dir_name.lower() == '--help' or dir_name.lower == '-h':
                show_help(sys.argv[0])
            else:
                if os.path.isdir(dir_name):
                    dir_list.append(dir_name)
                else:
                    print(dir_name + " is not a directory.")

    dup_finder = CDupFinder()
    
    for dir_name in dir_list:
        dup_finder.scan_directory(dir_name)

    duplicate_files_list_list = dup_finder.duplicate_files_list_list

    if len(duplicate_files_list_list) == 0:
        print("There are no duplicate files.")
    else:
        for duplicate_file_list in duplicate_files_list_list:
            initial_file_path = duplicate_file_list[0]
            
            for duplicate_file_path in duplicate_file_list[1:]:
                print(initial_file_path + " - " + duplicate_file_path)


if __name__ == '__main__':
    main()
