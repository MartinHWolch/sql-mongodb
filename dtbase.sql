-- Crear tabla gerentes
CREATE TABLE gerentes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT NOT NULL,
    ciudad VARCHAR(100) NOT NULL
);

-- Crear tabla empresas
CREATE TABLE empresas (
    id SERIAL,
    nombre VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(100) NOT NULL,
    gerente_id INT NOT NULL,
    PRIMARY KEY (id, gerente_id)
);

-- Crear tabla boletas
CREATE TABLE boletas (
    id SERIAL,
    empresa_id INT NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    fecha DATE NOT NULL,
    PRIMARY KEY (id, empresa_id)
);