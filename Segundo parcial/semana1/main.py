import psycopg2

conexion = psycopg2.connect(user="postgres", password="admin", host="127.0.0.1",
                            port="5432", database="clase_db")

cur = conexion.cursor()
cur.execute("SELECT * FROM public.\"personas\"")
records = cur.fetchall()  # All records
record = cur.fetchone()  # Single records

print(records)
