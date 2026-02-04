🧠 Problem Statement

You are given an array people where people[i] is the weight of the iᵗʰ person.
There are an infinite number of boats, and each boat can carry at most two people at the same time, provided the sum of their weights is at most limit.

Return the minimum number of boats required to carry every person.

💡 Approach: Two-Pointer Greedy
Key Observations

Each boat can carry at most two people.

To minimize the number of boats, always try to pair the lightest person with the heaviest person.

Sort the array to facilitate pairing.

🚀 Algorithm

Sort the people array in ascending order.

Initialize two pointers:

i → start (lightest person)

j → end (heaviest person)

While i <= j:

If people[i] + people[j] <= limit:

Pair them → move both pointers (i++, j--)

Else:

Heaviest person goes alone → move j--

Increment boats count

Return total boats.

⏱️ Complexity Analysis

Time Complexity: O(n log n) → due to sorting

Space Complexity: O(1) → only constant extra space used
