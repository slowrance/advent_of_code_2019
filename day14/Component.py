from __future__ import annotations
from typing import List



class Component:
    def __init__(self, name):
        self.name = name
        self.out_qty = 0
        self.inputs = {}

    def __repr__(self):
        return f'Component({self.name})'

    def create(self, qty_to_make: int, inventory: dict, components: List[Component]):
        # if self.inputs.get('ORE'):
        #     # conversions_needed = -(-qty_to_make // self.out_qty)
        #     conversions_needed = qty_to_make
        #     ore_needed = self.inputs['ORE'] * conversions_needed
        #
        #     inventory['ORE'] += ore_needed
        #     inventory[self.name] = inventory[self.name] + (self.out_qty * qty_to_make) - (qty_to_make * conversions_needed)
        #     return inventory

        # else:
        for k, v in self.inputs.items():

            if self.inputs.get('ORE'):

                # conversions_needed = -(-qty_to_make // self.out_qty)
                # conversions_needed = qty_to_make
                ore_needed = self.inputs['ORE'] * qty_to_make

                inventory['ORE'] += ore_needed
                inventory[self.name] = inventory[self.name] + (self.out_qty * qty_to_make)
                return inventory
            conversions_needed = -((-v * qty_to_make) // components[k].out_qty)
            if inventory[k] >= conversions_needed * v:
                inventory[k] -= conversions_needed * v
                continue
            inventory = components[k].create(conversions_needed, inventory, components)
            inventory[k] -= qty_to_make * self.inputs[k]
        # inventory[self.name] = inventory[self.name] + self.out_qty - qty_to_make
        return inventory

