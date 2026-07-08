// ──────────────────────────────────────────────────
// Problem     Students Marks Sum
// Difficulty  Easy
// Subdomain   Functions
// Platform    HackerRank
// Language    c
// Status      Accepted
// Submitted   2026-07-08, 08:32 p.m.
// ──────────────────────────────────────────────────



//Complete the following function.

int marks_summation(int* marks, int number_of_students, char gender) {
  //Write your code here.
   int sum = 0;
    
    // Boys are at even indices (0, 2, 4...), Girls are at odd indices (1, 3, 5...)
    int start_index = (gender == 'b') ? 0 : 1;
    
    // Loop through the array, skipping one element each time to stay on the same gender
    for (int i = start_index; i < number_of_students; i += 2) {
        sum += marks[i];
    }
    
    return sum;
}

