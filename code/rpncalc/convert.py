import requests


class Converter:
    API_URL = "https://api.exchangeit.app/rates/latest"
    USER_AGENT = "rpncalc/0.1 (florian@bruhin.software)"

    def __init__(self) -> None:
        self._eur2chf_rate = None

    def eur2chf(self, amount: float) -> float:
        if self._eur2chf_rate is None:
            self._eur2chf_rate = self._fetch()
        return amount * self._eur2chf_rate

    def chf2eur(self, amount: float) -> float:
        if self._eur2chf_rate is None:
            self._eur2chf_rate = self._fetch()
        return amount / self._eur2chf_rate

    def _fetch(self) -> float:
        print("Fetching exchange rates...")
        params = {"codes": ["EUR"]}
        headers = {"User-Agent": self.USER_AGENT}
        response = requests.get(
            self.API_URL,
            params=params,
            headers=headers,
        )
        response.raise_for_status()
        d = response.json()
        rates = d["data"][0]["rates"]
        rates_dict = {
            rate["code"]: rate["rate"]
            for rate in rates
        }
        return rates_dict["chf"]
