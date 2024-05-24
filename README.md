## Database Model - University <br>
##### *Author: Luiggi Paschoalini Garcia - RA: 22.122.006-4*
##### *Subject: CC5232 - Database* <br><br>

#### Relational Diagram: <br>
![Relational Diagram drawio](https://github.com/luiggigarcia/database_model_universityExample/assets/83616830/f6ff0d7c-f16b-467f-ae14-901ed9ae5aea)

1. To use this model you can test with Cockroachdb, Postgresql or Dbeaver database.
2. First clone the repository.
3. To create all tables in the model you should use the DDL file that is in sql_code directory (sql_code/ddl.sql)
4. Next step you can generate the SQL code (DML) with the generate_data.py that is in sql_code directory (sql_code/generate_data.py), this file generate a script.txt file contained the sql code for insertions in all tables.
5. Before you run the generate_data.py install the lib faker (pip install faker) in the cli.
6. To run the generate_data.py only is necessary write ( python generate_data.py)  in cli.
7. To do the queries in database the DQL file is in sql_code directory (sql_code/dql.sql) with 5 queries required by project.

