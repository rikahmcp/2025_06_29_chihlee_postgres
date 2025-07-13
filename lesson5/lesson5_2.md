## 創立員工及部門的關聯式表格
```sql
/*刪除舊表格 */
DROP TABLE IF EXISTS employee CASCADE;
DROP TABLE IF EXISTS branch CASCADE;

/*創立employee表格 */
CREATE TABLE employee(
	emp_id SERIAL,
	name VARCHAR(20),
	birth_date DATE,
	sex VARCHAR(1),
	salary INT,
	branch_id INT,
	sup_id INT,
 	PRIMARY KEY(emp_id)
);

/*創立branch表格 */
CREATE TABLE branch(
	branch_id INT,
	branch_name VARCHAR(20),
	manager_id INT,
	PRIMARY KEY(branch_id),
	FOREIGN KEY(manager_id) 
	REFERENCES employee(emp_id) ON DELETE SET NULL
);

/*補上employee少設的2個Foreign key */
ALTER TABLE employee
ADD FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL;

ALTER TABLE employee
ADD FOREIGN KEY(sup_id) REFERENCES employee(emp_id) ON DELETE SET NULL;


```