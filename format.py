a = 'A'
b = 'B'
c = 1.1

string = 'a={} b={} c{}'

formato = 'a={} b={} c={:.0f}'.format(a, b, c )
type_format = type(formato)
print(type_format)

print(formato)

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)