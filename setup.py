from distutils.core import setup

setup(
    name='bfdbg',
    py_modules = ["bfdbg"],
    version='0.6',
    description = "Simple brainfuck debugger",
    author = "Ben Herzog",
    author_email = "benherzog11235@gmail.com",
    keywords = ["brainfuck","debugger"],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)


