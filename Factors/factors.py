from primePy import primes as p

out = open('output.txt','wt')

with open('input.txt','r') as txt:
    for num in txt.read().split('\n'):
        list = p.factors(int(num))
        out.write(str(p.factors(int(num))) + '\n')