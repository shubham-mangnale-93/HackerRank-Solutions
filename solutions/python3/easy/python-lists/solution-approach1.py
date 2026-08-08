# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Problem     Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-08, 12:59 p.m.
# ──────────────────────────────────────────────────

import sys

if __name__ == '__main__':
    try:
        # Read the total number of commands
        line = sys.stdin.readline()
        if not line:
            sys.exit()
            
        N = int(line.strip())
        my_list = []
        
        for _ in range(N):
            command_line = sys.stdin.readline()
            if not command_line:
                break
                
            parts = command_line.split()
            if not parts:
                continue
                
            command = parts[0]
            args = parts[1:]
            
            if command == "print":
                print(my_list)
            else:
                int_args = list(map(int, args))
                getattr(my_list, command)(*int_args)
                
    except (EOFError, ValueError):
        pass
