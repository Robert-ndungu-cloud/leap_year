class SimpleClass:

    ...

class Classey:

    varia = 2

    def method1(self):
        print(self.varia)

object_one = Classey()
object_two = Classey()
object_one.varia = 3
object_two.varia = 5
#print(object_one.varia)
#print(object_two.varia)



class Transport:
    def __init__(self, air, water):
        self.air = air
        self.water = water


obj_transport = Transport("belunga", "Hovercart")
#print(obj_transport.air,obj_transport.water)

object_two = Transport("jet", "boat")
#print(object_two.air,object_two.water)


class Person:
    def __init__(self, fname , lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname,self.lname)

x= Person("John", "Doe")
y= Person("Mary", "Doe")
#x.printname()
#y.printname()

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

#calculate the no of items in our cart/list
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total


cart = ShoppingCart()

#add items into our cart
cart.add_item("Kiwi", 100)
cart.add_item("papaya", 200)
cart.add_item("orange", 78)

print("current items in cart")
for item in cart.items:
    print(item[0], "-" ,item[1])

total_qty = cart.calculate_total()
print("total Quantity: ",total_qty)