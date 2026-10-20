# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
# Problem     Mutations
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-20, 12:21 p.m.
# ──────────────────────────────────────────────────

def mutate_string(string, position, character):
    # Slice the string before the position, add the new character, 
    # and append the rest of the string after the position
    return string[:position] + character + string[position+1:]
    

