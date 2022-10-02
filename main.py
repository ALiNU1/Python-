import psycopg2 
from confic import host, user, password, database

try:
    connection = psycopg2.connect(
        host = host, 
        user = user, 
        password = password,
        database = database
    )

    connection.autocommit = True

    with connection.cursor() as cursor:
        #Проверка postgreSQL
        cursor.execute("SELECT version();")
        print(cursor.fetchall())

    with connection.cursor() as cursor:
        #Создаем новую талицу
        cursor.execute("""CREATE TABLE python (
            id serial PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            age integer);""")

        print("CREATE TABLE")

    with connection.cursor() as cursor:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = int(input("Age: "))
        cursor.execute(f"INSERT INTO python (first_name, last_name, age) VALUES ('{first_name}', '{last_name}', {age});")
        print("INSERT 0 1")

    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM python;")
    #     print(cursor.fetchall())
    
    # with connection.cursor() as cursor:
    #     cursor.execute("DELETE FROM python WHERE last_name = 'IT';")

    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM python;")
    #     print(cursor.fetchall())
    
    # with connection.cursor() as cursor:
    #     cursor.execute("DROP TABLE python;")
    #     print("DROP TABLE")

except Exception as error:
    print(error)

# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print("Closed PostgreSQL")


