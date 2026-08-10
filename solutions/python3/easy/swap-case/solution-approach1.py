# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
# Problem     sWAP cASE
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-10, 10:34 p.m.
# ──────────────────────────────────────────────────

def swap_case(s):
    swapped = []
    for char in s:
        if char.islower():
            swapped.append(char.upper())
        elif char.isupper():
            swapped.append(char.lower())
        else:
            swapped.append(char)
    return "".join(swapped)


