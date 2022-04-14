# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]


# -------------------------
# Write your solution here:
# -------------------------
if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add_item("bananas", 10)
    my_list.add_item("apples", 5)
    my_list.add_item("pineapple", 1)

    print(my_list.number_of_items())

    # the items on the shopping list are indexed from 1
    for i in range(1, my_list.number_of_items()+1):
        item = my_list.item(i)
        amount = my_list.amount(i)
        print(f"{item}: {amount} units")

    print(total_units(my_list))
    
