def get_formatted_name(first, last, midle=''):
    """Строит отформатированное полное имя."""
    if midle:
        full_name = f"{first} {midle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
