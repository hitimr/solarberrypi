import os, sys
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, datetime, timedelta

sys.path.insert(0, ".")
import config as cfg


class SE_Interface:
    url_request = str

    def __init__(self):
        api_file = cfg.FILE_API_KEY
        assert os.path.exists(api_file)

        # Load API Key from file
        f = open(api_file, 'r')
        self.api_credentials = json.loads(f.read())
        f.close()
        assert("key" in self.api_credentials)
        assert("id" in self.api_credentials)

        self.apiKey = self.api_credentials["key"]
        #self.url_request = cfg.URL_SOLAR_EDGE_JSON_ENDPOINT + self.api_credentials["key"]


    def request(self, url):
        print(f"Requesting: {url}")
        r = requests.get(url)
        #r = requests.get("https://monitoringapi.solaredge.com/sites/list?size=5&searchText=Lyon&sortProperty=name&sortOrder=ASC&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O")
        assert(r.status_code == cfg.STATUS_CODE_OK) # Got invalid response // TODO: proper error hanling
        #print(r.content)
        return r.json()

    def request_SitePowerDetailed(self, endTime, timeIntervall, safeToFile=False):
        #Example: powerDetails?meters=PRODUCTION,CONSUMPTION&startTime=2015-11-21%2011:00:00&endTime=2015-11-22%2013:00:00&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O
        #Exampl: https://monitoringapi.solaredge.com/site/1/powerDetails?meters=PRODUCTION,CONSUMPTION&startTime=2021-08-19 11:00:00&endTime=2021-08-20 13:00:00&api_key=NTT5LNJGA5CDCFI9OZGZCX2W1VD3CCW2

        # (Production/Consumption/SelfConsumption/FeedIn (export)/Purchased(import))
        
        meters="Consumption,Production"
        meterCnt = 1
        for letter in meters: 
            if letter == ",": 
                meterCnt += 1


        startTime = (endTime - timeIntervall).strftime(cfg.DATETIME_FORMAT)

        url = cfg.URL_SOLAR_EDGE_BASE + f"powerDetails?meters={meters}&startTime={startTime}&endTime={endTime.strftime(cfg.DATETIME_FORMAT)}&api_key={self.apiKey}"
        response = self.request(url)
        
        data = pd.DataFrame()
        types = []
        for i in range(meterCnt):
            type = response["powerDetails"]["meters"][i]["type"]
            types.append(type)

            df = pd.DataFrame()
            df = pd.DataFrame.from_dict(response["powerDetails"]["meters"][i]["values"])
            df = df.rename(columns={"value" : type})
            df = df.set_index("date")
            data = pd.concat([data, df])
            

        data = data.groupby(level=0).sum()
        data = data.fillna(0)
        if safeToFile: data.to_csv("out/data.csv")

        return data
        


if __name__ == "__main__":
    se_interface = SE_Interface()

    #now = datetime.now() - timedelta(minutes=15)
    now = datetime(year=2021, month=8, day=15, hour=23)
    se_interface.request_SitePowerDetailed(now, timedelta(days=2))

    pass