#! /usr/bin/env python3
"""
Docblock
"""

# import built in modules

# import Third party

# import local
from DualTimer.Src.Config.App import App as Config

__author__ = "John Evans <john@grandadevans.com?"
__copyright__ = "Copyright 2015, John Evans"
__credits__ = ["John Evans <john@grandadevans.com>"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "John Evans"
__email__ = "john@grandadevans.com"
__status__ = "Development"


class TestAppConfig:

    def test_base_directory_set(self):
        dir_ = Config().config()["base_dir"]
        print(dir_)
        assert len(dir_) is not 0,\
            "Base Directory is not set in config"
