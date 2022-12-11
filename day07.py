import aoc

class FileSystem():
    def __init__(self):
        self.sys = {}
        self.cur = self.sys
        self.stack = []

    def is_cd(self, line: list[str]):
        return True if line[0] == "$" and line[1] == "cd" else False
    
    def is_ls(self, line: list[str]):
        return True if line[0] == "$" and line[1] == "ls" else False
    
    def lookup(self, path: list[str]) -> dict:
        pointer:dict = self.sys
        for i, p in enumerate(path):
            if p not in pointer:
                pointer[p] = {}
                pointer[p][".."] = path[i-1]
                pointer[p]["_size"] = 0
            pointer = pointer[p]
        return pointer

    def add_size(self, size):
        node = self.sys
        for path in self.stack:
            node = node[path]
            node["_size"] += int(size)
    
    def cd(self, line):
        if line[2] == "..":
            self.stack.pop()
        else:
            self.stack.append(line[2])
        return self.lookup(self.stack)
    
    def ls(self, commands, i):
        while i < len(commands) and not self.is_cd(commands[i]):
            if self.is_ls(commands[i]): pass
            elif commands[i][0] == "dir":
                if commands[i][1] not in self.cur:
                    self.cur[commands[i][1]] = {}
                    self.cur[commands[i][1]][".."] = self.stack[len(self.stack)-1]
                    self.cur[commands[i][1]]["_size"] = 0
            else:
                self.cur[commands[i][1]] = commands[i][0]
                self.add_size(commands[i][0])
            i += 1
    
    def build_filetree(self, term_output: list[str]):
        commands = [l.split(" ") for l in term_output]
        for i in range(len(commands)):
            line = commands[i]
            if self.is_cd(line): 
                self.cur = self.cd(commands[i])
            if self.is_ls(line):
                self.ls(commands, i)
        return self.sys


def part_one():
    def get_candidate_size(dir):
        total = 0
        for k, val in dir.items():
            if k == "_size" and val < 100_000:
                total += val
            elif isinstance(val, dict):
                total += get_candidate_size(val)
        return total

    return get_candidate_size(FileSystem().build_filetree(aoc.read_input("07")))


def part_two():
    space = 70_000_000
    update = 30_000_000
    fs = FileSystem().build_filetree(aoc.read_input("07"))
    to_remove = abs(space - update - fs["/"]["_size"])

    def get_candidate_size(dir, remove):
        total = []
        for k, val in dir.items():
            if k == "_size" and val > remove:
                total.append(val)
            elif isinstance(val, dict):
                total += get_candidate_size(val, remove)
        return total

    return min(get_candidate_size(fs, to_remove))

print(part_one())
print(part_two())
