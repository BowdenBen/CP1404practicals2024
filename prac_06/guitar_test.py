from guitar import Guitar


# Create two Guitar objects
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 250.00)


# Test get_age() method
print(f"Gibson L-5 CES get_age() - Expected 102. Got", guitar1.get_age())
print(f"Another Guitar get_age() - Expected 11. Got", guitar2.get_age())

# Test is_vintage() method
print(f"Gibson L-5 CES is_vintage() - Expected True. Got", guitar1.is_vintage())
print(f"Another Guitar is_vintage() - Expected False. Got", guitar2.is_vintage())