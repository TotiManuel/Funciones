import zipfile
from zipfile import ZipFile
with zipfile.ZipFile("ComprimirArchivos/Comprimido.zip", "w") as fzip:
    fzip.write("ComprimirArchivos/Documentacion.txt")
    fzip.write("ComprimirArchivos/Python.py")
    fzip.write("ComprimirArchivos/C.c")
    fzip.printdir()
    fzip.extractall()
print("Archivos Comprimidos")
