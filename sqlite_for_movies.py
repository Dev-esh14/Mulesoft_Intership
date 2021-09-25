#importing the sqlite3 database to this file.
import sqlite3

#creating a try and exception block if any error occured during the process.
try:
    # creating a database with name = moviesdata and making a connection with it.
    connector = sqlite3.connect('MoviesDataBase.db')
    cur = connector.cursor()
    print("Created and Opened Database successfully !!!")
    
        
    '''creating a new table with name = Movies with parameters such as,
       movie name, actor name, actress name,director name and 
       finally year of release of the movie.'''
    cur.execute("""CREATE TABLE MOVIES(MOVIE_NAME TEXT, ACTOR_NAME TEXT, ACTRESS_NAME TEXT, DIRECTOR_NAME TEXT, YEAR_OF_RELEASE_MOVIE INT) """)
    print("Table created Successfully !!!")
    
    #Insering the values in the Movies table.
    cur.execute("INSERT INTO MOVIES VALUES('Tenet','Robert Pattinson','Elizabeth Debicki','Christopher Nolan',2020)")
    cur.execute("INSERT INTO MOVIES VALUES('Amazing Spiderman','Andrew Garfield','Emmastone','Marc Webb',2012)")
    cur.execute("INSERT INTO MOVIES VALUES('Avengers:EndGame','Robert Downey Jr','Scarlett Johansson','Anthony Russo and Joe Russo',2019)")
    cur.execute("INSERT INTO MOVIES VALUES ('The Matrix','Keanu Reeves','Carrie-Anne Moss',1999,'Lana Wachowski')")
    print("Data Inserted Successfully !!!")

    #Quering data from the Movies table.
    cur.execute("SELECT * FROM MOVIES")
    print(cur.fetchall())
    print("----------------------------------------")
    cur.execute("SELECT * FROM MOVIES WHERE DIRECTOR_NAME = 'Christopher Nolan'")
    print(cur.fetchall())
    print("Displayed the queries successfully !!!")
    
    connector.commit()
    

except Exception as err:
    print("ERROR OCCURED AT:",str(err))
