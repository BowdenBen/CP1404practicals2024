"""
What did you see on line 1? 7
What was the smallest number you could have seen, what was the largest? smallest = 5, largest = 20

What did you see on line 2? 9
What was the smallest number you could have seen, what was the largest? smallest = 3, largest = 9
Could line 2 have produced a 4? No, because the step size of 2 excludes even numbers from the sequence
(only odd numbers within the range are possible).

What did you see on line 3? 3.2673701941721554
What was the smallest number you could have seen, what was the largest? smallest = 2.5, largest = 5.5
"""

"""
Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
import random

print(random.randint(1, 100)) # print random integer from 1 to 100 inclusive.
