SELECT SUM(Quantity * UnitPrice) FROM sales;

SELECT Country, SUM(Quantity * UnitPrice)
FROM sales
GROUP BY Country;