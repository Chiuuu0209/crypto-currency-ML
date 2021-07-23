Collecting crypotocurrency historic data
================================================================
Downloading crypotocurrency historic data from CoinbasePro API for building ML model.

Usage
--------------------
- Collecting specific coin-pair with some interval
    - Get_rawdata.py -c {coin-pair} -s {start-time} -e {end-time} -g {granularity}
```
python3 Get_rawdata.py -c "BTC-USD" -s "2021-01-01" -e 2021-02-01 -g 60
```

- Run script for collecting whole data we specific in Config
    - Collecting_HistoricData.py -c {coin-pair}
```
python3 Collecting_HistoricData.py -c "BTC-USD"
```