#! /usr/bin/env python3
"""
Tests for the project class
"""

# import built in modules
import pytest
import os
import json

# import Third party

# import local
from DualTimer.Src.Project.Project import Project
from DualTimer.Src.Config.App import App as Config

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
        self.project_path = Config().paths()["base"] + "stubs/Project/"
        self.project_info_file = self.project_path + "project.json"

    @pytest.fixture
    def clear_old_files(self):
        if os.path.isfile(self.project_info_file) is True:
            os.remove(self.project_info_file)
        if os.path.isdir(self.project_path) is True:
            os.removedirs(self.project_path)

    def test_the_project_is_instantiated_with_its_name(self):
        assert \
            Project("Test Project Name").project_name == "Test Project Name", \
            "Project name is not being set on project instantiation"

    def test_we_can_create_the_project_directory(self, clear_old_files):
        clear_old_files
        project = Project("Test Project Name")
        project.create_project_directory()
        assert os.path.isdir(self.project_path) is True, \
            "Project directory was not created"

    # Todo: Create a "Project already exists exception
    def test_we_throw_an_exception_if_the_directory_exists(self):
        with pytest.raises(Exception):
            project = Project("Test Project Name")
            project.create_project_directory()

    def test_we_create_a_project_file(self, clear_old_files):
        clear_old_files
        project = Project("Test Project Name")
        project.create_project_directory()
        project.create_project_info_file()

        assert os.path.isfile(self.project_info_file) \
            is True, "Project info file is not found"

    def test_the_project_info_file_holds_the_right_info(self, clear_old_files):
        clear_old_files
        project = Project("Test Project Name")
        project.create_project_directory()
        project.create_project_info_file()
        project.create_the_project_info()
        fp = open(self.project_info_file)
        info = json.loads(fp.read())
        """
        Asserts are below as separate asserts and not asserting a full list
        etc as I don't care about the format it is stored in I just want
        to make sure that the correct information is returned
        """
        assert info["name"] == "Test Project Name"
        assert info["start_date"] is None
        assert info["end_date"] is None
        assert info["end_date_type"] is None
        assert info["contacts"] == []
        assert info["billing"]["billable"] is True
        assert info["billing"]["billable_unit"] == "hours"
        assert info["billing"]["billable_rate"] == 0.00
        assert info["billing"]["currency"] == "GBP"
        assert info["budget"]["unit"] == "hours"
        assert info["budget"]["value"] == 0
