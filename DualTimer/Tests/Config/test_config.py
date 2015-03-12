#! /usr/bin/env python3
"""
Tests to make sure that we have the correct Config keys in a template File

The system will be responsible for converting this template into the correct
Config File once it is installed. But this way it keeps the real ie my
API OAuth data out of the Version Control System
"""

import pytest

from DualTimer.Src.Config.Freeagent import Freeagent


class TestConfig:

    def test_we_have_a_blank_oauth_id(self):
        ob = Freeagent().ob()
        print(ob)
        assert ob['freeagent_API_auth_ID'] == ""

    def test_we_have_a_blank_oauth_secret(self):
        ob = Freeagent().ob()
        assert ob['freeagent_API_auth_secret'] == ""
