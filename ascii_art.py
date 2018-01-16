l = int(input()) # width
h = int(input()) # hight
t = input()      # letter
s = 0            # start block
e = l            # end block

alpha_input = [str(input()) for i in range(h)]
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
chars = {}
for x in alpha:
    chars[x] = (s, e)
    s += l
    e += l

buchstabe = []
for x in t:
    letter = []
    if x.islower():
        x = x.upper()
    if x not in alpha:
        x = '?'
    for i in range(h):
        letter.append(alpha_input[i][chars[x][0]:chars[x][1]])
    buchstabe.append(letter)

output_rows = []
for y in range(h):
    output_letter = []
    for x in range(len(t)):
        output_letter.append(buchstabe[x][y])
    output_rows.append(output_letter)

for i in output_rows:
    print(''.join(i))
