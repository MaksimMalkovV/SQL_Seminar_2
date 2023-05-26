CREATE DATABASE IF NOT EXISTS Seminar_2; 	

USE Seminar_2;

-- 1. Создание таблицы seles
CREATE TABLE IF NOT EXISTS seles (
  id SERIAL PRIMARY KEY AUTO_INCREMENT,
  order_date DATE,
  count_product INT UNSIGNED NOT NULL
  );
  -- 1.2. Заполняем ее данными
  INSERT INTO seles (order_date, count_product) VALUES
  ('2022-01-01',156),
  ('2022-01-02',180),
  ('2022-01-03',21),
  ('2022-01-04',124),
  ('2022-01-05',341);
-- 2. Строктурируем значения в 3 сегмента
SELECT
	id AS "id заказа",
    IF(count_product < 100, "Маленький заказ", 
		IF(count_product BETWEEN 100 AND 300, "Средний заказ",
			IF(count_product > 300, "Большой заказ", "")))
	AS "Тип заказа"
FROM seles;

-- 3. Создание таблицы orders 
CREATE TABLE IF NOT EXISTS orders (
  id SERIAL PRIMARY KEY AUTO_INCREMENT,
  employee_id VARCHAR(4) NOT NULL,
  amount DECIMAL(10,2),
  order_status VARCHAR(10) NOT NULL
  );
  -- 3.1. Заполняем ее данными
  INSERT INTO orders (employee_id, amount, order_status) VALUES
  ('e03',15.00,'OPEN'),
  ('e01',25.50,'OPEN'),
  ('e05',100.70,'CLOSED'),
  ('e02',22.18,'OPEN'),
  ('e04',9.50,'CANCELLED');
  
  SELECT * FROM orders;
  -- 3.2. Запрос на "полный" статус заказа таблицы orders
  SELECT
	id,
    CASE
		WHEN order_status = "OPEN" THEN "Order is in open state"
        WHEN order_status = "CLOSED" THEN "Order is closed"
        WHEN order_status = "CANCELLED" THEN "Order is cancelled"
		END AS "full_order_status"
FROM orders;

-- 4. null - "значение ни определено" а 0 - арифметическое значение
  
  

