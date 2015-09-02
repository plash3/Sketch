# The pattern is what to look for
pattern     = ['[', '(', '{']
counterpart = [']', ')', '}']

def check_parity(l, r):
    result = True
    for i in xrange(len(pattern)):
        if l == pattern[i]:
            if r != counterpart[i]:
                result = False
            break

    return result

def is_balanced(s):
    stack = []
    balanced = True
    for i in xrange(len(s)):
        if s[i] in pattern:
            stack.append(s[i])
        elif s[i] in counterpart:
            if not stack or not check_parity( stack.pop(), s[i] ):
                balanced = False
                break

    # if stack is not empty then the string is not balanced
    if stack:
        balanced = False
    return balanced
