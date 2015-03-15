#! /usr/bin/env python3
"""
Tests to make sure that we have non empty URLS for the Freeagent API calls
"""

from DualTimer.Src.Freeagent.URLs import URLs


class TestFreeagentURLs:

    def setup_class(self):
        self.all = URLs().URL_list()

    def test_we_have_non_empty_project_entries(self):
        assert 'https://api.Freeagent.com' in self.all['projects']['all']
        assert 'https://api.Freeagent.com' in self.all['projects']['single']
        assert 'https://api.Freeagent.com' in \
               self.all['projects']['by_contact']
        assert 'https://api.Freeagent.com' in self.all['projects']['create']
        assert 'https://api.Freeagent.com' in self.all['projects']['update']
        assert 'https://api.Freeagent.com' in self.all['projects']['delete']

    def test_we_have_non_empty_task_entries(self):
        assert 'https://api.Freeagent.com' in self.all['tasks']['all']
        assert 'https://api.Freeagent.com' in self.all['tasks']['single']
        assert 'https://api.Freeagent.com' in self.all['tasks']['create']
        assert 'https://api.Freeagent.com' in self.all['tasks']['update']
        assert 'https://api.Freeagent.com' in self.all['tasks']['delete']

    def test_we_have_non_empty_contact_entries(self):
        assert 'https://api.Freeagent.com' in self.all['contacts']['all']
        assert 'https://api.Freeagent.com' in \
               self.all['contacts']['all_with_filter']
        assert 'https://api.Freeagent.com' in self.all['contacts']['single']
        assert 'https://api.Freeagent.com' in self.all['contacts']['create']
        assert 'https://api.Freeagent.com' in self.all['contacts']['update']
        assert 'https://api.Freeagent.com' in self.all['contacts']['delete']

    def test_we_have_none_empty_timeslip_entries(self):
        assert 'https://api.Freeagent.com' in self.all['timeslips']['all']
        assert 'https://api.Freeagent.com' in \
               self.all['timeslips']['all_by_dates']
        assert 'https://api.Freeagent.com' in \
               self.all['timeslips']['all_by_user']
        assert 'https://api.Freeagent.com' in \
               self.all['timeslips']['all_by_task']
        assert 'https://api.Freeagent.com' in \
               self.all['timeslips']['all_by_project']
        assert 'https://api.Freeagent.com' in self.all['timeslips']['single']
        assert 'https://api.Freeagent.com' in self.all['timeslips']['create']
        assert 'https://api.Freeagent.com' in self.all['timeslips']['update']
        assert 'https://api.Freeagent.com' in self.all['timeslips']['delete']
