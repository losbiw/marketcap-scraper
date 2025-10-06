import re
from json import loads
from src.config import config


def extract_data(files: list[str], tickers: list[str]):
  regex = re.compile(
    config.data_extraction_regex, flags=re.DOTALL | re.MULTILINE)

  return [extract_json_from_file(file, regex, ticker) for (file, ticker) in zip(files, tickers)]


def extract_json_from_file(raw_file: str, regex: re.Pattern[str], name="unknown"):
  res = re.search(regex, raw_file)

  if not res:
    print(f"No match found for: {name}")
    return None

  return loads(res.group(1))
