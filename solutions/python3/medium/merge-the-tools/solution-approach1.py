# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
# Problem     Merge the Tools!
# Difficulty  Medium
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-20, 12:23 p.m.
# ──────────────────────────────────────────────────

def merge_the_tools(string, k):
    # your code goes here
    # Iterate through the string in chunks of size k
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        
        # Track seen characters to remove duplicates while preserving order
        seen = set()
        result = []
        
        for char in substring:
            if char not in seen:
                seen.add(char)
                result.append(char)
                
        # Print the processed substring joined back into a string
        print("".join(result))

