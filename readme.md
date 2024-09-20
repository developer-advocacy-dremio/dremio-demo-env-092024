# Docker Compose Setup for Data Engineering with Nessie, MinIO, Spark, and Dremio

## Instructions

### How to Spin Up the Services

1. **Ensure Docker and Docker Compose are installed** on your system.
2. **Navigate to the directory** containing the `docker-compose.yml` file.
3. **Place Seed Data:**
   - For MinIO, place the files to be seeded into the bucket in `./minio-data`.
   - For Spark, place any notebooks or datasets in `./notebook-seed`.
4. **Run the following command** to start all the services:
```bash
   docker-compose up -d
```
5. Once they are all setup, make sure to initialize superset in its container.

```bash
docker exec -it superset superset init
```

[Blog on How to Connect Superset to Dremio](https://www.dremio.com/blog/bi-dashboards-101-with-dremio-and-superset/)

Everything should be up and running. You can access the services using the following URLs:

- **Spark/Notebook:** http://localhost:8888
- **Dremio:** http://localhost:9047
- **Superset:** http://localhost:8088
- **MinIO:** http://localhost:9001
- **Nessie:** http://localhost:19120 (no ui, API access only)
- **Postgres:** http://localhost:5435 or http://postgres:5432 within docker network

### How to Spin Down the Services
To stop and remove the running containers, use the following command:

```bash
docker-compose down
```

This will stop all the services and remove the containers. Data stored in volumes (./nessie-data, ./minio-data, ./notebook-seed) will persist.

To clear volumes and remove all data, use the following command:

```bash
docker-compose down -v
```

### Seed Data Locations
- **MinIO:** Files placed in the ./minio-data folder on your host will be copied into the datalake bucket inside MinIO during startup.
- **Spark:** The ./notebook-seed folder on your host is mounted to /workspace/seed-data inside the Spark container. You can place Jupyter notebooks or datasets in this folder to be available in the Spark environment.

### Accessing the Services
- **Nessie API:** Access the Nessie API at http://localhost:19120.
- **MinIO Web UI:** Access the MinIO Web UI at http://localhost:9001.
- **Spark Master Web UI:** Access the Spark Master Web UI at http://localhost:8080.
- **Spark Worker Web UI:** Access the Spark Worker Web UI at http://localhost:8081.
- **Spark History Server:** Access the Spark History Server at http://localhost:18080.
- **Jupyter Notebook (Spark): Access the Jupyter Notebook interface at http://localhost:8888.
- **Dremio Web UI:** Access the Dremio Web UI at http://localhost:9047.

## Notes
Ensure that the appropriate ports (listed above) are open and not blocked by firewalls.
The services will run in a shared Docker network called intro-network, allowing them to communicate with each other.

For persistent data storage, ensure the mounted directories (./nessie-data, ./minio-data, ./notebook-seed) exist on your local machine.