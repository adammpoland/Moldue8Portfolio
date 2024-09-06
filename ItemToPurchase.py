class ItemToPurchase:
    #attributes
    item_name = "none"
    item_price = 0
    item_quantity = 0
    item_description = "none"

    def __init__(self, item_name, item_price, item_quantity, item_description):
        self.item_name = item_name
        self.item_price =  item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    
    def print_item_cost(self):
        unformatted_cost = self.item_quantity * self.item_price
        cost = "${:,.2f}".format(unformatted_cost)
        price = "${:,.2f}".format(self.item_price) 
        print(self.item_name + " " + str(self.item_quantity)  + " @ " + price +" = "  +cost)
