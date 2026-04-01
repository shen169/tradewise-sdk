"""
TradeWise 补货Agent 示例
运行: python demo.py
"""
from tradewise import TradeWiseClient

client = TradeWiseClient(api_key="tw_test_xxx")

result = client.agents.restock.consult(
    asin="B08XXXXX",
    sku="MY-SKU-001",
    sales_data={
        "last_30_days": 450,
        "last_60_days": 820,
        "last_90_days": 1150,
        "same_period_last_year": 380,
        "avg_daily_last_year": 12.0
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

print("=== 补货决策 ===")
print(f"决策: {result['decision']}")
print(f"建议补货量: {result['suggested_quantity']} 件")
print(f"紧急程度: {result['urgency_level']}")
print(f"运输建议: {result['shipping_recommendation']['label']}")
print(f"预测日销: {result['predicted_daily_sales']} 件/天")
print(f"当前库存可卖: {result['days_of_supply']} 天")
print(f"置信度: {result['confidence']:.0%}")
