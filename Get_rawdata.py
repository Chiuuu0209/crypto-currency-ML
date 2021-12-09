import sys
import cbpro
import json
import datetime
import time
import numpy as np
import os
import math
import argparse

class CoinbaseAPI:
    public_clinet = None

    def __init__(self):
        print("> Coinbase API Initialized")
        self.feature_names = [] # For feature comparison and visualization
        self.public_client = cbpro.PublicClient()
    

    # [ time, low, high, open, close, volume ],
    def getCoinHistoricData(self,coin_pair,start,end,granularity):
        print("> Collecting historic data for "+coin_pair," from ",start," to ",end," every ",granularity," sec")

        data = []
        start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
        while (start_date < end_date):
            print("> Date: ",start_date)
            start_limit = start_date
            end_limit = start_date + datetime.timedelta(hours=1)

            reversed_response = [] # Put in correct date order
            next_data = self.public_client.get_product_historic_rates(coin_pair, granularity=granularity,start=start_limit,end=end_limit)
            for nd in next_data:
                reversed_response.append(nd)

            data.append(list(reversed(reversed_response))[:-1])
            start_date += datetime.timedelta(minutes=60)
            time.sleep(3)

        return data
    
    def storeRawCoinHistoricData(self, datetime, granularity , coin_pair, data):
        print("> Storing Raw Historic Data for ", coin_pair)
        if not os.path.exists('raw_historic_data/'):
            os.mkdir('raw_historic_data')
        if not os.path.exists(f'raw_historic_data/{coin_pair}'):
            os.mkdir(f'raw_historic_data/{coin_pair}')
        if not os.path.exists(f'raw_historic_data/{coin_pair}/{granularity}'):
            os.mkdir(f'raw_historic_data/{coin_pair}/{granularity}')
        with open(f'raw_historic_data/{coin_pair}/{granularity}/{datetime}_{coin_pair}.json', 'w') as outfile:
            json.dump(data, outfile)


if __name__ == '__main__':
    print("Get raw_historic_data")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-c","--coin_pair",help="The coin-pair you want to get.")
    parser.add_argument("-s","--start",help="The interval starttime.")
    parser.add_argument("-e","--end",help="The interval endtime.")
    parser.add_argument("-g","--granularity",help="The granularity",type=int,default=60,choices=[60, 300, 900, 3600, 21600, 86400])
    args = parser.parse_args()
    # print("args:",args)

    tokens = args.start.split("-")
    # print("tokens:",tokens)
    if tokens:
        date = f"{tokens[0]}_{tokens[1]}"
    else:
        date = "2022_01"
    # print("date:",date)


    coinbaseAPI = CoinbaseAPI()
    historic_data = coinbaseAPI.getCoinHistoricData(coin_pair=args.coin_pair,start=args.start,end=args.end,granularity=args.granularity)
    # print("historic data:",historic_data[0])
    coinbaseAPI.storeRawCoinHistoricData(datetime=date,granularity=args.granularity,coin_pair=args.coin_pair,data=historic_data)
    print(f"> Collecting {args.coin_pair} historic_data from {args.start} to {args.end}.")