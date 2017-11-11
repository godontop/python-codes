class Pizza:

    def __init__(self, toppings):
        self.toppings = toppings

    @property
    # One common use of a property is to make an attribute read-only.
    def pineapple_allowed(self):
        return False

pizza = Pizza(["cheeese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
# AttributeError: can't set attribute
