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


