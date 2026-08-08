# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
# Problem     Tuples 
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-08, 01:13 p.m.
# ──────────────────────────────────────────────────

def old_tuple_hash(t):
    MASK = 0xFFFFFFFFFFFFFFFF  # 64-bit mask
    length = len(t)
    x = 0x345678
    mult = 1000003
    for i, item in enumerate(t):
        remaining = length - i - 1
        y = hash(item)
        x = ((x ^ y) * mult) & MASK
        mult = (mult + (82520 + 2 * remaining)) & MASK
    x = (x + 97531) & MASK
    # convert back to signed 64-bit
    if x >= 2**63:
        x -= 2**64
    if x == -1:
        x = -2
    return x

n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(old_tuple_hash(t))
