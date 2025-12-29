class Solution:
    def firstUniqChar(self, s: str) -> int:
        # ToDo: Write Your Code Here.
        # create an empty hash table
        h = {}
        # loop through the argument string
        # if s value does not exist create the key with value of 1
        # else find the key and increment the value by 1
        for key in s:
            if key in h:
                h[key] += 1
            else: 
                h[key] = 1
        # index out the key that has a value of greater than 1
        key = [key for key, value in h.items() if value == 1]
        # loop through the string to return the index position of the string
        for index in range(len(s)):
            if s[index] == key:
                return index
        # else return -1
        return -1

