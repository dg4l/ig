#!/bin/python
import re
import sys
import subprocess

out_file_name = "ig_output"

pattern = r'^\s*#include\s*[<"]([^">]+)[>"]'
buf = "strict digraph g {\nnode [shape=rectangle]\nrankdir=TB\n"
filenames = sys.argv[1:]
for filename in filenames:
    with open(filename, 'r') as f:
        contents = f.read()
        matches = re.findall(pattern, contents, re.MULTILINE)
        for match in matches:
            buf += f"\"{filename}\" -> \"{match}\";\n"

if len(buf) > len("strict digraph g {\n"):
    buf = buf[:-1]
    buf += "\n}"
    with open(f"{out_file_name}.dot", "w") as f:
        f.write(buf)
    subprocess.run(["dot", "-Tsvg", f"{out_file_name}.dot", "-o", f"{out_file_name}.svg"])
