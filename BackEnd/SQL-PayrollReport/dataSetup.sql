CREATE TABLE Payroll (EmployeeId INT, Paycode VARCHAR(100), Hours DECIMAL(12, 4), Rate DECIMAL(12, 4), FlatAmount DECIMAL(12, 4));
CREATE TABLE Employees (EmployeeId INT, Employee VARCHAR(100));

INSERT INTO Payroll
    (EmployeeId, Paycode, Hours, Rate, FlatAmount)
VALUES
    (001, 'Regular', 11.25, 15.21, 0.00),
    (002, 'Regular', 9.00, 15.00, 0.00),
    (002, 'Regular', 8.00, 15.00, 0.00),
    (001, 'Overtime', 3.86, 22.82, 0.00),
    (005, 'Salary', 0.00, 0.00, 2133.67),
    (002, 'Regular', 8.00, 15.00, 0.00),
    (003, 'Regular', 7.60, 18.50, 0.00),
    (002, 'Regular', 8.00, 15.00, 0.00),
    (004, 'Bonus', 0.00, 0.00, 500.00),
    (003, 'Regular', 10.76, 18.50, 0.00),
    (001, 'Regular', 6.50, 15.21, 0.00),
    (004, 'Regular', 8.67, 19.25, 0.00),
    (001, 'Bonus', 0.00, 0.00, 250.00),
    (004, 'Regular', 10.21, 19.25, 0.00),
    (004, 'Regular', 9.33, 19.25, 0.00),
    (002, 'Overtime', 5.89, 22.50, 0.00),
    (003, 'Regular', 8.25, 18.50, 0.00),
    (001, 'Regular', 12.75, 15.21, 0.00),
    (001, 'Regular', 9.50, 15.21, 0.00),
    (002, 'Regular', 7.00, 15.00, 0.00);

INSERT INTO Employees
    (EmployeeId, Employee)
VALUES
    (001, 'John Doe'),
    (002, 'Jane Schmidt'),
    (003, 'Matt Smith'),
    (004, 'Chase Jones'),
    (005, 'David Evans');
    
    
