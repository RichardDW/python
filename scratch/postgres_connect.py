#!/usr/bin/python
 
import psycopg2

#conn = psycopg2.connect(host="172.16.13.1",database="weather", user="postgres", password="Pa$$w0rd")
conn = psycopg2.connect(host="172.16.13.1",database="ispy", user="u_ispy", password="Pa$$w0rd")
cur = conn.cursor()

#cur.execute("INSERT INTO cities (date, city_name,averagetemp_celsius) VALUES (%s, %s, %s)",("05/08/2017", "Sydney", "16"))
#cur.execute("SELECT date, city_name, averagetemp_celsius from cities")
cur.execute("SELECT code, title, date_prod from event")
rows = cur.fetchall()
print(rows)
conn.commit()
cur.close()
conn.close()
 
#if __name__ == '__main__':
#   main()