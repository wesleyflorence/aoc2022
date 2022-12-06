import re
from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Op:
    count: int
    start: int
    dest: int

def parse_crates():
    ops = []
    crates = []
    stacks = 0
    for line in open(f"input/05.input"):
        line = line.rstrip('\n')
        if line and line[:4] == "move":
            ops.append(line)
        elif "[" in line:
            crates.append(line)
        elif line:
            stacks = int(max(line))

    supply = defaultdict(list)
    for row in crates:
        for col in range(1, stacks*4 + 1, 4):
            if row[col] != " ":
                supply[((col-1)//4)+1].insert(0, row[col])

    parsed_ops = []
    for op in ops:
        values = re.findall(r'move (.*?) from (.*?) to (.*)', op)[0]
        values = [int(x) for x in values]
        parsed_ops.append(Op(*values))
    return (stacks, supply, parsed_ops)
    
def move_crates(op: Op, crates, useQueue=False):
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
    top_crates = ""
    stacks, crates, ops = parse_crates()
    for op in ops:
        crates = move_crates(op, crates, is9001)

    for stack in range(1, stacks+1):
        top_crates += crates[stack].pop()

    return top_crates

def part_one():
    return organize_supply_stacks(False)

def part_two():
    return organize_supply_stacks(True)

print(part_one())
print(part_two())
