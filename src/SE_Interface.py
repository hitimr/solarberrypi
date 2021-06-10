import requests
import os
import json

import src.config as cfg


class SE_Interace:
    def __init__(self, api_file):
        assert os.path.exists(api_file)

        # Load API Key from file
        f = open(api_file, 'r')
        self.api_credentials = json.loads(f.read())
        f.close()
        assert("key" in self.api_credentials)
        assert("id" in self.api_credentials)



if __name__ == "__main__":
    SE_Interace(cfg.FILE_API_KEY)
    

    pass