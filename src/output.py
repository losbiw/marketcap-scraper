import pandas as pd
from src.config import config


def filter_entries(dataframe: pd.DataFrame, date_range: tuple[str, str]):
  start_date, end_date = date_range

  mask = (dataframe['date'] >= start_date) & (dataframe['date'] <= end_date)
  filtered = dataframe.loc[mask]

  return filtered


def write_to_excel(data: list[tuple[any, str]], output_file: str, date_range: tuple[str, str] = (None, None)):
  with pd.ExcelWriter(output_file) as writer:
    for entry in data:
      json, sheet_name = entry

      df = pd.DataFrame(json)
      df.rename({config.value_col: config.metric_col_dest},
                axis='columns', inplace=True)
      filtered_df = filter_entries(df, date_range)
      filtered_df.to_excel(writer, sheet_name=sheet_name, index=False)
