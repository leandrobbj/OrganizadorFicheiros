from pathlib import Path

pasta = Path.cwd()
count = 0

print("ORGANIZADOR DE FICHEIROS")
print("-----------------------")

for ficheiro in pasta.iterdir():
    if ficheiro.is_file():
        count += 1
        print("Nome:", ficheiro.name)
        print("Extensão:", ficheiro.suffix)
        print("Tamanho:", ficheiro.stat().st_size, "bytes")
        print("-----------------------")

if count == 0:
    print("A pasta não contém ficheiros")
else:
    print("Ficheiros Encontrados: ", count)


