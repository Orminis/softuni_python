"""
Create a class Catalogue. The __init__ method should accept the name of the catalogue (string).
Each catalogue should also have an attribute called products, an empty list.
The class should also have three more methods:
    add_product(product_name: str) - adds the product to the products' list
    get_by_letter(first_letter: str) - returns a list containing only the products that start with the given letter
    __repr__ - returns the catalogue info in the following format:

        "Items in the {name} catalogue:
        {item1}
        {item2}
        …
        {itemN}"
        The items should be sorted alphabetically in ascending order.
"""

class Catalogue:
    def __init__(self, name: str ):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        prod_list = [x for x in self.products if x[0] == first_letter]
        return prod_list

    def __repr__(self):
        items_list = '\n'.join(sorted(self.products, key=lambda x:x))
        return f"Items in the {self.name} catalogue:\n" \
               f"{items_list}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)