# import psycopg2
# from pprint import pprint

# with psycopg2.connect(user = "python", password = "class2020",host = "localhost",port = "5432", database = "postgres") as connection:
#     cursor = connection.cursor()
#     print("Print postgres server infomation")
#     print(connection.get_dsn_parameters(), "\n")
#     cursor.execute("SELECT version();")
#     record = cursor.fetchone()
#     print("You are connected to - ", record, "\n")