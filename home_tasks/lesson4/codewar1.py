def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    fuelNeeded = distance_to_pump / mpg
    if fuelNeeded <= fuel_left:
        return True
    else:
        return False