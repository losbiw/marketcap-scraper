import aiohttp
import asyncio
from src.config import config


async def get_raw_files(tickers: list[str]):
  async with aiohttp.ClientSession() as session:
    urls = [get_macrotrends_url(ticker) for ticker in tickers]
    tasks = [fetch(url, session) for url in urls]

    results = await asyncio.gather(*tasks, return_exceptions=True)

    for url, res in zip(urls, results):
      if isinstance(res, Exception):
        print(f'Failed to fetch from URL: {url}')

    return results


async def fetch(url: str, session: aiohttp.ClientSession):
  async with session.get(url) as res:
    return await res.text()


def get_macrotrends_url(ticker: str):
  return f'{config.base_url}/{config.file_name}?t={ticker}'
