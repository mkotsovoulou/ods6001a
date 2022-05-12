# DO NOT CHANGE THE CODE OF THE ShoppingList CLASS 
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)
    
    # if the item exists, remove it and add it again with the total qty
    def add_item(self, product: str, qty: int):
        previous_qty = 0
        for i in range(0, len(self.products)):
            if self.products[i][0] == product:
                previous_qty = self.products[i][1]
                self.products.pop(i)
        self.products.append((product, previous_qty + qty))

    def item(self, n: int):
        return self.products[n - 1][0]

    def qty(self, n: int):
        return self.products[n - 1][1]
    
## MAIN PROGRAM

def total_units(my_list):
    pass

def print_shopping_list(my_list):
    pass

if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add_item("bananas", 10)
    my_list.add_item("bananas", 12)
    my_list.add_item("apples", 5)
    my_list.add_item("apples", 2)
    my_list.add_item("pineapple", 1)

    # print("Total number of Items: ", my_list.number_of_items())
    # print("Shopping List", my_list.products)
   
    # Display all the items in the shopping list 
    # (notice that the items in the list are indexed from 1)
    for i in range(1, my_list.number_of_items()+1):
        item = my_list.item(i)
        quantity = my_list.qty(i)
        print(f"{item}: {quantity} units")

    # total_units is the function you have to define!
    print(total_units(my_list))
    
