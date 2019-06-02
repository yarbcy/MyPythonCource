# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
def double_char(s):
    new_s = []
    for char in s:
        new_s.append(char)
        new_s.append(char)
    seperator = ''
    return(seperator.join(new_s))