=====
bfdbg
=====

**Bbfdg** is a simple debugger for Brainfuck, written in python. Sample usage:
    
    ``#!/usr/bin/env python

    import bfdbg

    dbg = bfdbg.BrainfuckDebugger()
    dbg.load_code(">+>++>+++>++++")
    dbg.report()
    dbg.step()
    dbg.report()``



Installation
============

Build from source:
------------------

``git clone https://github.com/BenH11235/bfdbg``

