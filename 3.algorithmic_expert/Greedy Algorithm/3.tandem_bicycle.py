# Problem Name: Tandem Bicycle

# Problem Description:
# A tandem bicycle is a bicycle that's operated by two people: person A and person B. Both peope pedal the bicycle, but the person that pedals faster dictates the speed of the bicycle. So if person A is pedals at a speed of 5, and person B pedals at a speed of 4, the tandem bicycle moves at a speed of 5(i.e tandem speed = max(speedA, speedB)).

# You're given two lists of positive integers: one that contains the speeds of riders wearing red-shirts and one that contains the speeds of riders wearing blue-shirts. Each rider is represented by a single positive integer, which is the speed that they pedal a tandem bicycle at. Both lists have the same length, meaning that there are as many red-shirt riders as there are blue-shirt riders. Your goal is to pair every rider wearing a red-shirt with rider wearing a blue-shirt to operate a tandem bicycle.

# Write a function that returns the maximum possible total speed or the minimum possible total speed of all the tandem bicycles being ridden based on an input parameters, fastest. If fastest = True, your function should return the maximum possible total speed; otherwise it should return the minimum total speed. 

# "Total Speed" is defined as the sum of the speeds of all the tandem bicycle being ridden. For example, if there are 4 riders (2 red-shirt riders and 2 blue-shirt riders) who have speeds of 1,3,4,5, and if they're paired on tandem bicycles as follows: [1, 4], [5, 3], then the total speed of these tandem bicyles is 4 + 5 = 9.
  
####################################
# Sample Input:
#   redShirtSpeeds = [5, 5, 3, 9, 2]
#   blueShirtSpeeds = [3, 6, 7, 2, 1]
#   fastest = true

# Sample Output: 32

####################################
"""
Explain the solution:
- The brute-force approach to solve this problem is to generate every possible set of pairs of riders and to determine the total speed that each of these sets generates. This solution does not work but, it isn't optimal. Can you think of better way to solve this problem?

- Try looking at the input arrays in sorted order. How might this help you solve the problem?

- When generating the maximum total speed, you want to pair the slowest red-shirt riders with the fastest blue-shirt riders and vice versa, so as to always take advantage of the largest speeds. When generating the minimum total speed, you want to pair the fastest red-shirt riders with the fastest blue-shirt riders, so as to "eliminate" a large speed by pairing it with a another large(larger) speed.

- Sort the input arrays in place, and follow the strategy discussed in Hint #3. With the inputs sorted, you can find the slowest and largest speeds from each shirt color in constant time.

- O(n(log(n)) time | O(1) space - where n is the length of the tandem bicycles

##################
Detailed explanation of the Solution:

create a function of tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    sort the redShirtSpeeds and blueShirtSpeeds arrays in place
    if not fastest:
        call the function reverseArrayInPlace(redShirtSpeeds)

    totalSpeed is initialized to 0
    for idx in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[idx] # array in sorted ascending order
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - 1 - idx] # Reverse the blueShirtSpeeds array in descending order
        totalSpeed += max(rider1, rider2)

    return totalSpeed

create a function of reverseArrayInPlace(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
"""
####################################

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if not fastest:
        reverseArrayInPlace(redShirtSpeeds)

    totalSpeed = 0
    for idx in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[idx] # array in sorted ascending order
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - 1 - idx] # Reverse the blueShirtSpeeds array in descending order
        totalSpeed += max(rider1, rider2)

    return totalSpeed


def reverseArrayInPlace(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

print(tandemBicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True))