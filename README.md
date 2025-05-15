# Pequeño experimento con Docker Swarm y Python
Este proyecto consiste en un despliegue sobre Docker Swarm de una aplicación simple, dividida en Frontend y Backend. El Backend publica una API en el puerto que ofrece el valor, en segundos, del tiempo transcurrido desde el 1 de enero de 1970.
El frontend consume la información de la API y la ofrece como una página web.  


## ❗Advertencia
Esta aplicación *NO* debe desplegarse en un entorno de producción, ya que se ejecuta con Flask en modo Debugg y los contenedores no han sido creados para que sean seguros (se ejecutan como root, las imágenes de base ofrecen demasiada superficie). 

## Frontend
La aplicación del frontend publica la página web en el puerto 8080. En el fichero backend.Dockerfile. Sin embargo, en el fichero docker-swarm.yml se mapea dicho puerto al 80, empleado por defeto por todos los navegadores, para permitir el acceso de forma más sencilla.

La aplicación del frontend consume la API del backend, a través de la URL pasada como parámetro al iniciarla. En el despliegue se aprovecha la funcionalidad de balanceo de carga de Docker Swarm, al hacer que la URL sea el nombre del servicio de Backend. 

## Backend
La aplicación del backend publica la API en el puerto 5000, dentro del directorio "/api". El frontend está diseñado para que consuma dicho puerto y directorio de la URL pasada por parámetro. 
