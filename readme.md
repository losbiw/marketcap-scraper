> [!WARNING]
> The repo was intended as a once-off solution and hence isn't actively maintained. However, pull requests are welcome.

# About

There don't appear to be free, publically available datasets containing historic marketcaps of selected stocks. This project scrapes data from [macrotrends.net](https://www.macrotrends.net/) and turns it into a human-readable excel file.

> [!NOTE]
> A few words of advice:
>
> - The setup makes a few assumptions about the layout of the website itself, alongside the format of the data it uses. This is **potentially** subject to change.
> - The project was aimed specifically at scraping marketcap data. Macrotrends has a number of other metrics available, however they have not been tested against the existing code. If you feel brave, try changing `file_name` entry in [config.json](config.json) from `market_cap.php` to whatever other metric is required.

# Setup

## Unix

1. `python -m venv venv`
2. `chmod +X ./setup.sh && ./setup`

# Usage

Example: `python index.py NFLX IBM ORCL -s "2024-12-23" -e "2025-09-01"`

> [!IMPORTANT]
> US style dates (mm-dd-yyyy) must be used as opposed to european style dates.

```bash
usage: index.py [-h] [--start START_DATE] [--end END_DATE] [--output OUTPUT] tickers [tickers ...]

positional arguments:
tickers Requested stock tickers

optional arguments:
-h, --help show this help message and exit
--start START_DATE, -s START_DATE
Lower date range boundary
--end END_DATE, -e END_DATE
Upper date range boundary
--output OUTPUT, -o OUTPUT
Excel output file
```
