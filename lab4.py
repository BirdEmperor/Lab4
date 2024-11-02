import pyfiglet
from colorama import Fore, Style, init
import os

# Initialize colorama for colored output
init()

def preview_ascii_art(ascii_art, alignment):
    """Displays ASCII art preview with chosen alignment."""
    terminal_width = os.get_terminal_size().columns
    print("\nPreview of your ASCII art:\n")
    
    # Align preview text based on user choice
    if alignment == "left":
        formatted_preview = "\n".join(line.ljust(terminal_width) for line in ascii_art.splitlines())
    elif alignment == "right":
        formatted_preview = "\n".join(line.rjust(terminal_width) for line in ascii_art.splitlines())
    else:
        formatted_preview = "\n".join(line.center(terminal_width) for line in ascii_art.splitlines())
    
    print(formatted_preview)
    print("\n--- End of preview ---\n")

def generate_ascii_art():
    # Step 1: Get user input
    text = input("Enter a word or phrase for the ASCII art: ")
    
    # Step 2: Get the symbol set for the ASCII art (default to "*")
    symbol_set = input("Enter symbols for the ASCII art (e.g., '@#*'): ") or "*"

    # Step 3: Art size (width and height)
    while True:
        try:
            width = int(input("Enter ASCII art width (over 10): "))
            height = int(input("Enter ASCII art height (over 1): "))
            if width > 10 and height > 1:
                break
            else:
                print("Width must be greater than 10 and height greater than 1.")
        except ValueError:
            print("Please enter a numeric value.")

    # Step 4: Generate ASCII art
    font = "standard"  # Default font
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font, width=width)
    except pyfiglet.FontNotFound:
        ascii_art = pyfiglet.figlet_format(text, font="standard", width=width)

    # Scale the ASCII art by repeating lines to reach desired height
    art_lines = ascii_art.splitlines()
    scaled_art = "\n".join(line for line in art_lines for _ in range(height))

    # Step 5: Choose alignment for text
    alignment = input("Choose alignment (left, center, right): ").lower()
    alignment = alignment if alignment in ["left", "center", "right"] else "center"

    # Step 6: Choose color options
    print("Available colors:")
    print("1. Red")
    print("2. Green")
    print("3. Blue")
    print("4. Default (no color)")

    color_index = input("Enter color number for the text: ")
    color = {
        '1': Fore.RED,
        '2': Fore.GREEN,
        '3': Fore.BLUE,
    }.get(color_index, Style.RESET_ALL)

    # Step 7: Display the art with chosen settings
    print("\nDisplaying ASCII art with selected options:\n")
    print(color + scaled_art + Style.RESET_ALL)  # Apply color to art display
    preview_ascii_art(scaled_art, alignment)

    # Step 8: Optionally save ASCII art to file
    save_option = input("Would you like to save ASCII art to a file? (yes/no): ").strip().lower()
    if save_option in ['yes', 'y']:
        filename = input("Enter filename (without extension, e.g., 'ascii_art'): ") + '.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(scaled_art)
        print(f"ASCII art saved to file: {filename}")

# Run the function
generate_ascii_art()
