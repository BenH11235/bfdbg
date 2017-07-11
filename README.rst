=====
bfdbg
=====

**Bbfdg** is a simple debugger for Brainfuck, written in python. Sample usage:

.. code:: python

    #!/usr/bin/python3
    import bfdbg
    dbg = bfdbg.BrainfuckDebugger()
    dbg.load_code(">+>++>+++>++++")
    dbg.step()
    dbg.report()

Installation
============

Build from source:
------------------
.. code:: bash
    
    git clone https://github.com/BenH11235/bfdbg

