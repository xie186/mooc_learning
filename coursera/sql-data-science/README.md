# Databases and SQL for Data Science with Python

## Week1

### Select statement

```
select * from Book;
select book_id, title from Book;
select book_id, title from Book WHERE book_id = 'B1';
```

```
SELECT * FROM FilmLocations;
SELECT Title, Director, Writer FROM FilmLocations;
SELECT Title, Director, Writer FROM FilmLocations WHERE Director = "Jayendra";
SELECT Title, ReleaseYear, Locations FROM FilmLocations WHERE ReleaseYear>=2001;
```

### COUNT, DISTINCT, LIMIT

```
select COUNT(*) from tablename
select DISTINCT COUTRY from MEDALS where MEDALTYPE ="Gold"
slect * from tablename LIMIT 10
```

### Insert 
