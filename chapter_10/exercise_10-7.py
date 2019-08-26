"""
Write a function called has_duplicates that takes a list and
returns True if there is any element that appears more than once.
It should not modify the original list
"""

def has_duplicates(t):
    ts = sorted(t)
    for i in range(len(ts)-1):
        if ts[i] == ts[i+1]:
            return True
    return False
