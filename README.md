# datatalk_module1
for learning purposes only

install Docker first

# question 1

          docker run -it --rm --entrypoint bash python:3.13

What this does:

-it → interactive terminal

--rm → container auto-deletes after exit

--entrypoint bash → overrides default python entrypoint

python:3.13 → the image required

              
              pip --version

# question 2
      
Build a docker container with pgadmin 
```
services:
  db:
    container_name: postgres
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: 'postgres'
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_DB: 'ny_taxi'
    ports:
      - '5433:5432'
    volumes:
      - vol-pgdata:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: "pgadmin@pgadmin.com"
      PGADMIN_DEFAULT_PASSWORD: "pgadmin"
    ports:
      - "8080:80"
    volumes:
      - vol-pgadmin_data:/var/lib/pgadmin

volumes:
  vol-pgdata:
    name: vol-pgdata
  vol-pgadmin_data:
    name: vol-pgadmin_data

```

Answer: postgres:5432

        db:5432


Mount data into DB
add data folder in volume of docker container to create an easy pipeline we will also need Python and SQLAlchemy 
```
 db:
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: ny_taxi
    ports:
      - "5433:5432"
    volumes:
      - vol-pgdata:/var/lib/postgresql/data
      - ./data:/data
```      

