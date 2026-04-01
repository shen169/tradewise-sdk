from .restock import RestockAgent
from .profit import ProfitAgent


class AgentsNamespace:
    def __init__(self, http_client):
        self.restock = RestockAgent(http_client)
        self.profit  = ProfitAgent(http_client)
