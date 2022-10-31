class Solution(object):
    def parenthese_Validation(self, s:str):
        '''a method that takes a string of parentheses and checks different cases of entries
        before pushing to the stack, so it checks if it is an opening parentheses at first
        if so it pushes it if not it returns false, if it is an opening it pushes it and 
        look at the next one if it is an opening it pushes it again and if it is closing the method 
        pops it and continues to check other entries until it ends and then returns a boolean depending 
        on the case'''
        stack = []
        for c in s:
            if (c == '(') | (c == '{') | (c == '['):
                stack.append(c)
            elif (c == ')') | (c == '}') | (c == ']'):
                if len(stack) != 0:
                    top = stack.pop()
                    if top == '(' and c == ')':
                        continue
                    elif top == '{' and c == '}':
                        continue
                    elif top == '[' and c == ']':
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False



s = Solution()
print(s.parenthese_Validation("[]"))