"""补货Agent SDK封装"""


class RestockAgent:
    ENDPOINT = "/v1/agents/restock/consult"

    def __init__(self, http_client):
        self._http = http_client

    def consult(self, asin: str, sku: str, sales_data: dict,
                supply_chain: dict, context: dict) -> dict:
        payload = {
            "asin": asin,
            "sku": sku,
            "sales_data": sales_data,
            "supply_chain": supply_chain,
            "context": context
        }
        resp = self._http.post(self.ENDPOINT, json=payload)
        resp.raise_for_status()
        return resp.json()
