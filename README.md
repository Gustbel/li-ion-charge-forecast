# li-ion-charge-forecast

Python Library that predicts the charging time in minutes of a Lithium/Ion battery with simple discrete parameters.
Librería de Python que predice los tiempos en minutos de la carga de un dispositivo con Batería de Litio/Ión con parámetros discretos simples. 

El repositorio incluye:

-  Función Principal del cálculo de tiempo que se aloja en el archivo librería ``lib/tiempos_de_carga.py``.
-  Scripts ``test1.py`` y ``test2.py`` que son dos scripts de ejemplo para debuguear la librería.

Library
------------

La función principal está alojada en la librería y se llama ``tiempos_de_carga``. Recibe 4 valores numéricos y devuelve 5 valores (un boleano de control y 4 valores numéricos)

.. code:: python

    isCorrect, t25, t50, t75, t100 = tiempo_carga (i_actual, bat_state, bat_capac, i_max):
    
Valores de Entrada:
	-  **i_actual** : De 0 a Infinito, en la práctica de 10 a 3000. Se mide en mA (miliAmperes). Representa la corriente actual con la que se está cargando la batería.
	-  **bat_state** : De 0 a 100. Es un valor de porcentaje (%). Representa el porcentaje de carga total que tiene la batería.
	-  **bat_capac** : De 100 a Infinito, en la práctica de 100 a 6000 (en el caso de dispositivos portátiles/pequeños). Se mide en mAh (miliAmpereHora). Representa la capacidad total de energía que almacena la batería, en un término mas simple es la capacidad de la batería.
	-  **i_max** : De 500 a Infinito, en la práctica de 1000 a 4000. Se mide en mA (miliAmperes). Representa la corriente máxima que puede recibir la batería/dispositivo que se esté cargando, este valor es intrínseco del dispositivo a cargar y lo suele dar el fabricante.
	
Valores de Salida:
	-  **isCorrect** : Booleano, indica si los valores se calcularon exitosamente. Si ingresamos algún valor no esperado por la función su valor será ``False``.
	-  **t25** : float. Este valor será el *tiempo en minutos* que tardará el proceso de carga en hacer que la batería llegue al 25%. En caso de que ``bat_state`` sea mayor o igual al 25% tomará un valor nulo ``None``
	-  **t50** : float. Este valor será el *tiempo en minutos* que tardará el proceso de carga en hacer que la batería llegue al 50%. En caso de que ``bat_state`` sea mayor o igual al 50% tomará un valor nulo ``None``
	-  **t75** : float. Este valor será el *tiempo en minutos* que tardará el proceso de carga en hacer que la batería llegue al 75%. En caso de que ``bat_state`` sea mayor o igual al 75% tomará un valor nulo ``None``
	-  **t100** : float. Este valor será el *tiempo en minutos* que tardará el proceso de carga en hacer que la batería llegue al 100%. En caso de que ``bat_state`` sea mayor o igual al 100% tomará un valor nulo ``None``.
	
	
If you have any question about this repository, do not hesitate to contact me: gustavobelbruno@gmail.com or open an issue on GitHub.
Gustavo Belbruno
