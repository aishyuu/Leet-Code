#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

arr = [1,2,3,1]
arr_false = [1,2,3,4]

'''
Brute Force Method
Time: O(n^2)
Space: O(1)
'''

def brute_force(test):
    for i in range(len(test)):
        for j in range(i+1, len(test)):
            if test[i] == test[j]:
                return True
    
    return False

'''
Sorting Method
Time: O(nlogn)
Space: O(1)
'''

def sorting_method(test):
    test.sort()
    for i in range(len(test)-1):
        if test[i] == test[i+1]:
            return True
    
    return False


'''
Sets Method
Time: O(n)
Space: O(n)
'''

def sets_method(test):
    sets = set()
    for i in range(len(test)):
        if test[i] in sets:
            return True
        else:
            sets.add(test[i])
    
    return False