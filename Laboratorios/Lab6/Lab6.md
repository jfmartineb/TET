# Laboratorio 5-1 Tópicos Especiales en Telemática
 por *Juan Felipe Martínez Bedoya* - jfmartineb@eafit.edu.co
 
 Para empezar, se debe trabajar con un cluster EMR, por lo que se crea con los parámetros que se ha hecho anteriormente
 
 ![image](https://user-images.githubusercontent.com/69642154/202961581-4e72d42d-ea1b-444c-aef2-687ee36a5dd1.png)

Luego a través de Putty nos conectamos al nodo master.
![image](https://user-images.githubusercontent.com/69642154/202961817-c5b7a446-d2ae-42d1-b8d6-0bf2d180cea0.png)

En este se deben indicar los siguientes comandos:
```bash
sudo yum install git -y
git clone https://github.com/st0263eafit/st0263-2022-2.git
cd st0263-2022-2
pyspark
```

De este nos debe aparecer el siguiente resultado:
![image](https://user-images.githubusercontent.com/69642154/202961986-d14e039d-0697-42bb-ab0a-46660d185fbc.png)

## Parte 1:
Ejecución del wordcount

### De forma interactiva desde pyspark con archivos desde el HDFS

![image](https://user-images.githubusercontent.com/69642154/202973059-beabf8ed-a347-4286-a470-2ecb811e14dd.png)
![image](https://user-images.githubusercontent.com/69642154/202973270-9bd2a604-0175-4073-a934-b30118a7cd1e.png)

### De forma interactiva desde pyspark con archivos desde S3
Antes hay que crear la carpeta y subir los archivos en el s3, esto se hizo desde la interfaz grafica de HUE

![image](https://user-images.githubusercontent.com/69642154/202975569-ee9ec16f-b133-443f-8920-89bbb900ef48.png)

Además,se subieron todos los datasets desde la interfazde S3 de AWS

![image](https://user-images.githubusercontent.com/69642154/202976136-54b96c79-2c33-415e-a6d0-dd24b103c990.png)

Resultado:

![image](https://user-images.githubusercontent.com/69642154/202976834-0d04a18f-dfe0-4a60-a188-95ba615b496a.png)

![image](https://user-images.githubusercontent.com/69642154/202976993-c883234b-03c7-4bf9-a7d3-b485522d1bc6.png)

![image](https://user-images.githubusercontent.com/69642154/202977066-db33a6b6-ff49-4fa0-a18a-5d1b7b09fd64.png)

### Como un archivo python

![image](https://user-images.githubusercontent.com/69642154/202973554-35efbe43-4726-4d3f-89a8-855550ee9240.png)
![image](https://user-images.githubusercontent.com/69642154/202973568-44e19e91-a0b1-417b-8a85-644555bec601.png)

### Desde zeppelin

![image](https://user-images.githubusercontent.com/69642154/202974716-c7d6949d-9209-42f1-a269-92ed6446b303.png)

### Desde un jupyter notebook

![image](https://user-images.githubusercontent.com/69642154/202977337-4227bfc2-37f5-480c-9784-a31f45824113.png)

![image](https://user-images.githubusercontent.com/69642154/202977389-629b5ae5-b311-4e21-a309-afc91690b26a.png)

## Parte 2

En esta parte se replicará unos comandos en un jupyter notebook. Para empezar lo que se hace es descargar una librería que permite crear sesiones en Spark, y luego se crea una que se nombró como *data_processing*.

![image](https://user-images.githubusercontent.com/69642154/202977743-56eab735-70f5-41ea-920b-558ea7f70d36.png)

Se carga un dataset del bucket s3

![image](https://user-images.githubusercontent.com/69642154/202979161-05cefe84-d478-4d48-b2b3-39bd106c5110.png)

Luego, se hacen las operaciones con esa tabla cargada. Para empezar se saca el nombre de las columnas:

![image](https://user-images.githubusercontent.com/69642154/202979337-74c485e9-5386-47b0-8177-9aff512ad382.png)

Cuantas columnas hay:

![image](https://user-images.githubusercontent.com/69642154/202979423-87c0897b-40cd-4949-a8ef-5ebc2620e4a0.png)

Cuantas filas hay:

![image](https://user-images.githubusercontent.com/69642154/202979458-5a9313fa-2e39-4fc4-999f-fc2782cd8fe3.png)

El tamaño como si fuera una matriz:

![image](https://user-images.githubusercontent.com/69642154/202979513-42258f80-b6bf-45e8-904c-acb2a3b09a0c.png)

El esquema (que tipo de variables hay en cada columna):

![image](https://user-images.githubusercontent.com/69642154/202979607-c5bc6c30-2c0f-4e0f-9f68-669adb2d6daf.png)

Mostrar las 5 primeras filas:

![image](https://user-images.githubusercontent.com/69642154/202979691-e88d86fc-2d11-4476-9a52-67bc5d05b872.png)

Seleccionar solo dos columnas y mostrar 5 filas:

![image](https://user-images.githubusercontent.com/69642154/202979752-7ff905b5-22bc-4de9-acc2-2c79c56328ee.png)

Mostrar algunos datos estadísticos de las columnas:

![image](https://user-images.githubusercontent.com/69642154/202979841-47d49817-2009-4543-b76d-8f8daa943f8a.png)

Se descarga una librería que permite hacer operaciones en las columans. En el primer ejemplo se suman 10 años a la columna de edad

![image](https://user-images.githubusercontent.com/69642154/202980017-ffec2b58-abc5-44b6-b6cd-deb411b2545c.png)

Se cambia el tipo a doble en la columna de edad:

![image](https://user-images.githubusercontent.com/69642154/202980209-8330e31a-6b5e-42cf-921d-695bc09b5040.png)

Luego se hacen operaciones de filtrado en diferentes columnas, donde se varian parámetros y se van agregando diferentes condiciones

![image](https://user-images.githubusercontent.com/69642154/202980496-2f517c64-bfff-499d-b28b-5b3a5bea1c9d.png)

Valores distintivos en una columna y cuantos diferentes hay

![image](https://user-images.githubusercontent.com/69642154/202980726-13554146-ff6c-4a37-afac-0633e42c6071.png)

Agrupar y contar, y además ordenar en un orden descendente

![image](https://user-images.githubusercontent.com/69642154/202980796-557b17cc-23be-49ac-8175-f1cdd54efd1f.png)

Agrupar por valores distintivos y realizar operaciones en ellos

![image](https://user-images.githubusercontent.com/69642154/202980864-93aee11e-2319-4186-800e-ed8334ce492b.png)

![image](https://user-images.githubusercontent.com/69642154/202980888-7ecc58db-f375-4e54-ae47-82b0212bc835.png)

![image](https://user-images.githubusercontent.com/69642154/202981013-d2c8dd53-bc7d-4b3e-a1bd-029b134b8ae3.png)

Se descarga una libreria para hacer funciones definidas por el usuario y se realizan algunos ejemplos

![image](https://user-images.githubusercontent.com/69642154/202981256-0f5e44e3-ffd6-49f7-a5f5-fba10e093a83.png)

Usando una función lambda

![image](https://user-images.githubusercontent.com/69642154/202981345-03213ed4-874b-4fef-9b36-0050c866e665.png)

Se descarga la librería para poder hacer funciones definidas por el usuario utilizando pandas, sin embargo, este está tieando erros por la versión instalada

![image](https://user-images.githubusercontent.com/69642154/202981679-b5f372be-1429-442f-a1f0-423ca2852267.png)

Se buscan los valores duplicados, y se eliminan

![image](https://user-images.githubusercontent.com/69642154/202981822-ba727d33-b98e-418a-96a1-707e3605fe07.png)

Se crea un nuevo *dataframe* de pandas, se elimina una columna y se muestra nuevamente

![image](https://user-images.githubusercontent.com/69642154/202981933-b267f7e9-03bd-4795-bdb2-dbcca06646e2.png)

Se almacen la información en la carpeta de *datasetsjfmartineb* primero como csv y luego en formato parquet (formato de columnas aceptado por muchas herramientas de procesamiento de datos)

![image](https://user-images.githubusercontent.com/69642154/202982435-a9d79903-0656-40e0-897e-0f078415004a.png)

![image](https://user-images.githubusercontent.com/69642154/202982491-3c55e22f-e41d-4445-8385-b2d763d71323.png)

![image](https://user-images.githubusercontent.com/69642154/202982543-f7fbc349-d859-4b31-b1cf-4c96a6b5cc4c.png)

![image](https://user-images.githubusercontent.com/69642154/202982586-aa63b9fb-beb5-41f6-bd3a-ee88b9969ee4.png)

Los archivos de parquet no tienen previsualización.








