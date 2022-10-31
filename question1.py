
"""
# Function to remove duplicates from a string
(Note: Feel free to use python builtin functions)
"""

def remove_duplicates(s):
    ot = ''
    for i in s:
        if i not in ot:
            ot = ot + i
    return ot



if __name__ == '__main__':
    case1 = remove_duplicates('hello')
    print(case1)
    assert case1 == 'helo'
    case2 = remove_duplicates('icecream sandwitch is good good')
    print(case2)
    assert case2 == 'iceram sndwthgod'
    print('Success')