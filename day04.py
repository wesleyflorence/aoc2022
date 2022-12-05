import aoc

def get_range(assignment):
    start, end = assignment.split('-')
    return set(range(int(start), int(end)+1))

def parse_assignments():
    assignements = []
    for pair in aoc.read_input("04"):
        first, second = pair.split(',')
        assignements.append((get_range(first), get_range(second)))
    return assignements

def part_one():
    count = 0
    for first, second in parse_assignments():
        if first.issubset(second) or second.issubset(first):
            count += 1
    return count

def part_two():
    count = 0
    for first, second in parse_assignments():
        if first.intersection(second) or second.intersection(first):
            count += 1
    return count

print(part_one())
print(part_two())
