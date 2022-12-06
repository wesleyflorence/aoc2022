import re
from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Operation:
    count: int
    start: int
    dest: int

def parse_crates():
    input_data = open("input/05.input").read()
    stack_text, instructions = [part.split("\n") for part in input_data.split("\n\n")]
    stacks = int(max(stack_text.pop()))

    supply = defaultdict(list)
    for row in stack_text:
        for col, box in enumerate(row[1::4]):
            if box != " ":
                supply[col+1].insert(0, box)

    operations = []
    for op in instructions:
        if not op: continue
        values = re.findall(r'move (.*?) from (.*?) to (.*)', op)[0]
        values = [int(x) for x in values]
        operations.append(Operation(*values))
    return (stacks, supply, operations)
    
def move_crates(op: Operation, crates, useQueue=False):
    count = op.count
    stack = []
    while count:
        stack.append(crates[op.start].pop())
        count -= 1
    if useQueue: stack = stack[::-1]
    for crate in stack:
        crates[op.dest].append(crate)
    return crates

def organize_supply_stacks(is9001: bool):
    stacks, crates, ops = parse_crates()
    for op in ops:
        crates = move_crates(op, crates, is9001)
    return "".join(crates[s+1].pop() for s in range(stacks))

def part_one():
    return organize_supply_stacks(False)

def part_two():
    return organize_supply_stacks(True)

print(part_one())
print(part_two())
