import os

def preview_ascii_art(ascii_art, color_code):
    """Displays a preview of ASCII art with color."""
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80  # Стандартная ширина, если ошибка

    print("\nPreview of your ASCII Art:\n")
    # Center the preview and apply color
    formatted_preview = "\n".join(line.center(terminal_width) for line in ascii_art.splitlines())
    print(color_code + formatted_preview + "\033[0m")  # Reset color at the end
    print("\n--- End of Preview ---\n")

def get_numeric_input(prompt, min_value=None):
    """Helper function to get a numeric input with error handling."""
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Please enter a value greater than {min_value}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

# Full alphabet for ASCII art
basic_font = {
    'A': ["  *  ", " * * ", "*****", "*   *", "*   *"],
    'B': ["**** ", "*   *", "**** ", "*   *", "**** "],
    'C': [" ****", "*    ", "*    ", "*    ", " ****"],
    'D': ["**** ", "*   *", "*   *", "*   *", "**** "],
    'E': ["*****", "*    ", "**** ", "*    ", "*****"],
    'F': ["*****", "*    ", "**** ", "*    ", "*    "],
    'G': [" ****", "*    ", "* ***", "*   *", " ****"],
    'H': ["*   *", "*   *", "*****", "*   *", "*   *"],
    'I': [" *** ", "  *  ", "  *  ", "  *  ", " *** "],
    'J': ["  ***", "   * ", "   * ", "*  * ", " **  "],
    'K': ["*   *", "*  * ", "***  ", "*  * ", "*   *"],
    'L': ["*    ", "*    ", "*    ", "*    ", "*****"],
    'M': ["*   *", "** **", "* * *", "*   *", "*   *"],
    'N': ["*   *", "**  *", "* * *", "*  **", "*   *"],
    'O': [" *** ", "*   *", "*   *", "*   *", " *** "],
    'P': ["**** ", "*   *", "**** ", "*    ", "*    "],
    'Q': [" *** ", "*   *", "* * *", "*  **", " *** "],
    'R': ["**** ", "*   *", "**** ", "*  * ", "*   *"],
    'S': [" ****", "*    ", " *** ", "    *", "**** "],
    'T': ["*****", "  *  ", "  *  ", "  *  ", "  *  "],
    'U': ["*   *", "*   *", "*   *", "*   *", " *** "],
    'V': ["*   *", "*   *", "*   *", " * * ", "  *  "],
    'W': ["*   *", "*   *", "* * *", "** **", "*   *"],
    'X': ["*   *", " * * ", "  *  ", " * * ", "*   *"],
    'Y': ["*   *", " * * ", "  *  ", "  *  ", "  *  "],
    'Z': ["*****", "   * ", "  *  ", " *   ", "*****"],
    ' ': ["     ", "     ", "     ", "     ", "     "],  # Space for separation
}

def generate_ascii_art():
    print("Welcome to the ASCII Art Generator!")
    print("This tool lets you create ASCII art from text.")
    print("Follow the on-screen instructions to create ASCII art.\n")

    # Get user input
    text = input("Enter a word or phrase for ASCII art: ")

    # Construct ASCII art based on user input
    ascii_art_lines = [""] * 5  # Each letter is 5 lines high
    for char in text.upper():
        char_art = basic_font.get(char, [" " * 5] * 5)  # Replace unsupported chars with spaces
        for i, line in enumerate(char_art):
            ascii_art_lines[i] += line + "  "  # Add space between letters

    ascii_art = "\n".join(ascii_art_lines)

    # Get desired width and height for ASCII art
    width = get_numeric_input("Enter the desired width of ASCII art (recommended above 10): ", min_value=10)
    height = get_numeric_input("Enter the desired height of ASCII art (recommended above 1): ", min_value=1)

    # Scale ASCII art to the desired height (vertical scaling)
    scaled_art = "\n".join(line for line in ascii_art.splitlines() for _ in range(height))

    # Define colors using ANSI escape codes
    colors = {
        '1': "\033[31m",  # Red
        '2': "\033[32m",  # Green
        '3': "\033[34m",  # Blue
        '4': "\033[0m"    # Default (no color)
    }
    print("\nAvailable colors:\n1. Red\n2. Green\n3. Blue\n4. Default (no color)")

    # Get color choice
    color_code = colors.get(input("Enter the color number for the text: "), "\033[0m")

    # Get character for ASCII art
    symbol = input("Enter a symbol for creating ASCII art (default '*'): ") or '*'

    # Display preview
    preview_ascii_art(ascii_art, color_code)

    # Rebuild ASCII art with the new symbol
    final_ascii_art = '\n'.join(
        ''.join(symbol if c != ' ' else ' ' for c in line)
        for line in scaled_art.splitlines()
    )

    # Center the final ASCII art
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80  # Default width

    centered_final_art = "\n".join(line.center(terminal_width) for line in final_ascii_art.splitlines())

    print(f"\nYour ASCII art with the symbol '{symbol}':\n")
    print(color_code + centered_final_art + "\033[0m")  # Reset color

    # Save to file option
    if input("Would you like to save the ASCII art to a file? (yes/no): ").strip().lower() in ['yes', 'y']:
        filename = input("Enter file name (without extension, e.g., 'ascii_art'): ") + '.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(final_ascii_art)
        print(f"ASCII art saved to file: {filename}")

    print("\nThank you for using the ASCII Art Generator! Goodbye!")

# Run the function
generate_ascii_art()
