# converts decimal to binary and counts the quantity of 1

def count_bits(n,bin):
    bits = n % 2
    bin += [bits]
    n = n // 2
    print(n)
    if n > 0:
        return count_bits(n,bin)

    return bin

count = 0
bin = []
inv_bin = []
f = count_bits(76854,bin)

for i in range(len(bin), 0, -1):
    if bin[i-1] == 1:
      count += 1
    inv_bin.append(bin[i-1])

for b in inv_bin:
    print(b, end='')

print(f'\n{count}')
