#!/usr/bin/python
from sys import argv, stdout
import re

glossary = {
        ">": "my",
        "<": "in",
        "+": "glock",
        "-": "rari",
        "[": "Ra",
        "]": "Ri",
        ".": "I",
        ",": "gotta"
    }

with open(argv[1], "r") as file:
    for char in list(file.read()):
        if char != "" and char != "\n":
            stdout.write(glossary[char])
    print("")
