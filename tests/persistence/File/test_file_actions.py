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

    def setup_class(self):
        ts = str(time.time()).split('.')[0]
        print(TaskFile().base_dir)
        self.test_path = TaskFile().base_dir + 'stubs/' + ts + '.txt'

    def test_we_can_create_a_file(self):
        f = TaskFile()
        f.create(self.test_path)
        assert(path.isfile(self.test_path) is True, "File does not exist")
        os.remove(self.test_path)

    def test_we_can_write_to_a_file(self):
        f = TaskFile()
        f.write(self.test_path, 'Hello World!')
        handler = open(self.test_path, 'r')
        assert("Hello World!" in handler.read(),
               "Hello World! was not found in the file contents")
        os.remove(self.test_path)

    def test_we_can_update_a_file(self):
        f = TaskFile()
        f.write(self.test_path, 'Hello World!')
        f.update(self.test_path, '...Yes, Hello World!')
        handler = open(self.test_path, 'r')
        assert("Hello World!...Yes, Hello World" in handler.read(),
               "Updated text was not found in the file contents")
        os.remove(self.test_path)

    def test_we_can_delete_a_file(self):
        f = TaskFile()
        f.create(self.test_path)
        assert (path.isfile(self.test_path) is True, "File was not created")
        f = TaskFile()
        f.delete(self.test_path)
        assert (path.isfile(self.test_path) is False, "File was not deleted")
