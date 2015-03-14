#! /usr/bin/env python3
"""
Config values for the app
"""

# import built in modules
import os

# import Third party

# import local

__author__ = "John Evans <john@grandadevans.com?"
__copyright__ = "Copyright 2015, John Evans"
__credits__ = ["John Evans <john@grandadevans.com>"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "John Evans"
__email__ = "john@grandadevans.com"
__status__ = "Development"


class App:

    def paths(self):
        return {
            "base": os.path.dirname(__file__) + "/../../"
        }
