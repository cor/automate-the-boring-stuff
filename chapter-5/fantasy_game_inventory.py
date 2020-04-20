my_inventory = {'gold coin': 42, 'rope': 1}


def display_inventory(inventory):
    """Display an inventory"""
    print('Inventory:')
    for k, v in inventory.items():
        print(f'{v} {k}')
    print(f'Total number of items: {sum(inventory.values())}')


def add_to_inventory(inventory, added_items):
    """Add items to an inventory. Modifies the inventory parameter."""
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1


display_inventory(my_inventory)
add_to_inventory(my_inventory, ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'])
display_inventory(my_inventory)
