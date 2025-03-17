# Introduction

**Bbfdg** is a simple debugger for Brainfuck, written in python.
    
# Installation & Usage

Decide whether you trust this repo. If you do, then:

```bash
python -m pip install  git+https://github.com/BenH11235/bfdbg
```

You can then do:

```python
import bfdbg
dbg = bfdbg.BrainfuckDebugger()
dbg.load_code(
    "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++."
    ">>.<-.<.+++.------.--------.>>+.>++."
)
while not dbg.is_halted_state():
    dbg.step()

dbg.report()
```

