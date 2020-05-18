def str_city(city, strana, population=''):
    if population:
        full = f"{city} {strana} {population}"
    else:
        full = f"{city} {strana}"

    return full.title()
