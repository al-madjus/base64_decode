# Decodes base64 string
import argparse

index = {   'A' : 0,
            'B' : 1,
            'C' : 2,
            'D' : 3,
            'E' : 4,
            'F' : 5,
            'G' : 6,
            'H' : 7,
            'I' : 8,
            'J' : 9,
            'K' : 10,
            'L' : 11,
            'M' : 12,
            'N' : 13,
            'O' : 14,
            'P' : 15,
            'Q' : 16,
            'R' : 17,
            'S' : 18,
            'T' : 19,
            'U' : 20,
            'V' : 21,
            'W' : 22,
            'X' : 23,
            'Y' : 24,
            'Z' : 25,
            'a' : 26,
            'b' : 27,
            'c' : 28,
            'd' : 29,
            'e' : 30,
            'f' : 31,
            'g' : 32,
            'h' : 33,
            'i' : 34,
            'j' : 35,
            'k' : 36,
            'l' : 37,
            'm' : 38,
            'n' : 39,
            'o' : 40,
            'p' : 41,
            'q' : 42,
            'r' : 43,
            's' : 44,
            't' : 45,
            'u' : 46,
            'v' : 47,
            'w' : 48,
            'x' : 49,
            'y' : 50,
            'z' : 51,
            '0' : 52,
            '1' : 53,
            '2' : 54,
            '3' : 55,
            '4' : 56,
            '5' : 57,
            '6' : 58,
            '7' : 59,
            '8' : 60,
            '9' : 61,
            '+' : 62,
            '/' : 63,
            '=' : 0
        }

parser = argparse.ArgumentParser(description='Decode base64 strings')
parser.add_argument('--string', dest='string', required=True)
args = parser.parse_args()

bin_string = ''
output = ''

# Reiterate through all characters and get their value, convert 
# to 6bit binary, then combine
for char in args.string:
    if char in index.keys():
        bin_string += "{0:06b}".format((index.get(char)))
print("\nBinary string: \n" + bin_string)

# Partition the string in bytes, then find their ASCII values
while len(bin_string) >= 8:
    byte = bin_string[1:8]
    char = chr(int(byte, 2))
    output += char
    bin_string = bin_string[8:]

# Print the result
print("\nDecoded text: \n" + output)
