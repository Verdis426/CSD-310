# CSD-310
# Module 7 - Movies: Update & Deletes
# Name: Verdis Moorer

import mysql.connector


def show_films(cursor, title):
    cursor.execute(
        "SELECT film_name AS Name, film_director AS Director, "
        "genre_name AS Genre, studio_name AS Studio "
        "FROM film "
        "INNER JOIN genre ON film.genre_id = genre.genre_id "
        "INNER JOIN studio ON film.studio_id = studio.studio_id"
    )

    films = cursor.fetchall()

    print("\n" + title)
    print("-" * len(title))

    for film in films:
        print(
            "Name: {}\nDirector: {}\nGenre: {}\nStudio: {}\n".format(
                film[0], film[1], film[2], film[3]
            )
        )


# Connect to the movies database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="677871",
    database="movies"
)

cursor = db.cursor()

# Display the original films
show_films(cursor, "DISPLAYING FILMS")

# Insert a new film
cursor.execute(
    "INSERT INTO film "
    "(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) "
    "VALUES (%s, %s, %s, %s, %s, %s)",
    ("The Shining", 1980, 146, "Stanley Kubrick", 1, 1)
)

db.commit()

# Display films after the insert
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Update Alien to Horror
cursor.execute(
    "UPDATE film "
    "SET genre_id = 1 "
    "WHERE film_name = 'Alien'"
)

db.commit()

# Display films after the update
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

# Delete Gladiator
cursor.execute(
    "DELETE FROM film "
    "WHERE film_name = 'Gladiator'"
)

db.commit()

# Display films after the delete
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

cursor.close()
db.close()