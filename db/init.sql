CREATE TABLE IF NOT EXISTS cars (
    id SERIAL PRIMARY KEY,
    year INT,
    name TEXT,
    price BIGINT,
    description TEXT,
    viewing INT,
    posted_info TEXT
);

COPY cars(year, name, price, description, viewing, posted_info)
FROM '/docker-entrypoint-initdb.d/car_info.csv'
DELIMITER ','
CSV HEADER;
