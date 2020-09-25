#!/usr/bin/env python
# coding: utf-8

from math import exp
from math import log

def tiempo_carga (i_actual, bat_state, bat_capac, i_max):

    tau_max_teoric = 5      # Este es el tau maximo teórico y solo lo usaremos en la función para calcular la intersección
    tau_max = 2.5           # Aunque la matemática dice que se llega aprox a 100% en 5tau, las baterías terminan de cargar en mucho menos tiempo (por ahora dejamos 2.5tau)
    base_exponencial = 2    # Por ahora según los comportamientos vistos, la base del exponencial que mejor se adapta a una carga de batería en fase CV es 2

    ####      Comprobaciones        ####
    if i_actual == 0:                   # Si la corriente actual es 0 el dispositivo nunca se cargará, 
        return False, None, None, None, None                                                                
    if i_actual > i_max:                # Si la corriente actual es mayor a la teórica máxima es porque 
        return False, None, None, None, None              # hemos ingresado mal el valor de corriente teorico máximo
    if bat_state == 1:
        return True, None, None, None, None     # Carga Completa
    if bat_state < 0 or bat_state > 0.99:
        return False, None, None, None, None     # Valor de Batería Ingresado Incorrecto
   
    ####      CC Charging Phase     ####       Cálculo de la primera parte de carga, corriente continua        ##

    if bat_state < 0.7:                # Esta fase se ejecuta siempre y cuando la batería tenga un estado menor al 70%
        
        t_cc =  calculo_cc(bat_state, 0.7, bat_capac, i_actual)        # Esta fase irá hasta el 70% que es cuando termina la fase CC de la  
                                                                        # carga de una batería de Litio por lo que sacamos cuantos mAh de
                                                                        # energía faltan para llegar al 70% y como tenemos el valor de corriente 
                                                                        # actual en mA sacamos el total de horas que tardará en llegar a este 70%
                                                                        # por último multiplicamos por 60 para pasarlo a minutos
    else:
        t_cc = 0

    if bat_state < 0.25:                # Calculo del tiempo que demora llegar al 25% de carga 
        t_25 =  calculo_cc(bat_state, 0.25, bat_capac, i_actual) 
    else:
        t_25 = None

    if bat_state < 0.5:                # Calculo del tiempo que demora llegar al 50% de carga 
        t_50 =  calculo_cc(bat_state, 0.5, bat_capac, i_actual) 
    else:
        t_50 = None


    ####      CC-CV Transición Charging Phase     ####    Cálculo de la Transición entre las fases CC y CA     

    intersect = - (0.3/tau_max_teoric) * log( i_actual / i_max, base_exponencial)    # Acá si tenemos que poner que el tau máximo teórico y no tau_max 
                                                                        # porque hay que respetar la función verdadera a la hora de calcular la intersección

    
    if bat_state < 0.7 + intersect:

        if bat_state > 0.7:            # Esto se hace por si el estado actual de batería está entre 70% y el punto de intersección
            inicial_trans = bat_state
        else:
            inicial_trans = 0.7

        t_trans =  calculo_cc( inicial_trans, 0.7 + intersect, bat_capac, i_actual)

        if 0.7 + intersect >= 0.75:       # Si se alcanza el 75% dentro de la fase transición podemos calcularlo acá, sino lo calcularemos en la última fase
            t_75 =  calculo_cc(bat_state, 0.75, bat_capac, i_actual)
    else:
        t_trans = 0


    if bat_state >= 0.75:                # Calculo del tiempo que demora llegar al 25% de carga 
            t_75 = None
        
   
    ####      CV Charging Phase     ####       Cálculo de la última parte de carga, que tiene una corriente con una función con exponente negativo        ##
    
    if bat_state < 0.7 + intersect:
        inicial_cv = intersect
    else:
        inicial_cv = bat_state - 0.7


    t_cv = calculo_cv( inicial_cv, 0.3, bat_capac, i_max, tau_max, base_exponencial)     # Se pone 0.3 porque es lo que falta para llegar al 100% de batería
                                                                                         # recordemos que la función inicia en 0.7 (70%)

    if 0.7 + intersect < 0.75 and bat_state < .75:
        t_cv_75 = calculo_cv(inicial_cv, 0.05, bat_capac, i_max, tau_max, base_exponencial)
        t_75 = t_cc + t_trans + t_cv_75

    t_100 = t_cc + t_trans + t_cv


    return True, t_25, t_50, t_75, t_100


def calculo_cc (inicial, final, capacidad, corriente):
    return ( ( capacidad * (final - inicial) ) / corriente ) * 60 

def calculo_cv (inicial, final, capacidad, corriente_max, tau_m, base):
    return ( ((capacidad * 0.3) /corriente_max) * ( pow( base,  final/(0.3/tau_m) )  - pow ( base, inicial/(0.3/tau_m) ) ) ) * 60