import gzip
with open("ComprimirArchivos/Documentacion.txt","rb") as original:
    with gzip.open("ComprimirArchivos/ComprimidoG.txt.gz", "wb") as archivo1:
        archivo1.writelines(original)