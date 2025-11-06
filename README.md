
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
