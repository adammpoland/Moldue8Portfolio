from ItemToPurchase import ItemToPurchase

class ShoppingCart:
    #attributes
    customer_name = "none"
    current_date = "January 1, 2020"
    cart_items = []

    def __init__(self, customer_name, current_date ):
        self.current_date  = current_date
        self.customer_name =  customer_name
    
    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print(item_name + " Not found in cart. Nothing Removed")

    def modify_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                item.item_quantity = int(input("Please enter a new quantity"))
                return
        print(item_name + " Not found in cart.")   


    def get_num_items_in_cart(self):
        return len(self.cart_items)
    
    def get_cost_of_cart(self):
        total = 0.0
        for item in self.cart_items:
            total += (item.item_price * item.item_quantity)
        cost = "${:,.2f}".format(total)
        return cost
    
    def print_total(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date )
        print("Number of Items: " + str(self.get_num_items_in_cart()))
        if len(self.cart_items) > 0:
            for item in self.cart_items:
                item.print_item_cost()
            print("Total: " + str(self.get_cost_of_cart()))
        else:
            print("SHOPPING CART IS EMPTY")
    def print_descriptions(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date )
        print("Item Descriptions")
        for item in self.cart_items:
            print(item.item_name + ": " + str(item.item_description))



