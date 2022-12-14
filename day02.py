import aoc
from enum import Enum

class Move(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    def getPoints(self):
        return self.value + 1

class Outcome(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0

def play(prompt: Move, resp: Move):
    score = resp.getPoints()
    result = resp.getPoints() - prompt.getPoints()
    if result == 0:
        score += Outcome.DRAW.value
    elif (result % len(Move)) == 1:
        score += Outcome.WIN.value
    else:
        score += Outcome.LOSE.value
    return score

def parse_guide(lookup: dict):
    guide = []
    for line in aoc.read_input("02"):
        guide.append((lookup[line[0]], lookup[line[2]]))
    return guide

def desired_move(prompt: Move, outcome: Outcome):
    if outcome == Outcome.WIN:
        resp = Move((prompt.value + 1) % len(Move))
    elif outcome == Outcome.LOSE:
        resp = Move((prompt.value - 1) % len(Move))
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
