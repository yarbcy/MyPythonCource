import contextlib, io
zen = io.StringIO()
with contextlib.redirect_stdout(zen):
    import this

def countWord(word):
    count=0
    for item in zen.getvalue().split():
        if item == word:
            count+=True
    return count

print(countWord('is'))
print(countWord('better'))
print(countWord('never'))

