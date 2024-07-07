import requests

try:
    from functools import cache
except ImportError:
    # Python 3.7 / 3.8
    from functools import lru_cache
    cache = lru_cache(maxsize=None)


class Converter:
    API_URL = "https://api.exchangeit.app/v1/currencies/eur/latest"
    HEADERS = {"User-Agent": "rpncalc/0.1 (florian@bruhin.software)"}
    PARAMS = {"for": "chf"}

    def eur2chf(self, amount: float) -> float:
        eur2chf_rate = self._fetch()
        return amount * eur2chf_rate

    def chf2eur(self, amount: float) -> float:
        eur2chf_rate = self._fetch()
        return amount / eur2chf_rate

    @cache
    def _fetch(self) -> float:
        print("Fetching exchange rates...")
        response = requests.get(
            self.API_URL,
            params=self.PARAMS,
            headers=self.HEADERS,
        )
        response.raise_for_status()
        d = response.json()
        rates = d["data"]["rates"]
        return rates[0]["rate"]