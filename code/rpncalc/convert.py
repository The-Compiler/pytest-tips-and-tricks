# rpncalc/convert.py
import requests

class Converter:

    API_URL = "https://api.exchangerate.host/convert"
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
        params = {"from": "EUR", "to": "CHF"}
        headers = {"User-Agent": self.USER_AGENT}
        response = requests.get(
            self.API_URL,
            params=params,
            headers=headers)
        response.raise_for_status()
        data = response.json()
        assert data["success"], data
        return data["result"]
