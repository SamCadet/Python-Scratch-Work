
def cityCountry(city, country, population=''):
    if population:
        place = f'{city}, {country} - population {population}'
    else:
        place = f'{city}, {country}'
    return place
