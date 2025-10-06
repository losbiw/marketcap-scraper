from json import loads


class Config:
  # base_url and res_file must be populated
  to_find = ["base_url", "file_name", "metric_col_dest",
             "value_col", "data_extraction_regex"]

  def __init__(self, cfg_file):
    with open(cfg_file) as config:
      content = config.read()
      deserialized = loads(content)

      self.populate(deserialized)

  def populate(self, data: any):
    for flag in self.to_find:
      if flag not in data:
        raise ValueError(f"Property {flag} missing from config")

      setattr(self, flag, data[flag])


config = Config("config.json")
