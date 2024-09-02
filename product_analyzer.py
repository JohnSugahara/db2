# product_analyzer.py

from collections import defaultdict

class ProductAnalyzer:
    def __init__(self, sales_data):
        """
        Inicializa a classe com os dados de vendas.
        
        :param sales_data: Lista de dicionários contendo os dados das vendas.
        """
        self.sales_data = sales_data

    def total_sales_per_day(self):
        """
        Calcula o total de vendas por dia.
        
        :return: Um dicionário com as datas como chaves e os totais de vendas como valores.
        """
        total_sales = defaultdict(float)
        for sale in self.sales_data:
            date = sale['date']
            total_sales[date] += sale['quantity'] * sale['price']
        return dict(total_sales)

    def most_sold_product(self):
        """
        Encontra o produto mais vendido em termos de quantidade total vendida.
        
        :return: O nome do produto mais vendido.
        """
        product_sales = defaultdict(int)
        for sale in self.sales_data:
            product = sale['product']
            product_sales[product] += sale['quantity']
        most_sold = max(product_sales, key=product_sales.get)
        return most_sold

    def highest_spent_customer(self):
        """
        Encontra o cliente que mais gastou em uma única compra.
        
        :return: O nome do cliente que gastou mais em uma única compra.
        """
        customer_spending = defaultdict(float)
        for sale in self.sales_data:
            customer = sale['customer']
            total = sale['quantity'] * sale['price']
            if total > customer_spending[customer]:
                customer_spending[customer] = total
        highest_spent = max(customer_spending, key=customer_spending.get)
        return highest_spent

    def products_with_quantity_above_one(self):
        """
        Lista todos os produtos que tiveram uma quantidade vendida acima de 1 unidade.
        
        :return: Uma lista de nomes de produtos com quantidade vendida superior a 1.
        """
        product_quantity = defaultdict(int)
        for sale in self.sales_data:
            product = sale['product']
            product_quantity[product] += sale['quantity']
        return [product for product, quantity in product_quantity.items() if quantity > 1]

# Exemplo de uso da classe ProductAnalyzer
if __name__ == "__main__":
    # Exemplo de dados de vendas
    sales_data = [
        {'date': '2024-09-01', 'product': 'Produto A', 'quantity': 2, 'price': 10.0, 'customer': 'Cliente 1'},
        {'date': '2024-09-01', 'product': 'Produto B', 'quantity': 1, 'price': 20.0, 'customer': 'Cliente 2'},
        {'date': '2024-09-02', 'product': 'Produto A', 'quantity': 1, 'price': 10.0, 'customer': 'Cliente 3'},
        # mais dados
    ]

    # Criação de uma instância da classe ProductAnalyzer
    analyzer = ProductAnalyzer(sales_data)

    # Usando os métodos da classe
    print("Total de vendas por dia:", analyzer.total_sales_per_day())
    print("Produto mais vendido:", analyzer.most_sold_product())
    print("Cliente que mais gastou em uma única compra:", analyzer.highest_spent_customer())
    print("Produtos com quantidade vendida acima de 1 unidade:", analyzer.products_with_quantity_above_one())
