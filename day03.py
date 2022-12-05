import aoc
from functools import reduce

def get_priority(compartment):
    priority = 0
    for item in compartment:
        if item < 'a':
            priority += (ord(item) - ord('A')) + 27
        else:
            priority += (ord(item) - ord('a')) + 1
    return priority

def part_one():
    rucksacks = []
    for sack in aoc.read_input("03"):
        mid = len(sack) // 2
        rucksacks.append(set(sack[0:mid]).intersection(sack[mid:]))
    return reduce(lambda base, el: base + get_priority(el), rucksacks, 0)

def part_two():
    team_size = 3
    rucksacks = []
    team = []
    for i, sack in enumerate(aoc.read_input("03")):
        team.append(set(sack))
        if i % team_size == team_size-1:
            rucksacks.append(get_priority(set.intersection(*team)))
            team = []
    return sum(rucksacks)
    
print(part_one())
print(part_two())
