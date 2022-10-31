"""
# Function to get values list in reverse sorted order
(Note: Feel free to use python builtin functions)
"""

def get_values(data):
    return list(reversed(sorted(data.values())))

if __name__ == '__main__':
    case1 = get_values({'a':1234, 'b':2633, 'c':111})
    print(case1)
    assert case1 == [2633, 1234, 111]
    case2 = get_values({'a':-12, 'b':0, 'c':-10, 'd': 3, 'e': 0 })
    print(case2)
    assert case2 == [3,  0,  0, -10, -12]
    print('Success')