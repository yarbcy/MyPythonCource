def enough(cap, on, wait):
    fit = (on + wait) - cap
    if fit >= True:
        return fit
    else:
        return False