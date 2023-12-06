# Calculadora Gráfica

## Descripción
El programa consiste en una calculadora gráfica la cual es capaz de realizar cálculos matemáticos básicos como suma, resta, multiplicación o división con números enteros y con funciones específicas como sen, cos o exponencial, y además de permitir realizar los cálculos tambien permite realizar la graficación en dos dimensiones de las funciones mencionadas anteriormente y combinaciones de estas. Por lo tanto, resulta ser de gran utilidad para personas que deseen observar la gráfica de las funciones que están trabajando a la vez que reliza cálculos y observa los cambios en la gráfica.

El programa en python presenta una interfaz gráfica, que corresponde a la pantalla y los botones de una calculadora además del espacio para mostrar gráficas y los espacios para modificar los límites de la gráfica, creada mediante la librería Tkinter, cuando el usuario presiona alguno de los botones aparecerá su correspondiente número, símbolo u operación en la pantalla. Hay botones con funciones especiales como lo son el igual "=" que se encarga de calcular el resultado de una operación escrita y mostrarlo en la pantalla, el de graficar "Graph" que se encarga de generar la gráfica de la función escrita y mostrarla al usuario, y el botón de borrar "Clear" que se encarga de borrar todo lo que aparezca en la pantalla. El usuario puede realizar la cantidad de operaciones o gráficas que desee y cuando quiera finalizar solo debe cerrar la ventana del programa.

### Estructura del programa

<a href="https://imgbb.com/"><img src="https://i.ibb.co/SJsRy0N/imagen-2023-12-05-163027320.png" alt="imagen-2023-12-05-163027320" border="0"></a>

La estructura del programa se realizó mediante difrentes clases, las cuales implementan las diferentes funciones para la calculadora, por ejemplo, la clase Interfaz se encarga de abrir la ventana que representa la interfaz gráfica de la calculadora con los botones y la pantalla así como el espacio para las gráficas de funciones. En esta clase es donde se reciben las entradas enviadas por el usuario mediante los botones y se invocan las clases y métodos encargados de resolver o graficar lo deseado. Otra clase incluida es la de Graficar la cual recibe la entrada del usuario en la calculadora y la interpreta para detectar las funciones correspondientes y graficarlas en el espacio para esto, ahí mismo se manejan excepciones al momento de graficar. La tercera clase es la de Calcular la cual recibe la entrada envida por el usuario y la interpreta para obtener el resultado de la operación deseada, ahí tambien se manejan excepciones al momento de calcular el resultado.

### Objetivos
1. Desarrollar una herramienta para visualizar las funciones ingresadas por el usuario.
2. Implementar una interfaz gráfica amigable con el usuario.

### Limitaciones
1. No se logró desarrollar un método para borrar el último digito ingresado por el usuario, por lo que se dejó el método de Clear que borra todo lo que aparece en la pantalla.
2. Algunas funciones pedían más argumentos de los que se trabajaron para ser graficadas por lo que se tuvo que limitar a fuciones más sencillas.

## Instalación
Para usar el programa solo es necesario ejecutar el archivo .py con el código fuente correspondiente a este, pero si es necesario instalar en el equipo las dependencias del código si no están instaladas, estas dependencias se encuentran en el archivo requirements.txt presente en este repositorio y solamente es necesario ejecutar el comando: `pip install -r requirements.txt` en el entorno de python respectivo a la terminal de cada sistema operativo.

## Uso
Para ejecutar el programa debe descargar el archivo con el código fuente desde este repositorio e ingresar al directorio donde se encuentra este en su computadora, ahí debe abrir la terminal de su sistema operativo y escribir alguno de los siguientes comandos `python Proyecto_Final_Calculadora.py` o `python3 Proyecto_Final_Calculadora.py`.

Una vez ejecutado el programa aparecerá una ventana con la interfaz de la calculadora, en esta el usuario podrá presionar los botones que desee para realizar operaciones de suma, resta, multiplicación, o división ya sea con números enteros o con expresiones como sen, cos o exponencial. Para obtener el resultado de estas operaciones se debe presionar el botón de igual "=" después de escribir toda la operación y el resultado de esta aparecerá en la pantalla, si desea realizar otra operación solo debe escribirla y en la pantalla desaparecerá el resultado anterior y aparecerá la nueva operación. Si se escribe una operación que resulta en un error (como dividir entre cero) o se utiliza el botón de "x" para intentar calcular una operaión el programa detectará el error y se mostrara en la pantalla de la calculadora que ocurrió un error.

Si el usuario desea observar la gráfica de alguna función entre las opciones incluidas o combinaciones de estas deberá utilizar la variable "x" donde corresponda y especificar los límites para el eje horizontal en los espacios correspondientes, así cuando tenga la función y los límites listos deberá presionar el botón para graficar "Graph" así se actualizará el espacio de la gráfica con la función deseada, si se desea realizar la gráfica de otra función solo debe escribir la nueva función y volver a presionar el botón de graficar así desaparecerá la gráfica anterior y aparecerá la nueva gráfica correspondiente a la nueva función. Además de los botones el programa también es compatible con la entrada de teclado del equipo, por lo tanto mediante este se pueden escribir más funciones que las que se muestran en los botones, mientras se mantenga la estructura correcta de esta. Cabe resaltar que solo se realizan gráficas en 2 dimensiones, debido a esto solo existe la variable "x". Si no se incluye la variable "x" o no se usan los símbolos correspondientes a cada operación el programa detectará un error y se mostrará en la pantalla de la calculadora que ocurrió un error al graficar. 

Si el usuario se equivoca al escribir una operación o una función o solamente desea borrar lo que escribió deberá utilizar el botón "Clear" para borrar todo lo que se muestra en la pantalla y dejarla en blanco de nuevo.

Cuando se desee finalizar la ejecución del programa solamente es necesario cerrar la ventana correspondiente a este, y si se desea volver a abrir deberá ejecutar el código fuente en el entorno de python nuevamente.

## Ejemplos de uso

### Operaciones con números y funciones

<a href="https://ibb.co/0M0LSXs"><img src="https://i.ibb.co/fp3W5SD/imagen-2023-12-05-144443131.png" alt="imagen-2023-12-05-144443131" border="0"></a>

Como se observa en la figura las operaciones se pueden escribir como en una calculadora normal, utilizando cada símbolo de operación donde corresponda, y al presionar "=" se muestra el resultado, como se observa en la siguiente figura.

<a href="https://ibb.co/9HNdScz"><img src="https://i.ibb.co/b5PGDQq/imagen-2023-12-05-144818709.png" alt="imagen-2023-12-05-144818709" border="0"></a>

### Gráficas de fuciones

<a href="https://ibb.co/CH98Jfv"><img src="https://i.ibb.co/bKvmHkL/imagen-2023-12-05-145209906.png" alt="imagen-2023-12-05-145209906" border="0"></a>

En esta figura se puede observar como se deben escribir las funciones para realizar su graficación, utilizando cada símbolo de operación y la variable "x" donde corresponde. Además, tambien se modificaron los límites en el eje horizontal de la gráfica para observar más de esta, por último se presionó el botón "Graph" para mostrar la gráfica.
