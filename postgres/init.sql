-- Create tables
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department_id INT REFERENCES departments(id) ON DELETE SET NULL
);

-- Insert sample data
INSERT INTO departments (name) VALUES
  ('Operations'),
  ('Technical'),
  ('Marketing');

INSERT INTO employees (name, email, department_id) VALUES
  ('Alice Johnson', 'alice@example.com', 1),
  ('Bob Smith', 'bob@example.com', 2),
  ('Charlie Lee', 'charlie@example.com', 3);
