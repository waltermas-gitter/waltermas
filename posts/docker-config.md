Como cambiar la carpeta donde guarda las imagenes docker por default.  

```shell
sudo nvim /etc/docker/daemon.json
``` 


Crear el archivo si no existe.

```shell
{
  "data-root": "/run/media/SATURN/docker-images"
}
``` 


