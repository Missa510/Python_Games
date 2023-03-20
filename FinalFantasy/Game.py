import pygame
import os

class Jugador:
    def Estadisticas(nombre, nivel, items, bonus):
        # Nombre = "Altair Ibn-La'Ahad"
        Salud = 130
        Ataque = [30, 31, 32, 33, 34, 35]
        Defenza = [0.15, 0.16, 0.17, 0.18, 0.19, 0.20]
        # Items = "Espada"
        # Bonus = "Ataque +4"
        return nombre, Salud, Ataque, Defenza, nivel, items, bonus

print("Final Fantasy: Inicial Fantasy\nEstadisticas del jugador")
name = input("Nombre ->")
level = int(input("Nivel inicial ->"))
items = input("Items (Armas, posiones, etc...) ->")
bonusplus = input("Bonus (Ataque, defenza, salud) ->")
print(Jugador.Estadisticas(name, level, items, bonusplus))
