class SalesAnalytics:
    def __init__(self):
        self.sales_data = []

    def record_sale(self, product, quantity):
        self.sales_data.append({"product": product, "quantity": quantity})

    def calculate_total_sales(self):
        total_sales = sum(item['product'].price * item['quantity'] for item in self.sales_data)
        return total_sales

# Example usage:
analytics = SalesAnalytics()
analytics.record_sale(Product(1, "T-shirt", 20, "Comfortable cotton T-shirt"), 10)
analytics.record_sale(Product(2, "Jeans", 40, "Classic denim jeans"), 5)
total_sales = analytics.calculate_total_sales()
print("Total Sales:", total_sales)
