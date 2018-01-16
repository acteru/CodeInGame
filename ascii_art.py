l = int(input()) # width
h = int(input()) # hight
t = input()      # letter
s = 0            # start block
e = l            # end block

# 5 rows with every character
alpha_input = [str(input()) for i in range(h)]
# erstelle die matrix für das alphabet
# alpha_input = [0][' #  ']
# alpha_input = [1]['# # ']
# alpha_input = [2]['### ']
# alpha_input = [3]['# # ']
# alpah_input = [4]['# # ']


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
chars = {}
for x in alpha:
    chars[x] = (s, e)
    s += l
    e += l
# Kordinaten für die Buchstaben innerhalbe des alpha_inputs
#{'A': (0, 4), 'B': (4, 8), 'C': (8, 12), 'D': (12, 16), 'E': (16, 20),
#'F': (20, 24), 'G': (24, 28), 'H': (28, 32), 'I': (32, 36), 'J': (36, 40),
#'K': (40, 44), 'L': (44, 48), 'M': (48, 52), 'N': (52, 56), 'O': (56, 60),
#'P': (60, 64), 'Q': (64, 68), 'R': (68, 72), 'S': (72, 76), 'T': (76, 80),
#'U': (80, 84), 'V': (84, 88), 'W': (88, 92), 'X': (92, 96), 'Y': (96, 100),
#'Z': (100, 104), '?': (104, 108)}


# char und strings werden übergeben und müssen iteriert werden
buchstabe = []
for x in t:
    letter = []
    # check if all chars ar upper and replace @ with ?
    if x.islower():
        x = x.upper()
    if x not in alpha:
        x = '?'
    for i in range(h):
        letter.append(alpha_input[i][chars[x][0]:chars[x][1]])
    buchstabe.append(letter)
# E = [['### ', '#   ', '##  ', '#   ', '### ']]


# append zu output_rows[0] buchstabe[0][0]
                          #buchstabe[1][0]
                          #buchstabe[2][0]
                          #buchstabe[3][0]
                          #buchstabe[4][0]
output_rows = []
for y in range(h):
    output_letter = []
    for x in range(len(t)):
        output_letter.append(buchstabe[x][y])
    output_rows.append(output_letter)


for i in output_rows:
    print(''.join(i))
