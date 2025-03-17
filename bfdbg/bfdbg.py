#! /usr/bin/python3
import sys
import argparse

class _expandingList(list):
    def stretch(self,i):
        if i>=len(self):
            self += [0] * ((i-len(self))+1)
    def __getitem__(self,i):
        self.stretch(i)
        return list.__getitem__(self,i)
    def __setitem__(self,i,j):
        self.stretch(i)
        return list.__setitem__(self,i,j)

class BrainfuckDebugger:
    def __init__(self):
        self.strip = _expandingList([])
        self.breakpoints = set([0])
        self.ip = 0
        self.dp = 0

    def load_code(self, code):
        self.code = list(code)

        #prepare bracket matching logic
        self.matches = {}
        stack = []
        for index, inst in enumerate(code):
            if inst == '[': 
                stack.append(index)
            if inst ==']': 
                match = stack.pop()
                #support matching both [ to ] and vice-versa
                self.matches[match] = index
                self.matches[index] = match

    def load_from_file(self, fname):
        with open(fname, "r") as fh:
            self.load_code(fh.read().splitlines()[0])

    def report(self):
        print(["({})".format(x) if n==self.dp else x for (n,x) in enumerate(self.strip)])
        print("".join(["({})".format(y) if n==self.ip else y for (n,y) in enumerate(self.code)]))
        if self.is_halted_state():
            print("Machine halted")

    def is_halted_state(self):
        return self.ip >= len(self.code)


    def step(self):
        if self.is_halted_state(): return
        instruction = self.code[self.ip]
        if instruction == '+': self.strip[self.dp] += 1
        if instruction == '-': self.strip[self.dp] -= 1
        if instruction == '>': self.dp += 1
        if instruction == '<': self.dp -= 1
        if instruction == '.': print(chr(self.strip[self.dp]), end='')
        if instruction == ',': self.strip[self.dp] = ord(sys.stdin.read(1))
        if instruction == '[' and self.strip[self.dp] == 0:
            self.ip = self.matches[self.ip]        
        if instruction == ']' and self.strip[self.dp] != 0: 
            self.ip = self.matches[self.ip]
        self.ip += 1
    

    def prompt(self):
        cmd = input("> ")
        if cmd=="s": self.step()
        if cmd=="b":
            loc = int(input("Where to set/unset breakpoint? > "))
            self.breakpoints ^= set([loc])
        if cmd=="r":
            self.ip += 1
            while(self.ip not in self.breakpoints and self.ip<len(code)): step()
        if cmd=="q":
            exit(0)


def test_helloworld():
    dbg = BrainfuckDebugger()
    dbg.load_code(
        "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++."
        ">>.<-.<.+++.------.--------.>>+.>++."
    )
    while not dbg.is_halted_state():
        dbg.step()
    assert(dbg.strip == [0, 0, 72, 100, 87, 33, 10])
    



if __name__ == "__main__":
    cli = argparse.ArgumentParser(description="Debug Brainfuck code")
    cli.add_argument(
        "f",
        type=str,
        metavar="input_file",
        help="Path to input file containing brainfuck code"
    )
    args = cli.parse_args()
    debugger = BrainfuckDebugger()
    debugger.load_from_file(args.f)
    while(True):
        debugger.report()
        debugger.prompt()
