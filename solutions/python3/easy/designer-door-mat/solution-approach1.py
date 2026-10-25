# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
# Problem     Designer Door Mat
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-25, 01:18 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

# Top half: rows 1, 3, 5, ... n-2 repetitions of ".|."
for i in range(1, n, 2):
    print((".|." * i).center(m, "-"))

# Middle line
print("WELCOME".center(m, "-"))

# Bottom half: mirror of the top
for i in range(n - 2, 0, -2):
    print((".|." * i).center(m, "-"))
