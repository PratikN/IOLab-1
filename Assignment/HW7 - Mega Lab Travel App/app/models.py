import sqlite3 as sql

def check_login(username, password):
    with sql.connect("trip.db") as con:

        print(username, password)
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        result = cur.execute("SELECT * from users WHERE username = ? AND password = ?", (username, password)).fetchall()
        print(len(result))
    return result

def friend_choices(user):
    with sql.connect("trip.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT id, username FROM users WHERE username != ?", (user,)).fetchall()
    choices = []
    for i in result:
        choices.append((str(i[0]), str(i[1])))
    return choices

def insert_trip(user_id, name, destination, friend_id):
    print("creating trip")
    with sql.connect("trip.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO trips (name, destination) VALUES (?,?)", (name, destination))
        trip_id = cur.lastrowid
        cur.execute("INSERT INTO makes (trip_id, user_id) VALUES (?,?)", (trip_id, user_id))
        cur.execute("INSERT INTO makes (trip_id, user_id) VALUES (?,?)", (trip_id, friend_id))
        con.commit()
    print("trip created!!!!!!")

def retrieve_trips(user_id):
    with sql.connect("trip.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = cur.execute("SELECT trips.id, name, destination FROM makes JOIN trips ON makes.trip_id=trips.id WHERE user_id = ?", (user_id)).fetchall()
    return result

def remove_trip(trip_id):
    with sql.connect("trip.db") as con:
        cur = con.cursor()
        cur.execute("DELETE from trips where id = ?", (trip_id))
        cur.execute("DELETE FROM makes where trip_id = ?", (trip_id))
        con.commit()
    print("trip deleted!!!!!!")
