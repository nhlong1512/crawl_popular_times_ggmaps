import os

# give time to download map tiles
SLEEP_SEC = 30.0

# csv output delimiter
DELIM = ','
HEADER_COLUMNS = ('place', 'url', 'scrape_time', 'day_of_week', 'hour_of_day',
                  'popularity_percent_normal', 'popularity_percent_current')


# path to chrome and chromedriver
CHROME_BINARY_LOCATION = "C:/Program Files/Google/Chrome/Application/chrome.exe"
# CHROME_BINARY_LOCATION = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
CHROMEDRIVER_BINARY_LOCATION = "C:/Users/diuai/chromedriver_win32/chromedriver.exe"

# keep an cache of the source htmls, with a timestamp in the filename
# if so, they should be cleaned out once in a while, since they are 1MB each
SAVE_HTML = False

# put your url or path here to a csv where the first column is a google maps url
# google sheets - export as csv https://stackoverflow.com/a/33727897/2327328
# URL_PATH_INPUT = None
URL_PATH_INPUT = 'D:/KLTN/CrawlTraffic/crawl_popular_times_ggmaps/gmaps_popular_times_scraper/tests/test_urls.csv'

DEBUG = False
# URL_PATH_INPUT_TEST = 'tests' + os.sep + 'test_urls.csv'
