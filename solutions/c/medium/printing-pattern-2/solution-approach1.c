// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/challenges/printing-pattern-2/problem?isFullScreen=true
// Problem     Printing Pattern Using Loops
// Difficulty  Medium
// Subdomain   Conditionals and Loops
// Platform    HackerRank
// Language    c
// Status      Accepted
// Submitted   2026-08-21, 11:57 p.m.
// ──────────────────────────────────────────────────

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);
  	// Complete the code to print the pattern.
    int size = 2 * n - 1;   

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {

            int top = i;
            int left = j;
            int bottom = size - 1 - i;
            int right = size - 1 - j;

            int dist = top;
            if (left < dist) dist = left;
            if (bottom < dist) dist = bottom;
            if (right < dist) dist = right;

            int value = n - dist;

            printf("%d", value);

            if (j != size - 1) {
                printf(" ");
            }
        }
        printf("\n");    
    }
    return 0;
}
