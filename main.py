#!/usr/bin/env pypy3

# This is a new config generator for my projects.
# NOTE: The config parser/generator is for python only.
import os
projname = "kproj"

def parseFile(projname):
    file = open(projname, "r")
    fin = file.read().split()
    # print(fin)
    ip = 0
    title_stack = []
    buildname = "build.sh"
    out = open(buildname, 'w')
    out.write("#!/bin/sh\n\n")
    for ip in range(len(fin)):
        command = fin[ip]
        if command == 'title':
            title_stack.append(fin[ip + 1].replace('"', "")) 
            a = title_stack.pop()
            out.write(f"cp main.py {a}\n")
            out.write(f"chmod +x ./{a}\n")
            ip += 1
        elif command == 'file':
            os.system(f"touch {fin[ip+1]}")
        elif command == 'project':
            if fin[ip + 1] == 'run':
                out.write(f"./{a}") 
            ip += 1
        elif command.startswith('"'):
            continue
            ip += 1
        elif command == 'run':
            continue
            ip += 1
        else:
            print(f"Command `{command}` not recognized.")
            ip += 1
        ip += 1
if __name__ == '__main__':
    if os.path.exists(projname):
        print("NOTE: You already have a project config inside your directory, using that config...")
        parseFile(projname)
    else: 
        print("This is the first time that we need to create the file for you.")
        os.system(f"touch {projname}")
        parseFile(projname)