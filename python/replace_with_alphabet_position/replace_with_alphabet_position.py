alphabet = {
"a":1,
"b":2,
"c":3,
"d":4,
"e":5,
"f":6,
"g":7,
"h":8,
"i":9,
"j":10,
"k":11,
"l":12,
"m":13,
"n":14,
"o":15,
"p":16,
"q":17,
"r":18,
"s":19,
"t":20,
"u":21,
"v":22,
"w":23,
"x":24,
"y":25,
"z":26,

}

def alphabet_position(text):
    number = []
    for letter in text.lower():
        x = alphabet.get(letter,"")
        if x != "":
            number.append(x)

    return ' '.join(str(x) for x in number)

print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))