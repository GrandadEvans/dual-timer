#! /usr/bin/python3

import json
import pycurl
import webbrowser
from urllib.parse import urlencode


import io
# import config from Config

class Freeagent:

    def __init__(self):
        # self.OAuthID = config.OAuthID
        # self.OAthSecret = config.OAuthSecret

        self.config = {
            "OAuthID": "1dOS3vN5XScJwrhTX6td7Q",
            "OAuthSecret": "TcV_eCfUK1lPbIEGJmXctA",
            "AccessTokenRequestURL": "https://api.freeagent.com/v2/token_endpoint",
            "getAllProjects": "https://api.freeagent.com/v2/_data?view=active",
            "APIURL": "1366ldIpUez6ykMn1kmc_0DoGDXltvK_u1AD45i-c"
        }

        self.urls = {
            "AuthorisationRequestURL": "https://api.freeagent.com/v2/approve_app",
            "AccessTokenRequestEndToken": "https://api.freeagent.com/v2/token_endpoint",
            "getAllProjects": "https://api.freeagent.com/v2/_data",
            "getAllTasks": "https://api.freeagent.com/v2/tasks"
        }

    # This is used to allow the dual timer app access to the account
    def authorisation_request(self):
        url = self.urls["AuthorisationRequestURL"]
        url += "?client_id=" + self.config["OAuthID"]
        url += "&response_type=code"
        webbrowser.open(url)

    # Now we have been granted authorisation we need an access token that ties
    # the app to the authorisation request
    def access_token_request(self):
        postfields = urlencode({
            "grant_type": "authorization_code",
            "code": "1Kv2fvW_XhlzKcMLuQKQ3mrBl8AEa_4VK4VvHYBR-"
        })

        buffer = io.BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, self.urls["AccessTokenRequestEndToken"])
        c.setopt(c.POSTFIELDS, postfields)
        c.setopt(c.USERPWD, "1dOS3vN5XScJwrhTX6td7Q:TcV_eCfUK1lPbIEGJmXctA")
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        body = buffer.getvalue()

        path = './authorisation_token.txt'
        f = io.open(path, "w")
        f.write(body.decode('utf-8'))
        c.close()

    def get_authorisation_token(self):
        f = io.open('./authorisation_token.txt')
        authorisation_token = f.read()
        return authorisation_token

    def getAllProjects(self):
        buffer = io.BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, self.urls["getAllProjects"])
        c.setopt(c.HTTPHEADER, ["Authorization: Bearer " + self.get_authorisation_token()])
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        body = buffer.getvalue()
        text_body = body.decode('utf-8')
        c.close()
        self.put_data_to_file(json.loads(text_body), './_data/_data.json')

    def put_data_to_file(self, data, filename):
        f = io.open(filename, "w")
        json.dump(data, f, True, True, True, True, None, 1, (',', ': '))

    def getAllTasks(self, project):
        buffer = io.BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, self.urls["getAllTasks"] + '?project=v2/_data/' + project)
        c.setopt(c.HTTPHEADER, ["Authorization: Bearer " + self.get_authorisation_token()])
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        body = buffer.getvalue()
        text_body = body.decode('utf-8')
        c.close()
        self.put_data_to_file(json.loads(text_body), './tasks/' + project + '.json')

    def get_usable_project_id(self, id):
        bits = id.split('https://api.freeagent.com/v2/_data/')
        return bits[1]


if __name__ == "__main__":
    Freeagent()
