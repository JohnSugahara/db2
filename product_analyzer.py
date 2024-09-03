# product_analyzer.py

from database import Database

class ProductAnalyzer:
    def __init__(self, database_name, collection_name):
        self.db = Database(database=database_name, collection=collection_name)

    def total_sales_per_day(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data", "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id": 1}}
        ]
        result = self.db.collection.aggregate(pipeline)
        return list(result)

    def most_sold_product(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ]
        result = self.db.collection.aggregate(pipeline)
        return list(result)

    def highest_spending_customer(self):
        pipeline = [
            {"$group": {"_id": "$cliente", "total_gasto": {"$max": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ]
        result = self.db.collection.aggregate(pipeline)
        return list(result)

    def products_sold_above_one_unit(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"total_vendido": {"$gt": 1}}}
        ]
        result = self.db.collection.aggregate(pipeline)
        return list(result)
