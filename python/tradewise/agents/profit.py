"""利润测算Agent SDK封装"""


class ProfitAgent:
    ENDPOINT = "/v1/agents/profit/consult"

    def __init__(self, http_client):
        self._http = http_client

    def consult(self, asin: str, sale_price: float, unit_cost: float,
                marketplace: str = "US", **kwargs) -> dict:
        payload = {
            "asin": asin,
            "sale_price": sale_price,
            "unit_cost": unit_cost,
            "marketplace": marketplace,
            **kwargs
        }
        resp = self._http.post(self.ENDPOINT, json=payload)
        resp.raise_for_status()
        return resp.json()
