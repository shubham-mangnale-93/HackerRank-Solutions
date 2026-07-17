# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
# Problem     collections.Counter()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-17, 09:59 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

# Read total number of shoes
num_shoes = int(input())

# Read shoe sizes and convert them to a list of integers
shoe_sizes = list(map(int, input().split()))

# Create a inventory counter
inventory = Counter(shoe_sizes)

# Read total number of customers
num_customers = int(input())

total_earned = 0

# Process each customer's request
for _ in range(num_customers):
    size, price = map(int, input().split())
    
    # Check if the shoe size is available in stock
    if inventory[size] > 0:
        total_earned += price
        inventory[size] -= 1  # Reduce inventory by one shoe

# Print the final earnings
print(total_earned)
