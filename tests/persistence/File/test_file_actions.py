#! /usr/bin/env python3
"""
Test file to test all the file persistent implementations
"""

import pytest
import io
import os
import time

from os import path

# import Third party

# import local
from ....src.persistence.file.TaskFile import TaskFile

__author__ = "John Evans <john@grandadevans.com?"
__copyright__ = "Copyright 2015, John Evans"
__credits__ = ["John Evans <john@grandadevans.com>"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "John Evans"
__email__ = "john@grandadevans.com"
__status__ = "Development"


class TestFileActions:

    def test_we_can_create_a_file(self):
        ts = str(time.time()).split('.')[0]
        f = TaskFile()
        test_path = TaskFile().base_dir + 'stubs/' + ts + '.txt'
        f.create(test_path)
        assert(path.isfile(test_path) is True)

        os.remove(test_path)

    def test_we_can_write_to_a_file(self):
        ts = str(time.time()).split('.')[0]
        test_path = TaskFile().base_dir + 'stubs/' + ts + '.txt'
        f = TaskFile()
        f.write(test_path, 'Hello World!')

        handler = open(test_path, 'r')
        print(handler)
        assert("Hello World!" in handler.read())
        os.remove(test_path)

    def test_we_can_update_a_file(self):
        ts = str(time.time()).split('.')[0]
        test_path = TaskFile().base_dir + 'stubs/' + ts + '.txt'
        f = TaskFile()
        f.write(test_path, 'Hello World!')

        ts = str(time.time()).split('.')[0]
        test_path = TaskFile().base_dir + 'stubs/' + ts + '.txt'
        f = TaskFile()
        f.update(test_path, '...Yes, Hello World!')

        handler = open(test_path, 'r')
        print(handler)
        assert("Hello World!...Yes, Hello World" in handler.read())
        os.remove(test_path)

    def test_we_can_delete_a_file(self):
        ts = str(time.time()).split('.')[0]
        f = TaskFile()
        test_path = TaskFile().base_dir + 'stubs/' + ts + '.txt'
        f.create(test_path)
        assert (path.isfile(test_path) is True)

        f = TaskFile()
        f.delete(test_path)
        assert (path.isfile(test_path) is False)
