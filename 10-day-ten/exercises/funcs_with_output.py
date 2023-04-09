def format_name(first_name, last_name):
    """Take a first and last name and format it to 
    return thr title case version of the name"""
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs"
    formatted_name = f"{first_name.title()} {last_name.title()}"
    return formatted_name


print(format_name("johnson", "ojo"))
print(format_name("", ""))
