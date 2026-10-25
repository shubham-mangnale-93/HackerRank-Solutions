# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
# Problem     String Formatting
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-25, 01:21 p.m.
# ──────────────────────────────────────────────────

def print_formatted(number):
    # your code goes here
    width = len(bin(number)) - 2  # bin() adds a "0b" prefix
    for i in range(1, number + 1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")


