inventory = {'arrows': 12, 'gold coins': 42,
             'rope': 1, 'torches': 6,
             'dagger': 1, }


def display_inventory(inventory):
    print("Inventory:")
    amount = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        amount += v
    print('Total number of items: ' + str(amount))


display_inventory(inventory)

print()  # to give a space


def add_to_inventory(inventory, added_items):
    for loot in added_items:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    return(inventory)


inv = {'gold coins': 42, 'rope': 1}
dragon_loot = ['gold coins', 'dagger', 'gold coins', 'gold coins', 'ruby']
inv = add_to_inventory(inv, dragon_loot)

display_inventory(inv)

# https://github.com/IFinners/automate-the-boring-stuff-projects/blob/master/Chapter%2005/Game_Inventory.py
