from database import Database
from helper.writeAJson import writeAJson
from product_analyzer import ProductAnalyzer
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")

result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total": -1}},
    {"$limit": 1}
])

writeAJson(result, "Produto mais vendido")

analyzer = ProductAnalyzer(database_name="mercado", collection_name="compras")

# Total de vendas por dia
sales_per_day = analyzer.total_sales_per_day()
writeAJson(sales_per_day, "Total de Vendas por Dia")

# Produto mais vendido
most_sold_product = analyzer.most_sold_product()
writeAJson(most_sold_product, "Produto Mais Vendido")

# Cliente que mais gastou
highest_spending_customer = analyzer.highest_spending_customer()
writeAJson(highest_spending_customer, "Cliente que Mais Gastou")

# Produtos vendidos acima de uma unidade
products_above_one_unit = analyzer.products_sold_above_one_unit()
writeAJson(products_above_one_unit, "Produtos Vendidos Acima de Uma Unidade")