# Laboratorio 5-1 Tópicos Especiales en Telemática
 por *Juan Felipe Martínez Bedoya* - jfmartineb@eafit.edu.co
 
## Crear el cluster EMR
Se empieza con la creación de un cluster de EMR en AWS
![image](https://user-images.githubusercontent.com/69642154/200090494-2ce99c60-9846-4e11-8b2f-6012dd2f78b8.png)

Luego en la parte inferior se puede añadir texto donde se coloca el siguiente código:
```bash
[
    {
        "Classification": "jupyter-s3-conf",
        "Properties": {
            "s3.persistence.enabled": "true",
            "s3.persistence.bucket": "notebooksjfmartineb"
        }
    }
]
```

Se presiona next y se cambian los nodos del cluster para que se vean como en la siguiente imagen
![image](https://user-images.githubusercontent.com/69642154/200090537-cb9fd48e-5f92-40db-aa01-508c48d5a657.png)

Luego se habilita la terminación automática y se modifica el tamaño en GB del “Root Volume”
![image](https://user-images.githubusercontent.com/69642154/200090549-59fb98a0-6696-43fd-abd0-a71b245b0fd6.png)

Luego se presiona next y se le cambia el nombre a la instancia que se va a crear
![image](https://user-images.githubusercontent.com/69642154/200090563-889308b3-7b73-4a78-9771-e5b0e2671292.png)

Se presiona next y sigue la parte de las opciones de seguridad, donde se selecciona un par de seguridad previamente creado, en mi caso se llama TET, finalmente se procede a crear el cluster, el cual toma un aproximado de 20 min.
![image](https://user-images.githubusercontent.com/69642154/200090574-1f979d2d-2236-41cb-bcf0-573cd3728e84.png)
![image](https://user-images.githubusercontent.com/69642154/200090581-84962325-a36d-4007-8a8d-229d2f23ff6e.png)

Cuando termine de correr se debe ver de la siguiente manera:
![image](https://user-images.githubusercontent.com/69642154/200090590-28c51a6a-a5ee-475d-bf1d-0b2455a867d8.png)

## Crear el Bucket
Al terminar la creación del cluster, se sigue a crear un Bucket S3 de AWS, el cual se le dará el mismo nombre del que se dio anteriormente.
![image](https://user-images.githubusercontent.com/69642154/200090619-a483cbd5-7d30-4a6f-a418-fc648322e287.png)

Se le da luego a crear el bucket y se vuelve a la pestaña de EMR para conectarnos al nodo master del cluste.

## Conexión vía PuTTy
Luego para conectarse al nodo principal del cluster se descarga la aplicación de putty, la que se conecta por ssh utilizando las claves previamente creadas
![image](https://user-images.githubusercontent.com/69642154/200090643-bd453ca3-1c3a-490d-bc06-a16354ac630d.png)

Antes de intentar la conexión, se selecciona el cluster EMR, y  toca ir a los diferentes grupos de seguridad y añadir el trafico TCP por los puertos 22, 8888, 8443, 9443. Además se selecciona la clave .ppk almacenada para permitir la conexión. Finalmente cuando nos conectemos se verá así:
![image](https://user-images.githubusercontent.com/69642154/200090723-871a0931-9184-4e06-981d-4c8c525f1287.png)

## Problemas
Para utilizar los diferentes servicios de EMR obtuve los mismos errores cada vez:
![image](https://user-images.githubusercontent.com/69642154/200090788-9bb3f70e-870d-44d6-9436-d951e1671018.png)
 , por lo cual no pude utilizar ninguno de los servicio. Además otro error que se presentaba era:
 ![image](https://user-images.githubusercontent.com/69642154/200090798-ec30b3f0-c1e3-43c3-aa60-917e2950bf47.png)
Sin importar que ya allá activado los puertos en los security group.

Dado esto no se pudo acceder a ninguno de los servicios.
