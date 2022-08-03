from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

def GetHistoricalDataUsecase(id: str="bitcoin", vs_currency: str="usd", limit: int=10000):
    raw = cg.get_coin_market_chart_by_id(id=id, vs_currency=vs_currency, days=limit)

    data = list()
    for price, vol, cap in zip(raw['prices'], raw['total_volumes'], raw['market_caps']):
        tmp = dict(
            timestamp=price[0],
            price=price[1],
            volume=vol[1],
            market_cap=cap[1]
        )
        data.append(tmp)

    return data

def GetMarketDataUsecase(limit: int=100, offset: int=1):
    raw = cg.get_coins_markets(vs_currency="usd", per_page=limit, page=offset)
    return raw

def GetMarketDataByKeyUsecase(key="bitcoin"):
    raw = cg.get_coins_markets(vs_currency="usd", ids=[key])
    if len(raw):
        return raw[0]
    raise Exception("Could not find coin with the given id")