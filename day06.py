import aoc

def find_marker(s: str, end: int):
    for start, _ in enumerate(s):
        marker = s[start:start+end]
        if len(list(set(marker))) == end:
            return start + end
    return -1

def solve(length: int):
    return find_marker(aoc.read_input("06")[0], length)

def part_one():
    return solve(4)

def part_two():
    return solve(14)

print(part_one())
print(part_two())
