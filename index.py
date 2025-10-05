import asyncio
import re
from argparse import ArgumentParser, Namespace
from src import network, output, parse


def assign_args():
  cli_parser = ArgumentParser()

  cli_parser.add_argument("tickers", nargs="+", help="Requested stock tickers")
  cli_parser.add_argument("--start", "-s", dest="start_date",
                          help="Lower date range boundary")
  cli_parser.add_argument("--end", "-e", dest="end_date",
                          help="Upper date range boundary")
  cli_parser.add_argument("--output", "-o", dest="output",
                          help="Excel output file", default="output.xlsx")

  args = cli_parser.parse_args()
  validate_args(args)

  return args


def validate_args(args: Namespace):
  date_regex = re.compile(r"(\d{4})-(\d{2})-(\d{2})")

  if args.start_date and not bool(re.match(date_regex, args.start_date)):
    raise Exception(
      f"Invalid start date format: {args.start_date}. Expected: year-mm-dd or year-dd-mm.")
  if args.end_date and not bool(re.match(date_regex, args.end_date)):
    raise Exception(
      f"Invalid end date format: {args.end_date}. Expected: year-mm-dd or year-dd-mm.")
  if not args.output.endswith(".xlsx"):
    raise Exception(f"Invalid file format: {args.output}. Expected .xlsx")


async def main():
  args = assign_args()
  files = await network.get_raw_files(args.tickers)
  parsed_json = parse.extract_data(files, args.tickers)

  output.write_to_excel(list(zip(parsed_json, args.tickers)), args.output,
                        date_range=(args.start_date, args.end_date))


if __name__ == "__main__":
  asyncio.run(main())
