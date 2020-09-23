#!/usr/bin/env python
# coding: utf-8

from lib import tiempos_de_carga as tc

print("---- Pronóstico de Tiempos de Carga Demostración ----   VERSION 1.0\n")
print("AHORA INGRESARÁ VALORES (Solo ingresar numeros no letras ni simbolos):\n")

act = float(input("Ingrese el porcentaje de Batería actual (Entre 0 y 100 %):\n"))
i_act = float(input("Ingrese la Corriente Actual en mA (Entre 10 mA y 2000 mA):\n"))
i_max = float(input("Ingrese la Corriente Maxima que soporta su dispositivo en mA (Sugerido 2200 mA - Debe ser MAYOR a la corriente Actual o dará error):\n"))
cap = float(input("Ingrese la Capacidad de su dispositivo en mAh (Por ej Iphone11 tiene 3110)):\n"))


a, b, c, d, e = tc.tiempo_carga (i_act, act/100, cap,  i_max)
if (a == False): 
    print("\nHa ingresado un valor no esperado, por favor compruebe los valores ingresados e intente nuevamente")
else:
  print("\nExito en carga de datos\nRESULTADOS: Dispositivo ahora -> Batería: %.0f %%" % act)
  if b == None: b = 0
  print("El dispositivo llegará al  25%% en:  %.0f minutos" % b)
  if c == None: c = 0
  print("El dispositivo llegará al  50%% en:  %.0f minutos" % c)
  if d == None: d = 0
  print("El dispositivo llegará al  75%% en:  %.0f minutos" % d)
  if e == None: e = 0
  print("El dispositivo llegará al 100%% en:  %.0f minutos" % e)