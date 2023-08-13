"""
CP1404 Practical
hex_colours
Code that enter colour name to get the hexadecimal colour codes
"""

COLOUR_CODES = {"Absolute Zero": "#0048ba", "Amber": "#ffbf00", "Aqua": "#00ffff", "Aureolin": "#fdee00",
                "Cadmium Red": "#e30022",
                "Gray": "#bebebe", "Medium": "#66cdaa", "Purple": "#a020f0", "Wild Strawberry": "#ff43a4",
                "Yellow Orange": "#ffae42"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print(f"The hexadecimal code of \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ")
