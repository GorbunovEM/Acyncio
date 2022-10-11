import aiohttp
import asyncio
import time
import requests

url = 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{}?modules=price'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.2.1495 Yowser/2.5 Safari/537.36'}
tickers = ['AAPL', 'AMZN', 'GOOG', 'DAL', 'AA']

def asynchronous():
    async def fetch(client, ticker, url, headers):
        async with client.get(url.format(ticker), headers=headers) as resp:
            assert resp.status == 200
            return await resp.text()

    async def main(ticker, url):
        async with aiohttp.ClientSession() as client:
            html = await fetch(client, ticker, url, headers)
            print(html)

    start = time.time()
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(main(ticker, url)) for ticker in tickers]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    end = time.time()
    print("Total time: {}".format(end - start))

def synchronous():
    def fetch_syn(ticker, url, headers):
        response = requests.get(url.format(ticker), headers=headers)
        print(response.text)

    start = time.time()
    for ticker in tickers:
        fetch_syn(ticker, url, headers)
    end = time.time()
    print("Total time: {}".format(end - start))

asynchronous()
synchronous()
