-- Crea la tabla para los usuarios
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    userName VARCHAR(80) UNIQUE NOT NULL,
    "password" VARCHAR(80) NOT NULL
);

-- Crea la tabla para las tareas
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    uuidTask UUID UNIQUE NOT NULL,
    userName VARCHAR(80) NOT NULL,
    title VARCHAR(120) NOT NULL,
    "description" VARCHAR(250),
    color VARCHAR(10),
    active BOOLEAN DEFAULT TRUE,
    preference INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);