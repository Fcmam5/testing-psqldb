# Exploiting PostgreSQL

* [Concurrency 00 (Multi-threads insertion)](./python-multithread-insertion)
* [Concurrency 01 (RT Chat application)](./node-chat-psql-storage)
* [Table inheritance]('#table-inheritance')

## Table inheritance

```
# We had a table named cars in our DB (conc_test)
conc_test> \d cars
+----------+---------+----------------------------------------------------+
| Column   | Type    | Modifiers                                          |
|----------+---------+----------------------------------------------------|
| id       | integer |  not null default nextval('cars_id_seq'::regclass) |
| name     | text    |                                                    |
| price    | integer |                                                    |
+----------+---------+----------------------------------------------------+
Indexes:
    "cars_pkey" PRIMARY KEY, btree (id)

```

Then We create a table `sport_cars` that inherits from `cars`
```sql
  CREATE TABLE sport_cars(                                                           
    team char(100)
  ) INHERITS (cars);
```
Now we can insert and query the elements of `sport_cars`, for example:
```sql
INSERT INTO sport_cars(name,price,team) VALUES ('Sonacom Sport',4000,'Algerian team');           
```

Examples of `SELECT` queries
```sql
conc_test> SELECT * from sport_cars WHERE name = 'Sonacom Sport';
+------+---------------+---------+------------------------------------------------------------
| id   | name          | price   | team                                                       
|------+---------------+---------+------------------------------------------------------------
| 49   | Sonacom Sport | 4000    | Algerian gang                                              
+------+---------------+---------+------------------------------------------------------------


conc_test> SELECT * from cars WHERE name = 'Sonacom Sport';
+------+---------------+---------+
| id   | name          | price   |
|------+---------------+---------|
| 49   | Sonacom Sport | 4000    |
+------+---------------+---------+

conc_test> SELECT * from cars WHERE price = 4000;
+------+---------------+---------+
| id   | name          | price   |
|------+---------------+---------|
| 49   | Sonacom Sport | 4000    |
+------+---------------+---------+

```
