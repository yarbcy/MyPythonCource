import contextlib, io
zen = io.StringIO()
with contextlib.redirect_stdout(zen):
    import this

zen_str = str(zen.getvalue())

def countWord(word):
    count=0
    for item in zen_str.split():
        if item == word:
            count+=True
    return count

print(countWord('is'))
print(countWord('better'))
print(countWord('never'))

print(zen_str.upper())

while (zen_str.find('I')>=0) or (zen_str.find('i')>=0):
    zen_str = zen_str.replace('I','&')
    zen_str = zen_str.replace('i','&')

print(zen_str)
    
    
