DATASET_DIR = "datasets/"
RAWDATASET_DIR = "raw_historic_data/"
GRANULARITY = 60
HISTORIC_MONTHS = {
    "BTC-USD":[
    # "2014_01","2014_02","2014_03","2014_04","2014_05","2014_06","2014_07","2014_08","2014_09","2014_10","2014_11","2014_12",
    # "2015_01","2015_02","2015_03","2015_04","2015_05","2015_06","2015_07",
    "2015_08","2015_09","2015_10","2015_11","2015_12",
    "2016_01","2016_02","2016_03","2016_04","2016_05","2016_06","2016_07","2016_08","2016_09","2016_10","2016_11","2016_12",
    "2017_01","2017_02","2017_03","2017_04","2017_05","2017_06","2017_07","2017_08","2017_09","2017_10","2017_11","2017_12",
    "2018_01","2018_02","2018_03","2018_04","2018_05","2018_06","2018_07","2018_08","2018_09","2018_10","2018_11","2018_12",
    "2019_01","2019_02","2019_03","2019_04","2019_05","2019_06","2019_07","2019_08","2019_09","2019_10","2019_11","2019_12",
    "2020_01","2020_02","2020_03","2020_04","2020_05","2020_06","2020_07","2020_08","2020_09","2020_10","2020_11","2020_12",
    "2021_01","2021_02","2021_03","2021_04","2021_05","2021_06"
],
    "BTC-USDT":[
    # "2014_01","2014_02","2014_03","2014_04","2014_05","2014_06","2014_07","2014_08","2014_09","2014_10","2014_11","2014_12",
    # "2015_01","2015_02","2015_03","2015_04","2015_05","2015_06","2015_07","2015_08","2015_09","2015_10","2015_11","2015_12",
    # "2016_01","2016_02","2016_03","2016_04","2016_05","2016_06","2016_07","2016_08","2016_09","2016_10","2016_11","2016_12",
    # "2017_01","2017_02","2017_03","2017_04","2017_05","2017_06","2017_07","2017_08","2017_09","2017_10","2017_11","2017_12",
    "2018_01","2018_02","2018_03","2018_04","2018_05","2018_06","2018_07","2018_08","2018_09","2018_10","2018_11","2018_12",
    "2019_01","2019_02","2019_03","2019_04","2019_05","2019_06","2019_07","2019_08","2019_09","2019_10","2019_11","2019_12",
    "2020_01","2020_02","2020_03","2020_04","2020_05","2020_06","2020_07","2020_08","2020_09","2020_10","2020_11","2020_12",
    "2021_01","2021_02","2021_03","2021_04","2021_05","2021_06"
],
    "ETH-USD":[
    # "2016_01","2016_02","2016_03","2016_04","2016_05","2016_06","2016_07","2016_08",
    "2016_09","2016_10","2016_11","2016_12",
    "2017_01","2017_02","2017_03","2017_04","2017_05","2017_06","2017_07","2017_08","2017_09","2017_10","2017_11","2017_12",
    "2018_01","2018_02","2018_03","2018_04","2018_05","2018_06","2018_07","2018_08","2018_09","2018_10","2018_11","2018_12",
    "2019_01","2019_02","2019_03","2019_04","2019_05","2019_06","2019_07","2019_08","2019_09","2019_10","2019_11","2019_12",
    "2020_01","2020_02","2020_03","2020_04","2020_05","2020_06","2020_07","2020_08","2020_09","2020_10","2020_11","2020_12",
    "2021_01","2021_02","2021_03","2021_04","2021_05","2021_06"
],
    "ETH-USDT":[
    # "2016_01","2016_02","2016_03","2016_04","2016_05","2016_06","2016_07","2016_08","2016_09","2016_10","2016_11","2016_12",
    # "2017_01","2017_02","2017_03","2017_04","2017_05","2017_06","2017_07","2017_08","2017_09","2017_10","2017_11","2017_12",
    "2018_01","2018_02","2018_03","2018_04","2018_05","2018_06","2018_07","2018_08","2018_09","2018_10","2018_11","2018_12",
    "2019_01","2019_02","2019_03","2019_04","2019_05","2019_06","2019_07","2019_08","2019_09","2019_10","2019_11","2019_12",
    "2020_01","2020_02","2020_03","2020_04","2020_05","2020_06","2020_07","2020_08","2020_09","2020_10","2020_11","2020_12",
    "2021_01","2021_02","2021_03","2021_04","2021_05","2021_06"
]

}
COLLECTING_MONTHS = {
    "BTC-USD":[
        # "2014-01-01","2014-02-01","2014-03-01","2014-04-01","2014-05-01","2014-06-01","2014-07-01","2014-08-01","2014-09-01","2014-10-01","2014-11-01","2014-12-01",
        # "2015-01-01","2015-02-01","2015-03-01","2015-04-01","2015-05-01","2015-06-01","2015-07-01","2015-08-01",
        "2015-09-01","2015-10-01","2015-11-01","2015-12-01",
        "2016-01-01","2016-02-01","2016-03-01","2016-04-01","2016-05-01","2016-06-01","2016-07-01","2016-08-01","2016-09-01","2016-10-01","2016-11-01","2016-12-01",
        "2017-01-01","2017-02-01","2017-03-01","2017-04-01","2017-05-01","2017-06-01","2017-07-01","2017-08-01","2017-09-01","2017-10-01","2017-11-01","2017-12-01",
        "2018-01-01","2018-02-01","2018-03-01","2018-04-01","2018-05-01","2018-06-01","2018-07-01","2018-08-01","2018-09-01","2018-10-01","2018-11-01","2018-12-01",
        "2019-01-01","2019-02-01","2019-03-01","2019-04-01","2019-05-01","2019-06-01","2019-07-01","2019-08-01","2019-09-01","2019-10-01","2019-11-01","2019-12-01",
        "2020-01-01","2020-02-01","2020-03-01","2020-04-01","2020-05-01","2020-06-01","2020-07-01","2020-08-01","2020-09-01","2020-10-01","2020-11-01","2020-12-01",
        "2021-01-01","2021-02-01","2021-03-01","2021-04-01","2021-05-01","2021-06-01","2021-07-01"
    ],
    "BTC-USDT":[
        # "2014-01-01","2014-02-01","2014-03-01","2014-04-01","2014-05-01","2014-06-01","2014-07-01","2014-08-01","2014-09-01","2014-10-01","2014-11-01","2014-12-01",
        # "2015-01-01","2015-02-01","2015-03-01","2015-04-01","2015-05-01","2015-06-01","2015-07-01","2015-08-01","2015-09-01","2015-10-01","2015-11-01","2015-12-01",
        # "2016-01-01","2016-02-01","2016-03-01","2016-04-01","2016-05-01","2016-06-01","2016-07-01","2016-08-01","2016-09-01","2016-10-01","2016-11-01","2016-12-01",
        "2017-01-01","2017-02-01","2017-03-01","2017-04-01","2017-05-01","2017-06-01","2017-07-01","2017-08-01","2017-09-01","2017-10-01","2017-11-01","2017-12-01",
        "2018-01-01","2018-02-01","2018-03-01","2018-04-01","2018-05-01","2018-06-01","2018-07-01","2018-08-01","2018-09-01","2018-10-01","2018-11-01","2018-12-01",
        "2019-01-01","2019-02-01","2019-03-01","2019-04-01","2019-05-01","2019-06-01","2019-07-01","2019-08-01","2019-09-01","2019-10-01","2019-11-01","2019-12-01",
        "2020-01-01","2020-02-01","2020-03-01","2020-04-01","2020-05-01","2020-06-01","2020-07-01","2020-08-01","2020-09-01","2020-10-01","2020-11-01","2020-12-01",
        "2021-01-01","2021-02-01","2021-03-01","2021-04-01","2021-05-01","2021-06-01","2021-07-01"
    ],
    "ETH-USD":[
        # "2016-01-01","2016-02-01","2016-03-01","2016-04-01","2016-05-01","2016-06-01",
        "2016-07-01","2016-08-01","2016-09-01","2016-10-01","2016-11-01","2016-12-01",
        "2017-01-01","2017-02-01","2017-03-01","2017-04-01","2017-05-01","2017-06-01","2017-07-01","2017-08-01","2017-09-01","2017-10-01","2017-11-01","2017-12-01",
        "2018-01-01","2018-02-01","2018-03-01","2018-04-01","2018-05-01","2018-06-01","2018-07-01","2018-08-01","2018-09-01","2018-10-01","2018-11-01","2018-12-01",
        "2019-01-01","2019-02-01","2019-03-01","2019-04-01","2019-05-01","2019-06-01","2019-07-01","2019-08-01","2019-09-01","2019-10-01","2019-11-01","2019-12-01",
        "2020-01-01","2020-02-01","2020-03-01","2020-04-01","2020-05-01","2020-06-01","2020-07-01","2020-08-01","2020-09-01","2020-10-01","2020-11-01","2020-12-01",
        "2021-01-01","2021-02-01","2021-03-01","2021-04-01","2021-05-01","2021-06-01","2021-07-01"
    ],
    "ETH-USDT":[
        # "2016-01-01","2016-02-01","2016-03-01","2016-04-01","2016-05-01","2016-06-01","2016-07-01","2016-08-01","2016-09-01","2016-10-01","2016-11-01","2016-12-01",
        "2017-01-01","2017-02-01","2017-03-01","2017-04-01","2017-05-01","2017-06-01","2017-07-01","2017-08-01","2017-09-01","2017-10-01","2017-11-01","2017-12-01",
        "2018-01-01","2018-02-01","2018-03-01","2018-04-01","2018-05-01","2018-06-01","2018-07-01","2018-08-01","2018-09-01","2018-10-01","2018-11-01","2018-12-01",
        "2019-01-01","2019-02-01","2019-03-01","2019-04-01","2019-05-01","2019-06-01","2019-07-01","2019-08-01","2019-09-01","2019-10-01","2019-11-01","2019-12-01",
        "2020-01-01","2020-02-01","2020-03-01","2020-04-01","2020-05-01","2020-06-01","2020-07-01","2020-08-01","2020-09-01","2020-10-01","2020-11-01","2020-12-01",
        "2021-01-01","2021-02-01","2021-03-01","2021-04-01","2021-05-01","2021-06-01","2021-07-01"
    ],
    "XRP-USD":[
        "2016-07-01","2016-08-01","2016-09-01","2016-10-01","2016-11-01","2016-12-01",
        "2017-01-01","2017-02-01","2017-03-01","2017-04-01","2017-05-01","2017-06-01","2017-07-01","2017-08-01","2017-09-01","2017-10-01","2017-11-01","2017-12-01",
        "2018-01-01","2018-02-01","2018-03-01","2018-04-01","2018-05-01","2018-06-01","2018-07-01","2018-08-01","2018-09-01","2018-10-01","2018-11-01","2018-12-01",
        "2019-01-01","2019-02-01","2019-03-01","2019-04-01","2019-05-01","2019-06-01","2019-07-01","2019-08-01","2019-09-01","2019-10-01","2019-11-01","2019-12-01",
        "2020-01-01","2020-02-01","2020-03-01","2020-04-01","2020-05-01","2020-06-01","2020-07-01","2020-08-01","2020-09-01","2020-10-01","2020-11-01","2020-12-01",
        "2021-01-01","2021-02-01","2021-03-01","2021-04-01","2021-05-01","2021-06-01","2021-07-01"
    ]
}