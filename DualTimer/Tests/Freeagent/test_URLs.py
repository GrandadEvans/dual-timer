#! /usr/bin/env python3
"""
Tests to make sure that we have non empty URLS for the Freeagent API calls
"""

from DualTimer.Src.Freeagent.URLs import URLs


class TestFreeagentURLs:

    def test_we_have_non_empty_project_entries(self):
        ob = URLs().URL_list()
        assert 'https://api.Freeagent.com' in ob['projects']['all']
        assert 'https://api.Freeagent.com' in ob['projects']['single']
        assert 'https://api.Freeagent.com' in ob['projects']['by_contact']
        assert 'https://api.Freeagent.com' in ob['projects']['create']
        assert 'https://api.Freeagent.com' in ob['projects']['update']
        assert 'https://api.Freeagent.com' in ob['projects']['delete']

    def test_we_have_non_empty_task_entries(self):
        ob = URLs().URL_list()
        assert 'https://api.Freeagent.com' in ob['tasks']['all']
        assert 'https://api.Freeagent.com' in ob['tasks']['single']
        assert 'https://api.Freeagent.com' in ob['tasks']['create']
        assert 'https://api.Freeagent.com' in ob['tasks']['update']
        assert 'https://api.Freeagent.com' in ob['tasks']['delete']

    def test_we_have_non_empty_contact_entries(self):
        ob = URLs().URL_list()
        assert 'https://api.Freeagent.com' in ob['contacts']['all']
        assert 'https://api.Freeagent.com' in ob['contacts']['all_with_filter']
        assert 'https://api.Freeagent.com' in ob['contacts']['single']
        assert 'https://api.Freeagent.com' in ob['contacts']['create']
        assert 'https://api.Freeagent.com' in ob['contacts']['update']
        assert 'https://api.Freeagent.com' in ob['contacts']['delete']

    def test_we_have_none_empty_timeslip_entries(self):
        ob = URLs().URL_list()
        assert 'https://api.Freeagent.com' in ob['timeslips']['all']
        assert 'https://api.Freeagent.com' in ob['timeslips']['all_by_dates']
        assert 'https://api.Freeagent.com' in ob['timeslips']['all_by_user']
        assert 'https://api.Freeagent.com' in ob['timeslips']['all_by_task']
        assert (
            'https://api.Freeagent.com' in ob['timeslips']['all_by_project'])
        assert 'https://api.Freeagent.com' in ob['timeslips']['single']
        assert 'https://api.Freeagent.com' in ob['timeslips']['create']
        assert 'https://api.Freeagent.com' in ob['timeslips']['update']
        assert 'https://api.Freeagent.com' in ob['timeslips']['delete']
