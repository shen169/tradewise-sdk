"""
TradeWise Python SDK Client
"""
import httpx
from .agents import AgentsNamespace

TRADEWISE_API_BASE = "https://api.tradewise.ai"


class TradeWiseClient:
    """
    TradeWise API 客户端

    示例:
        client = TradeWiseClient(api_key="tw_your_key")
        result = client.agents.restock.consult(...)
    """

    def __init__(self, api_key: str, base_url: str = TRADEWISE_API_BASE, timeout: int = 60):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self._http = httpx.Client(
            base_url=self.base_url,
            headers={
                "Authorization": f"Bearer {api_key}",
                "X-SDK-Version": "0.1.0",
                "Content-Type": "application/json"
            },
            timeout=timeout
        )
        self.agents = AgentsNamespace(self._http)

    def __repr__(self):
        return f"TradeWiseClient(base_url={self.base_url!r})"
