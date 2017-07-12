from distutils.core import setup

setup(
    name='bfdbg',
    version='3.0',
    packages=["bfdbg"],
    package_dir = {"bfdbg":"src"},
    description = "Simple brainfuck debugger",
    author = "Ben Herzog",
    author_email = "benherzog11235@gmail.com",
    keywords = ["brainfuck","debugger"],
    license='LICENSE.txt',
    long_description=open('README.rst').read(),
)


