# UniqueCombinations
This project is meant  to give the 30 'most unique' combinations of 2 input lists with conditions.

List1 = ['A', 'B', 'C']
List2 = [1, 2, 3, 4, 5]

For a combination, all items can be used only once, where 'A' can only have 1 number, and 'B' and 'C' need to have 2 numbers

Examples are:
[A5, B14, C32]
[C13, B45, A2]
[B21, A3, C54]

The researchers find [A1, B2-3, C4-5] to resemble [A1, B3-3, C4-5] more than [C3-1, A5, B4-2]

An initial idea to find the 'most unique' is by comparing two combinations and use the lists with the lowest jaccard similarity score over a table by comparing every combination to another and then using the total 'dissymilation score'
