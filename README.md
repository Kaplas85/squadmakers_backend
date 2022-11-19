# Reto Backend para SquadMakers

Este repositorio contiene todos los archivos para ejecutar una API hecha con:
- FastAPI
- MongoDB
- Docker & Docker Compose

Esto siguiendo las mejores practicas vigentes para el desarrollo en **FastAPI**.

## ¿Cómo ejecutar el código?
Para evitar instalaciones y lograr un rápido despliegue se usó docker y docker compose

⚠ Si tiene una versión de Docker Compose < 2 ten en cuenta que el comando `docker compose` puede no funcionarte y deberás usar `docker-compose` o si tienes una versión más reciente, en vez de usar `docker compose` podrás usar `compose`.

### Primero, creamos el archivo .env

| Nombre de la Variable | Ejemplo                                      | Valor                                                                                              |
| --------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| DATABASE_URL          | mongodb://username:password@host:port/dbname | mongodb://squadMakersUsername:squadMakersPassword@mongo:27017/squadMakersDatabase?authSource=admin |

Por buenas practicas y por unicamente fines educativos, se dejan las credenciales aquí, las cuales tambien pueden encontrar en el archivo `docker-compose.yml` y de querer, pueden modificarlo.

### Segundo, levantamos el entorno con Docker
Sencillamente procederemos a escribir en nuestra shell

```bash
docker compose up -d
```

Esto empezará a descargar las imagenes de MongoDB y Python 3.10.6

### Tercero, testeamos

Como estamos usando un entorno Docker, se deben probar directamente en el entorno. Para eso, sencillamente usamos
```bash
docker compose exec back pytest
```
❗ Todos los test se encuentran en la carpeta `tests`

### Probar la API y ver la documentación

Para poder ver la documentación interactiva de FastAPI, se deberá ingresar a http://localhost:8000/docs ahí podrán probar de forma inmediata todos los endpoints.

❗ Si quieren ver los logs en vivo, pueden usar:
```bash
# Para ver unicamente el back
docker compose logs -f back

# Para ver unicamente la db
docker compose logs -f mongo

# Para ver todos
docker compose logs -f
```
</br>
<hr/>
</br>
Gracias por su tiempo.