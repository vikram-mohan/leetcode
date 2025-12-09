def validParenthesis(st):

    left = []
    star = []

    for i in range(len(st)):
        if st[i] == "(":
            left.append(i)

        if st[i] == "*":
            star.append(i)

        if st[i] == ")":
            if not left and not star:
                return False
            
            if left:
                left.pop()
            else:
                star.pop()

        while left and star:
            if left.pop() > star.pop():
                return False
    
    return not left

s = "(((**)))"
print(s,  "->", validParenthesis(s))

s = "(())"
print(s,  "->", validParenthesis(s))

s = "(((*)))*"
print(s,  "->", validParenthesis(s))

s = "(((*)"
print(s,  "->", validParenthesis(s))

s = "(((*))"
print(s,  "->", validParenthesis(s))