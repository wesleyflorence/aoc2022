import aoc
from enum import Enum

Move = Enum('Move', ['ROCK', 'PAPER', 'SCISSORS'])

class Outcome(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0

def play(prompt, resp):
    score = resp.value
    result = resp.value - prompt.value
    if result == 0:
        score += Outcome.DRAW.value
    elif (result % len(Move)) == 1:
        score += Outcome.WIN.value
    else:
        score += Outcome.LOSE.value
    return score

def parse_guide(lookup):
    guide = []
    for line in aoc.read_input("02"):
        guide.append((lookup[line[0]], lookup[line[2]]))
    return guide

def desired_move(prompt, outcome):
    if outcome == Outcome.WIN:
        resp = Move((prompt.value % len(Move)) + 1)
    elif outcome == Outcome.LOSE:
        resp = Move(((prompt.value - 2) % len(Move)) + 1)
    else:
        resp = prompt
    return (prompt, resp)

def part_one():
    lookup = {
        "A" : Move.ROCK,
        "B" : Move.PAPER,
        "C" : Move.SCISSORS,
        "X" : Move.ROCK,
        "Y" : Move.PAPER,
        "Z" : Move.SCISSORS
    }
    total = 0
    for prompt, resp in parse_guide(lookup):
        total += play(prompt, resp)
    return total

def part_two():
    lookup = {
        "A" : Move.ROCK,
        "B" : Move.PAPER,
        "C" : Move.SCISSORS,
        "X" : Outcome.LOSE,
        "Y" : Outcome.DRAW,
        "Z" : Outcome.WIN
    }
    total = 0
    for prompt, resp in parse_guide(lookup):
        total += play(*desired_move(prompt, resp))
    return total

print(part_one())
print(part_two())
