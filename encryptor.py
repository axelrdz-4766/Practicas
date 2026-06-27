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

def encrypt(x):
    print

def decrypt(x):
    dicc_par = {}
    x_first = x.split("*")
    c = 0

    for i in x_first:
        partes = i.split("^")
        c += 1
        
        base = int(partes[0])
        exponente = int(partes[1])
        ter = f'termino_{c}'

        dicc_par[ter] = {"base": base, "exponente": exponente}
#----------------------- Bloque de Codigo ---------------------------

try:
    if len(sys.argv) < 2:
        sys.exit("Para mas informacion de los comandos usa la flag --help")
    
    if sys.argv[1] in flags:
        if sys.argv[1] == "--help":
            print(header)
            sys.exit(help)
        elif sys.argv[1] == "--encrypt": 
            num = int(sys.argv[2])
            if isinstance(num, int):
                encrypt(num)
            else: raise IndexError;
        elif sys.argv[1] == "--decrypt":
            if sys.argv[2]:
                num_prim = sys.argv[2]
                decrypt(num_prim)

    else: sys.exit("Para mas informacion de los comandos usa la flag --help")

except (ValueError, IndexError):
    sys.exit("Para mas informacion de los comandos usa la flag --help")