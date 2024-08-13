e = 'out_test.txt'
a = 'Hello out_test.txt'
with open(e, 'w') as f:
    f.write(a)

with open(e, 'r') as f:
    for line in f:
        print(line, end=" ")

