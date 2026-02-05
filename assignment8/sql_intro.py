import sqlite3

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} is in the database already ")

def add_magazine(cursor, name, publisher_name):
    cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
    results = cursor.fetchall()
    if len(results) > 0:
        publisher_id = results[0][0]
    else:
        print(f"no publisher named '{publisher_name}'")
        return
    
    try:
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"Magazine '{name}' already in database ")

def add_subscriber(cursor, name, address):
    cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
    results = cursor.fetchall()
    if len(results) > 0:
        print(f"Subscriber '{name}' in '{address}' in databasea already")
        return
    
    cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))

def add_subscription(cursor, subscriber_name, subscriber_address, magazine_name, expiration_date):
    cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?", (subscriber_name, subscriber_address))
    results = cursor.fetchall()
    if len(results) > 0:
        subscriber_id = results[0][0]
    else:
        print(f"no subscriber named '{subscriber_name}'")
        return
    
    cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
    results = cursor.fetchall()
    if len(results) > 0:
        magazine_id = results[0][0]
    else:
        print(f"no magazine named '{magazine_name}'")
        return
    
    cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
    results = cursor.fetchall()
    if len(results) > 0:
        print(f"Subscriber '{subscriber_name}' is subscribed to '{magazine_name}'")
        return
    
    cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date))

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
        )
        """)

        print("Database created")

        add_publisher(cursor, "Time Inc.")
        add_publisher(cursor, "National Geographic Society")
        add_publisher(cursor, "Dotdash Meredith")
        add_publisher(cursor, "Rolling Stone LLC")

        add_magazine(cursor, "Time Magazine", "Time Inc.")
        add_magazine(cursor, "Sports Illustrated", "Time Inc.")
        add_magazine(cursor, "National Geographic", "National Geographic Society")
        add_magazine(cursor, "People", "Dotdash Meredith")
        add_magazine(cursor, "Rolling Stone", "Rolling Stone LLC")

        add_subscriber(cursor, "Michael Jordan", "23 Bulls Way, Chicago, IL")
        add_subscriber(cursor, "Pam Beesly", "1725 Slough Avenue, Scranton, PA")
        add_subscriber(cursor, "Buckley Barnes", "1941 Liberty Lane, Brooklyn, NY")
        add_subscriber(cursor, "Leslie Knope", "1212 Pawnee Blvd, Pawnee, IN")

        add_subscription(cursor, "Michael Jordan", "23 Bulls Way, Chicago, IL", "Sports Illustrated", "2027-02-05")
        add_subscription(cursor, "Michael Jordan", "23 Bulls Way, Chicago, IL", "Time Magazine", "2026-11-11")
        add_subscription(cursor, "Pam Beesly", "1725 Slough Avenue, Scranton, PA", "People", "2026-08-20")
        add_subscription(cursor, "Buckley Barnes", "1941 Liberty Lane, Brooklyn, NY", "National Geographic", "2027-05-30")
        add_subscription(cursor, "Leslie Knope", "1212 Pawnee Blvd, Pawnee, IN", "Time Magazine", "2026-12-25")
        add_subscription(cursor, "Leslie Knope", "1212 Pawnee Blvd, Pawnee, IN", "People", "2027-01-01")

        conn.commit()
        print(" data inserted .")

        print("Query 1: All subscribers")
        cursor.execute("SELECT * FROM subscribers")
        results = cursor.fetchall()
        for row in results:
            print(row)

        print("Query 2: All magazines sorted by name ")
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        results = cursor.fetchall()
        for row in results:
            print(row)

        print("Query 3: Magazines for 'Time Inc.' publisher")
        cursor.execute("SELECT m.name, p.name FROM magazines m JOIN publishers p ON m.publisher_id = p.publisher_id WHERE p.name = 'Time Inc.'")
        results = cursor.fetchall()
        for row in results:
            print(row)

except sqlite3.Error as e:
    print(f"Database Error: {e}")