#! /usr/bin/env python3
"""
Docblock
"""

# import built in modules

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


class URLs:

    def URL_list(self):
        return {
            "projects": {
                "all": "https://api.freeagent.com/v2/projects",
                "single": "https://api.freeagent.com/v2/projects/:id",
                "by_contact":
                    "https://api.freeagent.com/v2/projects?\
                    contact=https://api.freeagent.com/v2/contacts/2",
                "create": "https://api.freeagent.com/v2/projects",
                "update": "https://api.freeagent.com/v2/projects/:id",
                "delete": "https://api.freeagent.com/v2/projects/:id"
            },
            "tasks": {
                "all": "https://api.freeagent.com/v2/tasks?project=:project",
                "single": "https://api.freeagent.com/v2/tasks/:id",
                "create":
                    "https://api.freeagent.com/v2/tasks?project=:project",
                "update": "https://api.freeagent.com/v2/tasks/:id",
                "delete": "https://api.freeagent.com/v2/users/:id"
            },
            "contacts": {
                "all": "https://api.freeagent.com/v2/contacts",
                "all_with_filter":
                    "https://api.freeagent.com/v2/contacts?view=active",
                "single": "https://api.freeagent.com/v2/contacts/:id",
                "create": "https://api.freeagent.com/v2/contacts",
                "update": "https://api.freeagent.com/v2/contacts/:id",
                "delete": "https://api.freeagent.com/v2/contacts/:id"
            },
            "timeslips": {
                "all": "https://api.freeagent.com/v2/timeslips",
                "all_by_dates":
                    "https://api.freeagent.com/v2/timeslips?\
                    from_date=2012-01-01&to_date=2012-03-31",
                "all_by_user":
                    "https://api.freeagent.com/v2/timeslips?\
                    user=https://api.freeagent.com/v2/users/2",
                "all_by_task":
                    "https://api.freeagent.com/v2/timeslips?\
                    task=https://api.freeagent.com/v2/tasks/2",
                "all_by_project":
                    "https://api.freeagent.com/v2/timeslips?\
                    project=https://api.freeagent.com/v2/projects/2",
                "single": "https://api.freeagent.com/v2/timeslips/:id",
                "create": "https://api.freeagent.com/v2/timeslips",
                "update": "https://api.freeagent.com/v2/timeslips/:id",
                "delete": "https://api.freeagent.com/v2/timeslips/:id"
            }
        }
