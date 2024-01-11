class FoodDeliverySystem:
    order_id = 0
    orders_log = {}
    def __init__(self):
        self.menu = {
            "Burger": 150,
            "Pizza": 250,
            "Pasta": 200,
            "Salad": 120,
            "Beverages": 130,
            "Noodles": 150,
            "Sushi": 270,
            "Bakery":350
            # Add more items to the menu
        }
        self.bill_amount = 0
        
    def display_menu(self):
        return """
        Return the menu details in the following format:
        Burger  |  150
        Pizza   |  250
        Pasta   |  200
        Salad   |  120
        Beverages  |  130
        Noodles  |  150
        Sushi   |  270
        Bakery  |  350
        """
        #return 
        
    def place_order(self, customer_name, order_items):
        """
        Return orders log after order placed by a customer with status as "Placed", otherwise return "order placement failed"
        Format:
        orders_log = {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity"}, status = "Placed}}
        """
        return None
        
    def pickup_order(self, order_id):
        """
        status: Picked Up	
        Return the changed status of the order: {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity"}, status = "Picked Up"}}
        """
        return None
        
    def deliver_order(self, order_id):
        """
        status: Delivered
        Return the delivery status of order (delivered or not delivered)
        """
        return None
        
    def modify_order(self, order_id, new_items):
        """
        Return the modified order with items available in menu only if the order is not picked up:
        {order_id: {"customer_name":ABC, "order_items":{"item1":"Quantity", new_items}, status = "Placed"}}
        """
        return None
    
    def generate_bill(self, order_id):
        """
        if the sum of all items > 1000
        Amount = Sum of all items placed + 10% of total sum
        if sum of all items < 1000
        Amount = Sum of all items placed + 5% of total sum
        Return the total bill amount
        """
        return None
        
    def cancel_order(self, order_id):
        """
        Cancel order items for the customer if the order is not Picked Up and remove order details from orders log
        Return the order logs. For example, if you have 3 orders, but the third order is cancelled, you need remove this from the orders log and just return the first two orders:
        {1: {"customer_name":"clientA", "order_items":{"Burger":1,"Pasta":2},"status":"Delivered"}, 2: {"customer_name":"clientB", "order_items":{"Salad":2,"Sushi":4, "Beverages":6, "Bakery":2},"status":"Placed"}}
        """
        return None

x = FoodDeliverySystem.display_menu(1)
print(x)
