DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS tags;

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price FLOAT,
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
    tag_id INT REFERENCES tags(id) ON DELETE CASCADE,
    timestamp TIMESTAMP

);