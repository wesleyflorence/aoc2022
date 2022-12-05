import aoc
from collections import defaultdict

def build_inventory():
    elf = 0
    inventory = defaultdict(int)
    for calorie in aoc.read_input("01"):
        if calorie == '\n':
            elf += 1
        else:
            inventory[elf] += int(calorie)
    return inventory

def part_one():
    return max(build_inventory().values())

def part_two(top: int):
    total = 0
    inventory = build_inventory()
    while top:
        key = max(inventory, key=lambda k: inventory[k])
        total += inventory.pop(key)
        top -= 1
    return total


print(part_one())
print(part_two(3))
