# Nociones básicas de Python

## Variables
Las variables son como cajas, con ellas podemos transportar los valores que deseamos. Las variables se utilizan para realizar operaciones de un modo flexible.

Imaginemos que estamos escribiendo un programa que suma dos numeros. El modo más difícil y menos útil es calcular el resultado de cada una de todas las operaciones aritméticas posibles y ofrecerlo según sea la operación que lo requiere. EL modo más fácil y más útil es introducirlos en un medio flexible que pueda soportar todo el rango de números necesarios y transportarlos desde que el usuario los ingresa hasta donde la operación se produce, recoger el resultado y dárselo de nuevo al usuario.

~~~
# paso 1 : la suma
2 + 2, 2 + 3, 2 + 4...

# paso 2 : la variable, simplemente cambiamos su valor
var_a = 1
var_b = 2
result = var_a + var_b
~~~

## Flujo de datos y Estructuras de Control
La flexibilidad que nos aporta una variable nos permite transportarla de un lado a otro creando un flujo de datos. Y para controlar este flujo de datos tenemos las llamadas "estructuras de control de flujo de datos".

Imaginemos que tenemos una variable A a la que deseamos sumar un conjunto de numeros B. Diríamos a que a A le sumamos cada item de B. Si tenemos diez números en B, esta operación se realizará diez veces. Nuevamente, el modo óptimo es aquél que nos provea de la mayor flexibilidad posible. Para ello utilizaremos una estructura agnóstica, es decir una que no se vea afectada por los cambios de valores, y que actúe en bucle, es decir, que se repita de un modo definido.

En este caso, el bucle que se repite esta definido como "a A le sumamos cada item de B" y la tarea propiamente consiste en : localizar el conjunto B, seleccionar el primer item y sumarlo a A, para luego repetir con el siguiente hasta que se hayan procesado todos los items del conjunto B.

~~~~
# queremos sumar cada elemento de var_b a var_a
var_a = 1
var_b = [1, 2, 3, 4]

# modo ineficiente
result = var_a + 1
result = var_a + 2
result = var_a + 3
result = var_a + 4

# modo eficiente : estructura flexible
for item in var_b:
  result = var_a + item
~~~~

## Funciones
Las funciones nos dan la oportunidad de reutilizar nuestras variables y estructuras, es decir, nos permiten reutilizar nuestro código. Imaginemos que escribimos un programa en el cual debemos utilizar muchas veces las variables y la estructura que vimos anteriormente. Lo primero que podríamos pensar es en copiar/pegar las veces necesarias aquello que necesitemos. Esto provocaría que nuestro archivo se extendiera, además, en caso de haber un error, lo deberíamos buscar en cada fragmento de nuestro copia/pega. El peor de los casos vendría si escribiesemos un archivo con miles de líneas de código, nos obligaría a buscar en cada una e incluso, si el error estuviera ubicado sutilmente en una de ellas nos obligaría a escribir todo el archivo desde el principio por causa de ese error.

La opción más eficiente, en este caso, sería crear una estructura flexible que nos permitiera realizar la misma operación sin escribir cada paso de principio a fin cada vez que la utilicemos. Para lograr esto, flexibilidad y reutilización, podemos definir la estructura llamada "función". Gracias a las funciones, podemos escribir una vez el código que necesitamos pero reutilizar ese código cada vez que volvamos a necesitarlo, incluso si es necesario cambiar los valores que se procesan en ella.

~~~
# caso 1 : sumar dos números cualquiera
# definimos una función
def suma(var_a,var_b):
  result = var_a + var_b
  return result

# ejemplo de uso 1 :
suma(1,2) -> 3.00
suma(2,2) -> 4.00
suma(2,3) -> 5.00


# caso 2 : sumar a un número los números de una lista
# definimos una función
def sumarLista(num,lista):
  result = 0
  for item in lista:
    result += num + item
  return result

# ejemplo de uso 2 :
sumarLista(1,[1,2,3,4]) -> 14
sumarLista(2,[1,2,3,4]) -> 18
sumarLista(1,[5,6,7,8]) -> 30
sumarLista(2,[5,6,7,8]) -> 34
~~~

## La Librería
Una librería es el modo eficiente de reutilizar código. En el caso de la ciencia de datos, guardan código orientado a tareas específicas, por ejemplo construir un gráfico.

Al programar con Python, muchas librerías se encuentran ya instaladas con su distribución. En este caso, solo debemos importar la librería que deseamos utilizar en el archivo que deseamos utilizarla.

No todas las librerías existentes en el universo Python se encuentran preinstaladas pero se pueden instalar manualmente. Este no será nuestro caso.

En este tutorial utilizaremos tres librerías : "pandas" para cargar la base de datos en una variable de modo flexible y eficiente, "seaborn" para crear gráficos como el de regresión lineal, y "sklearn" para transformar variables categóricas en variables numéricas.

Para ello, imaginemos que estamos al comienzo de nuestro archivo de Python llamado "visualizacion.py". Como estas librerías estan preinstaladas en el corazón de nuestra distribución de Python, simplemente las importaremos, ya que no tenemos la necesidad de instalarlas manualmente.

~~~
# las importaremos del siguiente modo
# en la línea 1 escribiremos :

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


# Voilá! A partir de ahora,
# todas las variables y funciones de estas librerias
# estan disponibles en nuestro archivo "visualizacion.py"

~~~







































#
