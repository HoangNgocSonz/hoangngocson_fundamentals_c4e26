def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else :
        inventory[fruit] = quantity
    return

def test(s):
    if s:
        print ("true")
    else:
        print("false")
    return



new_inventory={}

add_fruit(new_inventory, "strawberries",10)

test("strawberries" in new_inventory)
test(new_inventory["strawberries"]==10)
add_fruit(new_inventory, "strawberries",25)
test(new_inventory["strawberries"]==35)
