import contextlib, io
zen = io.StringIO()
with contextlib.redirect_stdout(zen):
    import this

print(zen.getvalue().upper())

