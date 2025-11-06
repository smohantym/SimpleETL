
# Simple Spark ETL (Docker Compose)

This project runs a tiny Spark batch job that reads a CSV, aggregates totals by category, and writes a CSV output.

## Prerequisites
- Docker Desktop (Compose v2)

## Project layout
```
.
├─ app/
│  └─ etl.py
├─ data/
│  └─ sales.csv
├─ docker-compose.yml
└─ README.md

````

## Run
```bash
# From the project root
docker compose up --remove-orphans --pull always
````

You should see a success message: `✅ ETL job completed successfully!`

## Inspect results

Spark writes a folder with part files:

```
./data/output/csv/
  ├─ part-00000-*.csv
  └─ _SUCCESS
```

Open the `part-*.csv`; expected content:

```
category,total_sales
Clothing,130
Electronics,3200
```

## Troubleshooting

* If you get module errors, ensure Docker pulled the latest image:

  ```bash
  docker pull spark:3.5.1-python3
  ```
* If the container can't find `etl.py`, make sure your working directory is project root when running Compose, and the `app/` folder exists.
* If you need extra Python libraries, switch to a Dockerfile-based flow and install via `pip`. Example:

  ```dockerfile
  FROM spark:3.5.1-python3
  WORKDIR /app
  # COPY requirements.txt .
  # RUN pip install --no-cache-dir -r requirements.txt
  CMD ["/opt/spark/bin/spark-submit", "--master", "local[*]", "/app/etl.py"]
  ```

  And update `docker-compose.yml` to use `build: .` and (optionally) remove the `/app` bind mount if you COPY code into the image.

```
```
