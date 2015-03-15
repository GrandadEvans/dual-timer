#! /usr/bin/env python3
"""
Tests for the project class
"""

# import built in modules
import pytest

# import Third party

# import local
from DualTimer.Src.Project.Project import Project

__author__ = "John Evans <john@grandadevans.com?"
__copyright__ = "Copyright 2015, John Evans"
__credits__ = ["John Evans <john@grandadevans.com>"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "John Evans"
__email__ = "john@grandadevans.com"
__status__ = "Development"


class TestProject:

    def setup_class(self):
        pass

    def test_the_project_is_instantiated_with_its_name(self):
        assert \
            Project("Test Project Name").project_name == "Test Project Name", \
            "Project name is not being set on project instantiation"
