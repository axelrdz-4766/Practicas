import sys

# ---------------------------- Variables Generales --------------------
help = '''Para usar encryptor se usan las siguientes flags:
--encrypt [numero]: Esto dara como output los numeros primos del numero dado.
Ejemplo -> encryptor.py --encrypt 120
--decrypt ["Numeros primos"]: Da como output el numero de los numeros primos. Debe de ir dentro de las comillas o comillas simples
Ejemplo -> encryptor.py --decrypt "2^3 * 3^1 * 5^1" '''

header = """
███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██████╔╝
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██╔══██╗
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝██║  ██║
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝
"""
flags = [
    "--help",
    "--encrypt",
    "--decrypt"
]

# -------------------------- Bloque de funciones ------------------------

def test(x):
    if x == 2:
        print("Perfecto, lo tienes!!")

# -------------------------- Bloque de Codigo ---------------------------

try:
    if len(sys.argv) < 2:
        sys.exit("Para mas informacion de los comandos usa la flag --help")
    
    if sys.argv[1] in flags:
        if sys.argv[1] == "--help":
            print(header)
            sys.exit(help)
        elif sys.argv[1] == "--encrypt": print("funciona!!")
        elif sys.argv[1] == "--decrypt":
            if sys.argv[2]:
                test_str = sys.argv[2]
                test_int = int(test_str)
                test(test_int)

    else: sys.exit("Para mas informacion de los comandos usa la flag --help")

except ValueError:
    sys.exit()