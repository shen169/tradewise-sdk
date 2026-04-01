# TradeWise SDK

> **跨境电商 Agent-to-Agent 专家服务平台 — 官方SDK**

让任何AI Agent在5分钟内接入10年跨境电商专家决策能力。

## 快速开始

### Python

```bash
pip install tradewise
```

```python
from tradewise import TradeWiseClient

client = TradeWiseClient(api_key="tw_your_api_key")

# 补货决策
result = client.agents.restock.consult(
    asin="B08XXXXX",
    sku="MY-SKU-001",
    sales_data={
        "last_30_days": 450,
        "last_60_days": 820,
        "last_90_days": 1150,
        "same_period_last_year": 380
    },
    supply_chain={
        "production_lead_time": 30,
        "preferred_shipping": "sea",
        "unit_cost": 8.5,
        "shipping_cost_per_unit": 1.2
    },
    context={
        "current_stock": 280,
        "inbound_quantity": 150,
        "product_lifecycle": "growth",
        "profit_margin": 35.0,
        "fba_capacity_limit": 1000,
        "marketplace": "US"
    }
)

print(result.decision)           # "restock_now"
print(result.suggested_quantity) # 520
print(result.urgency_level)      # "high"
print(result.shipping_recommendation)
```

### JavaScript / Node.js

```bash
npm install @tradewise/sdk
```

```javascript
const { TradeWise } = require('@tradewise/sdk');
const client = new TradeWise({ apiKey: 'tw_your_api_key' });

const result = await client.agents.restock.consult({ ... });
```

### MCP (Model Context Protocol)

```json
{
  "mcpServers": {
    "tradewise": {
      "url": "https://mcp.tradewise.ai/v1",
      "apiKey": "tw_your_api_key"
    }
  }
}
```

## 文档

- [API Reference](https://docs.tradewise.ai)
- [MCP Schema](./schemas/mcp_schema.json)
- [示例代码](./examples/)

## 许可证

MIT License — SDK开源，核心知识库和决策引擎闭源
