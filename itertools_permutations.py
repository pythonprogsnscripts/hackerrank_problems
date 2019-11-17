from itertools import permutations
# This tool returns successive  length permutations of elements in an iterable.
'''
Task

You are given a string .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.
'''
string, number = input().split()
print(*[''.join(i) for i in list((permutations(sorted(string),int(number))))],sep='\n')
