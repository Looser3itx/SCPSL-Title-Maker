def generate_gradient_word(word, start_color, end_color):
    def interpolate_color(color1, color2, t):
        r = int((1 - t) * color1[0] + t * color2[0])
        g = int((1 - t) * color1[1] + t * color2[1])
        b = int((1 - t) * color1[2] + t * color2[2])
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    # Validate input colors and word
    if not (start_color and end_color and word):
        return "Error"

    if len(start_color) != 6 or len(end_color) != 6:
        return "Error"

    try:
        start_color = tuple(int(start_color[i:i+2], 16) for i in (0, 2, 4))
        end_color = tuple(int(end_color[i:i+2], 16) for i in (0, 2, 4))
    except ValueError:
        return "Error"

    gradient_word = ""

    word_len = len(word)
    if word_len > 0:
        step = 1.0 / max(word_len - 1, 1)  # Avoid division by zero
        for i in range(word_len):
            t = step * i
            color = interpolate_color(start_color, end_color, t)
            gradient_word += f"<color={color}>{word[i]}</color>"

    return gradient_word

if __name__ == "__main__":
    input_word = input("Enter a word: ")
    start_color = input("Enter the starting color (in hexadecimal format, e.g., fbd308): ")
    end_color = input("Enter the ending color (in hexadecimal format, e.g., 8b00ff): ")

    gradient_html = generate_gradient_word(input_word, start_color, end_color)
    print("3itx SCPSL Title =>:", gradient_html)
