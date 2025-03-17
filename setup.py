from setuptools import setup, find_packages

setup(
    name="bfdbg",               # The package name
    version="0.1",                   # Initial version
    packages=find_packages(),        # Automatically find packages in the directory
    description="Compact Brainfuck debugger",
    author="Ben Herzog",
)
