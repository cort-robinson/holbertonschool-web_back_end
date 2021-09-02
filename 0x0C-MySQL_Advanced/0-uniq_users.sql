-- creates a table with unique users
-- id: int, email: string(255), name: string(255)
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255)
);
