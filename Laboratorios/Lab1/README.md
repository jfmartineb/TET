Laboratorio 1 de Tópicos Especiales de Telemática
Juan Felipe Martínez Bedoya

Para utilizar el programa correr el main.py con parámetros de -p ##, donde ## es el número del puerto a utilizar.
ej: python main.py -p 80.
Ya luego en el navegador, introducir la dirección ip del servidor aws (34.238.124.2) y :## (el puerto ingresado) en el navegador de preferencia, este llevará al index.html, y luego en este mostrará las opciones de los otros archivos que se pueden obtener.

Para detener el programa se debe ingresar en el navegador /close, esto detendrá el socket. Si se desea volver a correr después de cerrarlo toca cerrar las pestaña del navegador y ahí sí se puede lanzar nuevamente el servidor. 
Ese problema presenta solo cuando el codigo es corrido en windows, si se corre en linux funciona ctrl-c para detener el programa.

Bibliografia:
- https://rico-schmidt.name/pymotw-3/http.server/index.html
- https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842
- https://github.com/AlejandroAlvarez4A/Python-Web-Servers/blob/master/server.py