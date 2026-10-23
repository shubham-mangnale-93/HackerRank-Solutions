# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
# Problem     Company Logo
# Difficulty  Medium
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-23, 11:42 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
count = {}
for ch in s:
    count[ch] = count.get(ch, 0) + 1

result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

for ch, c in result[:3]:
    print(ch, c)
