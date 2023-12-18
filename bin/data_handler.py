import glob
import json
import os

import requests
from PyQt6.QtWidgets import QInputDialog


class DataHandler:
    base_dir = 'data'
    base_url = 'https://adventofcode.com'
    conf_file = 'config.json'
    file_dict = {}

    def __init__(self, gui):
        self.gui = gui
        for filename in glob.iglob(self.base_dir + '**/*', recursive=True):
            if os.path.isfile(filename):  # exclude directories
                # key = filename without base_dir and extension, value = full filename
                key = os.path.splitext(filename.replace(self.base_dir + '/', ''))[0]
                self.file_dict[filename.split('\\')[1]] = key

    def __getitem__(self, item):
        file = self.file_dict.get(item, None)
        if file is None:
            # File not found in local data, attempt to download it
            file = self.download_file(item)
        with open(file, 'r') as f:
            return f.read()

    def build_url(self, item):
        year = "20" + item[1:3]
        day = int(item[4:6])
        url = f"{self.base_url}/{year}/day/{day}/input"
        return url

    def download_file(self, item):
        url = self.build_url(item)
        with requests.Session() as session:
            response = self.request_file(session, url)
            if response.status_code == 400:
                session.cookies.pop('session', None)
                response = self.request_file(session, url)
            file_path = os.path.join(self.base_dir, item)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            return file_path

    def request_file(self, session, url):
        self.login(session)
        return session.get(url)

    def login(self, session):
        conf_data = self.load_conf()
        token = conf_data.get('session_token')
        if token is None or not self.verify_token(session, token):
            token = self.prompt_for_token()
            conf_data['session_token'] = token
            self.save_conf(conf_data)
        session.cookies['session'] = token

    def load_conf(self):
        if os.path.exists(self.conf_file):
            with open(self.conf_file, 'r') as f:
                return json.load(f)
        else:
            return {}

    def save_conf(self, conf_data):
        with open(self.conf_file, 'w') as f:
            json.dump(conf_data, f)

    def prompt_for_token(self):
        token, ok = QInputDialog.getText(
            self.gui._main_window, "Session token", "Please enter your session token:"
        )
        if ok and token:
            return token
        else:
            raise ValueError("Invalid session token")

    def verify_token(self, session, token):
        # Replace with a function that verifies the token
        session.cookies['session'] = token
        response = session.get(self.base_url)
        return response.status_code == 200
