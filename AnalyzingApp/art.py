def colors(color, bold):
    effect = ""
    if color != 0:
        effect += "\u001b[38;5;" + str(color) + "m"
    else:
        effect += ""

    if bold == 1:
        effect += "\u001b[1m"
    else:
        effect += ""
    return effect


def FontEffect(string, color, bold):
    return colors(color, bold) + string + colors("\u001b[0", 0)


def FormalFiller(string, col):
    return string + " " * (int(120 / col) - len(string))

class Print:
    def ln(content):
        print(content, "\n")

    def tabln(content):
        print("     ", content + "\n")


def LoadBar(ratio, range, height):
    filler = ""
    if height == 1:
        filler = "█"
    if height == 0:
        filler = "▄"
    if ratio <= 1:
        return filler * int(range * ratio) + "_" * int(range - range * ratio)
    else:
        return filler * range