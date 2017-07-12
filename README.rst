=====
bfdbg
=====

**Bbfdg** is a simple debugger for Brainfuck, written in python. Sample usage:

.. code:: python

    #!/usr/bin/python3
    import bfdbg
    dbg = bfdbg.BrainfuckDebugger()
    dbg.load_code(
        "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++."
        ">>.<-.<.+++.------.--------.>>+.>++."
    )
    while not dbg.is_halted_state():
        dbg.step()

    dbg.report()
    
Installation
============

Build from source:
------------------
.. code:: bash
    
    git clone https://github.com/BenH11235/bfdbg
    sudo python3 setup.py install

