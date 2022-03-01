# Chapter 11 - Classes
# 3. Project
# 1. Basta Fazoolin'

# You've started position as the lead programmer for the family-style Italian
# resturant Basta Fazoolin' with My Heart. The resturant has been doing fantastically
# and seen a lot of growth lately. You've been hired to keep things organized.

# Tasks
# Actually, this list is sooo long I don't care about writing it all down. 

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        welcome = "{} menu is available from {} to {}".format(self.name, self.start_time, self.end_time)
        return welcome
    
    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return bill
    
brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)
early_bird = Menu("Early-Bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 15, 18)
dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17, 23)
kids = Menu("Kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

print(brunch)
print(early_bird)
print(dinner)
print(kids)

print("\n")

print(brunch.calculate_bill(['pancaces', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'vegan mushroom ravioli']))

# First half. Had to get some help with the calculate_bill method, but I was on the right track, just had to get down the self.
# Need a small break to pick up GF. Will commit the first half.
