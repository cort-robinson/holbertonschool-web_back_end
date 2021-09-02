-- Creates a table users with the following columns:
-- id: integer, never null, autoincrement, primary key
-- email: string(255), not null, unique
-- name: string(255)
-- country, enumeration of values: US, CO, and TN, default is US, not null
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
