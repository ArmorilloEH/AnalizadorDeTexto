texto=input("Ingrese el texto que desees analizar:").lower()
print("Ingrese 3 letras:")
a=input().lower()
b=input().lower()
c=input().lower()
txt1=texto.count(a)
print("------------------------------------------------------")
print("La letra "+str(a)+" se muestra "+str(txt1)+" veces.")
txt2=texto.count(b)
print("La letra "+str(b)+" se muestra "+str(txt2)+" veces.")
txt3=texto.count(c)
print("La letra "+str(c)+" se muestra "+str(txt3)+" veces.")
lista_texto=list(texto)
print("------------------------------------------------------")
print("Hay "+str(len(lista_texto))+" caracteres en su texto.")
palabras_texto=texto.split()
print("Hay "+str(len(palabras_texto))+" palabras en su texto.")

print("------------------------------------------------------")
print("La primera letra de su texto es la "+str(texto[0])+".")
ultima_letra=len(texto)-1
print("La ultima letra de su texto es la "+str(texto[ultima_letra])+".")
print("------------------------------------------------------")
print("Texto invertido:")
texto_invertido=texto[::-1]
print(texto_invertido)
print("------------------------------------------------------")
print(("¿Desea comprobar si existe una palabra en concreto?"))
char=input("s/n\n").lower()
def buscar():
    print("¿Que palabra desea comprobar que aparezca en el texto?")
    texto_buscar = input().lower()
    bandera=bool(str(texto_buscar) in texto)
    if bandera:
        print(str(texto_buscar)+" aparece en el texto.")
        print("Gracias por usar el analizador de texto de Agustín.")
    else:
        print(str(texto_buscar)+" no aparece en el texto.")

if char=="s":

  buscar()
else:
    print("Gracias por usar el analizador de texto de Agustín.")




