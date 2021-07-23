import os
from Config import *
import argparse


if __name__ == "__main__":
    print("Collecting HistoricData")

    parser = argparse.ArgumentParser()
    parser.add_argument("-c","--coin_pair",help="The coin-pair you want to get.")
    args = parser.parse_args()

    for i in range(len(COLLECTING_MONTHS[args.coin_pair])-1):
        month = COLLECTING_MONTHS[args.coin_pair]
        c = str(args.coin_pair)
        s = str(month[i])
        e = str(month[i+1])
        g = str(GRANULARITY)
        print(i," :　",month[i],month[i+1])
        print(f"python3 Get_rawdata.py -c \"{c}\" -s \"{s}\" -e \"{e}\" -g {g}")

    


# for m in range(len(COLLECTING_MONTHS["BTC-USD"])-1):
#     print(m," :　",COLLECTING_MONTHS["BTC-USD"][m],COLLECTING_MONTHS["BTC-USD"][m+1])
#     s = str(COLLECTING_MONTHS["BTC-USD"][m])
#     e = str(COLLECTING_MONTHS["BTC-USD"][m+1])
#     g = str(GRANULARITY)
#     # print(f"python Get_rawdata.py -c \"BTC-USD\" -s \"{s}\" -e \"{e}\" -g {g}")
#     os.system(f"python3 Get_rawdata.py -c \"BTC-USD\" -s \"{s}\" -e \"{e}\" -g \"{g}\"")

# for m in range(len(COLLECTING_MONTHS["ETH-USD"])-1):
#     print(m," :　",COLLECTING_MONTHS["ETH-USD"][m],COLLECTING_MONTHS["ETH-USD"][m+1])
#     s = str(COLLECTING_MONTHS["ETH-USD"][m])
#     e = str(COLLECTING_MONTHS["ETH-USD"][m+1])
#     g = str(GRANULARITY)
#     # print(f"python Get_rawdata.py -c \"BTC-USD\" -s \"{s}\" -e \"{e}\" -g {g}")
#     os.system(f"python3 Get_rawdata.py -c \"ETH-USD\" -s \"{s}\" -e \"{e}\" -g \"{g}\"")