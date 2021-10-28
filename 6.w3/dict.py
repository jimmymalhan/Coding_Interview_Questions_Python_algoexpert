################################
# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
################################

# class Solution:
#     def __init__(self, dictionary):
#         self.dictionary = dictionary

#     def sort_ascending(self):
#         return sorted(self.dictionary.items(), key=lambda x: x[1])

#     def sort_descending(self):
#         return sorted(self.dictionary.items(), key=lambda x: x[1], reverse=True)

# def main():
#     dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#     print(Solution(dictionary).sort_ascending())
#     print(Solution(dictionary).sort_descending())

# if __name__ == '__main__':
#     main()

################################
# 2. Write a Python script to add a key to a dictionary. Go to the editor

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
################################

# class Dictionary:
#     def __init__(self, d:dict):
#         self.d = d
    
#     def addKey(self):
#         print(f'original_key:', self.d)
#         # method 1
#         # self.d[2] = 30

#         # method 2
#         # self.d.update({2:30})
#         # print(f'updated_key:', self.d)
#         # method 3
#         self.d = {**self.d, 2:30}
#         print(f'updated_key:', self.d)
        
# def main():
#     givenDict = Dictionary({0: 10, 1: 20})
#     givenDict.addKey()

# if __name__ == '__main__':
#   main()

################################
# 3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
################################

# class Dictionary(object):
#     def __init__(self, dic1: dict, dic2: dict, dic3: dict) -> None:
#         self.dic1 = dic1
#         self.dic2 = dic2
#         self.dic3 = dic3

#     def concatenate(self):
#         # print(self.dic1)
#         # print(self.dic2)
#         # print(self.dic3)

#         # method 1
#         # self.dic1.update(self.dic2)
#         # self.dic1.update(self.dic3)
#         # return self.dic1

#         # method 2
#         return {**self.dic1, **self.dic2, **self.dic3}


# def main():
#     givenDict = Dictionary({1:10, 2:20}, {3:30, 4:40}, {5:50,6:60})
#     print(givenDict.concatenate())

# if __name__ == '__main__':
#     main()

################################
# 4. Write a Python script to check whether a given key already exists in a dictionary
################################

# class Solution:
#     def __init__(self, dictionary:dict()) -> None:
#         self.dictionary = dictionary
    
#     def check_key(self, key:int) -> bool:
#         return key in self.dictionary

# def main():
#     givenDict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#     givenSolution = Solution(givenDict)
#     print(givenSolution.check_key(5))

# if __name__ == '__main__':
#     main()

################################
# 5. Write a Python program to iterate over dictionaries using for loops.
################################

# class Solution:
#     def __init__(self, dictionary:dict()) -> None:
#         self.dictionary = dictionary

#     def iterate_dictionary(self):
#         for key, value in self.dictionary.items():
#             print(f'{key} : {value}')

# import unittest
# class Test(unittest.TestCase):
#     def test_iterate_dictionary(self):
#         givenDict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#         givenSolution = Solution(givenDict)
#         givenSolution.iterate_dictionary()
# def main():
#     unittest.main()

# if __name__ == '__main__':
#     main()

################################
# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
################################

# class Solution:
#     def __init__(self, n:int) -> None:
#         self.n = n

#     # method 1
#     # def generate_dictionary(self):
#     #     for key, value in self.dictionary.items():
#     #         finalValue = key * key
#     #         print(f'{key} : {finalValue}')

#     def generate_dictionary(self):
#         return {x: x*x for x in range(1, self.n+1)}
    
#     def print_dictionary(self):
#         print(self.generate_dictionary())
    
# import unittest
# class Test(unittest.TestCase):
#     def test_generate_dictionary(self):
#         givenN = 5
#         givenSolution = Solution(givenN)
#         givenSolution.print_dictionary()

# def main():
#     unittest.main()

# if __name__ == '__main__':
#     main()

#################################
# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
#################################

# class Solution:
#     def __init__(self, dictionary:dict()) -> None:
#         self.dictionary = dictionary
    
#     def print_dictionary(self):
#         # method 1
#         # for i in range(1, 16):
#         #     print(f'{i}' ':' f'{i*i}')
#         # method 2
#         # print({x: x*x for x in range(1, 16)})
#         # method 3
#         # print(f'{dict(zip(range(1, 16), [x*x for x in range(1, 16)]))}')
#         # method 4
#         # dictionary = {x: x*x for x in range(1, 16)}
#         # print(dictionary)
#         # method 5
#         # d = dict()
#         # for i in range(1, 16):
#         #     d[i] = i*i
#         # print(d)
# def main():
#     Solution({}).print_dictionary()

# if __name__ == '__main__':
#     main()

#################################
# 8. Write a Python script to merge two Python dictionaries.
#################################

# class Solution:
#     def __init__(self, dictionary1:dict(), dictionary2:dict()) -> None:
#         self.dictionary1 = dictionary1
#         self.dictionary2 = dictionary2

#     def merge_dictionary(self):
#         return {**self.dictionary1, **self.dictionary2}
    
#     def print_dictionary(self):
#         print(self.merge_dictionary())

# def main():
#     givenDict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#     givenDict2 = {7: 70, 8: 80, 9: 90, 10: 100}
#     givenSolution = Solution(givenDict1, givenDict2)
#     givenSolution.print_dictionary()
    
# if __name__ == '__main__':
#     main()

#################################
# 9. Write a Python program to iterate over dictionaries using for loops.
#################################

# class Solution:
#     def __init__(self):
#         self.dict = {'a': 1, 'b': 2, 'c': 3}

#     def print_dictionary(self):
#         for key, value in self.dict.items():
#             print(key, value)

# def main():
#     s = Solution()
#     s.print_dictionary()

# if __name__ == '__main__':
#     main()

#################################
# 10. Write a Python program to sum all the items in a dictionary.
#################################

# class Solution:
#     def __init__(self, dictionary:dict()) -> None:
#         self.dictionary = dictionary

#     def sum_items(self):
#         return sum(self.dictionary.values())

#     def print_sum(self):
#         print(self.sum_items())

# def main():
#     givenDict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#     givenSolution = Solution(givenDict)
#     givenSolution.print_sum()

# if __name__ == '__main__':
#     main()

#################################
# 11. 11. Write a Python program to multiply all the items in a dictionary. 
#################################
# from functools import reduce

# class Solution:
#     def __init__(self, dictionary:dict()) -> None:
#         self.dictionary = dictionary
    
#     def multiply_items(self):
#         return reduce(lambda x, y: x*y, self.dictionary.values())

#     def print_multiply(self):
#         print(self.multiply_items())

# def main():
#     givenDict = {1: 1, 2: 2, 3: 3}
#     givenSolution = Solution(givenDict)
#     givenSolution.print_multiply()

# if __name__ == '__main__':
#     main()