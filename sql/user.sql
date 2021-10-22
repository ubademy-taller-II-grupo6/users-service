CREATE TABLE users(
    user_id SERIAL,
    user_name VARCHAR(255) NOT NULL,
    user_lastname VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) unique NOT NULL,
    primary key (user_id)
)