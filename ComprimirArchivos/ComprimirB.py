import bz2
cadena=b"Julian Manuel Mandaio"
cadena_c=bz2.compress(cadena)
print(cadena)
print(cadena_c)
print(bz2.decompress(cadena_c))