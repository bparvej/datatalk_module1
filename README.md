# Data Pipeline Simple

this is a data pipeline where you will store datasets in CSV or prequet format into the data folder and run the service data_ingest to load data into postgresql db you can check data using container based pg admin as well

useful commands to run this pipeline

docker compose up -d --build
docker logs data_ingest


Access pgAdmin: Go to http://localhost:5050 in your browser. Login with pgadmin@pgadmin.com / pgadmin.

To connect to the DB: Use host db, port 5432, user postgres.