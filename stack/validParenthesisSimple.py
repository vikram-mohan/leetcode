def validParenthesis(st):
    stack = []
    d = { "}" : "{", 
          "]" : "[", 
          ")" : "(" }

    for ch in st:
        if ch in d:
            if stack and stack[-1] == d[ch]:
                stack.pop()
        else:
            stack.append(ch)
    return True if not stack else False

s = "[]"
print(s,  "->", validParenthesis(s))

s = "([{}])"
print(s,  "->", validParenthesis(s))

s = "[(])"
print(s,  "->", validParenthesis(s))

# 944921