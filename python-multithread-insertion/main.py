import psycopg2
import thread
import time


car_list = (
    (
        ('Audi', 52642),
        ('Mercedes', 57127),
        ('Skoda', 9000),
    ),
    (
        ('Volvo', 29000),
        ('Bentley', 350000),
        ('Citroen', 21000),
    ),
    (
        ('Hummer', 41400),
        ('Volkswagen', 21600),
        ('Renault', 21600),
    ),
    (
        ('Honda', 41400),
        ('Hunday', 21600),
        ('Peugeot', 21600),
    ),
    (
        ('Toyota', 41400),
        ('Suzuki', 21600),
        ('Mazda', 21600),
    ),
    (
        ('Fiat', 41400),
        ('Kia', 21600),
        ('Sonacom', 21600),
    ),
)

def insert_data(cars, thread_name):
    try:
        print 'Starting %s\n' % (thread_name)
        conn = psycopg2.connect(database = "conc_test", user = "abdeldjalil",
                password = "igmo", host = "127.0.0.1", port = "5432")
        cursor = conn.cursor()
        query = "INSERT INTO Cars ( Name, Price) VALUES (%s, %s)"
        cursor.executemany(query, cars)
        conn.commit()
        print 'The thread %s has finished\n' % (thread_name)

    except Exception as e:
        print "The %s has failed\n" % (thread_name)
        print e

if __name__ == '__main__':

    try:
        conn = psycopg2.connect(database = "conc_test", user = "abdeldjalil",
                password = "igmo", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS Cars")
        cur.execute("CREATE TABLE Cars(id serial PRIMARY KEY, Name TEXT, Price INT)")
        conn.commit()
        time.sleep(3)

        # Launch threads !
        try:
           thread.start_new_thread( insert_data, (car_list[0], "Thread-1",) )
           thread.start_new_thread( insert_data, (car_list[1], "Thread-2",) )
           thread.start_new_thread( insert_data, (car_list[2], "Thread-3",) )
           thread.start_new_thread( insert_data, (car_list[3], "Thread-4",) )
           thread.start_new_thread( insert_data, (car_list[4], "Thread-5",) )
           thread.start_new_thread( insert_data, (car_list[5], "Thread-6",) )

           time.sleep(5)
        except:
           print "Error: unable to start thread"

    except Exception as e:
        print "Uh oh, can't connect. Invalid dbname, user or password?"
        print e
