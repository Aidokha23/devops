from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

@app.get("/cars")
def get_cars():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "car_db"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "postgres"),
        host=os.getenv("POSTGRES_HOST", "car-db"),
        port=5432
    )
    cur = conn.cursor()
    cur.execute("SELECT year, name, price, description, viewing, posted_info FROM cars;")
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    return [dict(zip(columns, row)) for row in rows]
