print("Determinar si un carácter es una letra o un dígito")
print("==================================================" )

caracter = input("Ingresa un caracter: ")

if 'A' <= caracter <= 'Z' or 'a' <= caracter <= 'z':
    print("Letra")
    
if '0' <= caracter <= '9': 
    print("Digito")