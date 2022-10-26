"""import emoji

# grinning face
print("\U0001f600")

# grinning squinting face
print("\U0001F606")

# rolling on the floor laughing
print("\U0001F923")

"""
import time

print("Bienvenido a la isla \U0001f600 \nTu misión será encontrar el tesoro")
time.sleep(1)
print("Encontrarás muchos retos y decisiones que tomar, ¡Mucha Suerte!")
time.sleep(1)
print("¡Oh oh! Te has encontrado con barba negra, pero aún no te ha visto.")
time.sleep(1)
decision = input("¿Decides esconderte? \n")
if decision=="Si":
    time.sleep(1)
    print("Te has encontrado con un mapa del tesoro.")
    time.sleep(1)
    decision = input("¿Leer el mapa? \n")
    if decision=="No":
        time.sleep(1)
        print("Escuchaste un grito de auxilio, parece que es una damisela en apuros.")
        time.sleep(1)
        decision = input("¿Buscar el origen del grito? \n")
        if decision=="Si":
            time.sleep(1)
            print("Es una princesa, te advierte que no sigas adelante porque había un hueco.")
            time.sleep(1)
            print(" La liberas*")
            time.sleep(2)
            print("Llegan a un lago")
            time.sleep(1)
            decision = input("¿Nadar o rodear el lago?\n")
            if decision=="Rodear":
                time.sleep(1)
                print("Se encuentran cansados")
                time.sleep(1)
                decision = input("¿Descansar o seguir?\n")
                if decision=="Descansar":
                    time.sleep(1)
                    print("Esperan un rato y mientras hablan con la damisela encuentran muchas cosas en común.")
                    time.sleep(2)
                    decision = input("¿Seguir descansando o continuar?\n")
                    if decision=="Continuar":
                        time.sleep(1)
                        print("Encuentras una choza")
                        time.sleep(1)
                        decision = input("¿Seguir descansando o continuar?\n")
                        if decision=="Entrar":
                            time.sleep(1)
                            print("Hay comida, un tesoro, cama, una televisión con Netflix. Tú y la damisela se quedan a vivir allí felizmente.")
                        elif decision=="Seguir":
                            time.sleep(1)
                            print("Te perdiste en la isla. \nGame Over ")
                        else:
                            print("Escogiste una opción no disponible")
                    elif decision=="Descansar":
                        time.sleep(1)
                        print("Un cazador furtivo los confunde con un leopardo y les dispara. Mueres* \nGame Over")
                    else:
                        print("Escogiste una opción no disponible")
                elif decision=="Seguir":
                    time.sleep(1)
                    print("Había un tigre depredando en los alrededores y les ataca. \nGame Over.")
                else:
                    print("Escogiste una opción no disponible")
            elif decision=="Nadar":
                print("Atacado por una tribú \nGame Over")
            else:
                print("Escogiste una opción no disponible")
        elif decision=="No":
            time.sleep(1)
            print("Caiste en el agujero \nGame Over")
        else:
            print("Escogiste una opción no disponible")
    elif decision=="Si":
        time.sleep(1)
        print("El mapa estaba envenenado. *Mueres lenta y dolorosamente* \nGame Over")
    else:
        print("Escogiste una opción no disponible")
elif decision == "No":
    time.sleep(1)
    print("\"Hey aventurero, creo que no entiendes quien manda acá\", Barba Negra te ha apuñalado con su sable. \nGame Over.")
else:
    print("Escogiste una opción no disponible")