#! /usr/bin/env python3
"""
Tests for the project class
"""

# import built in modules
import pytest
import os

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
        print(Config().paths()["base"] + "stubs/Project")
        self.project_path = Config().paths()["base"] + "stubs/Project"

    def test_the_project_is_instantiated_with_its_name(self):
        assert \
            Project("Test Project Name").project_name == "Test Project Name", \
            "Project name is not being set on project instantiation"

    def test_we_can_create_the_project_directory(self):
        os.removedirs(self.project_path)
        project = Project("Test Project Name")
        project.create_project_directory()
        assert os.path.isdir(self.project_path) is True, \
            "Project directory was not created"

    # Todo: Create a "Project already exists exception
    def test_we_throw_an_exception_if_the_directory_exists(self):
        with pytest.raises(FileExistsError):
            project = Project("Test Project Name")
            project.create_project_directory()
