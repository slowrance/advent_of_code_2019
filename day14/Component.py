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
        if self.inputs.get('ORE'):
            conversions_needed = -(-qty_to_make // self.out_qty)
            ore_needed = self.inputs['ORE'] * conversions_needed
            inventory['ORE'] += ore_needed
            return inventory
        if inventory[self.name] >= qty_to_make:
            inventory[self.name] -= qty_to_make
        else:
            for k, v in self.inputs.items():
                inventory = components[k].create(v, inventory, components)

