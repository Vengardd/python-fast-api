# Project for algorithms and data structures in python

## Implementation of djikstra algorithm

### Used technologies:

- Python 3.10
- FastAPI
- SQLAlchemy
- Swagger

### Starting project:

1. Clone project: `git clone {url}`
2. Install of necessery depedencies with `pip`
3. Install `uvicorn` to start server
4. Create `mysql` database, prefered with docker.
    - I used docker for it with
      command: `docker run --name=user --env="MYSQL_ROOT_PASSWORD=password" -p 3306:3306 -d mysql:latest`
5. In `mysql` database, create database with name `fastapi`
    - If you're using docker with previous command, you have to:
        - Find your container ID with command `docker container ls`
        - Go inside this container with command `docker exec -it {twoFirstLettersOfContainerId} bin/bash`
        - Login to mysql as root with command `mysql -u root -p` (password should be same as this that you used creating
          container, in this case `password`)
        - Create database with command `create database fastapi`
6. Inside of your folder with project use command `uvicorn main:app --reload` to start server
7. Go to site `localhost:8000/docs` to get swagger documentation or `localhost:8000` to get welcome message.

Proper logs should looks like this on app starting:

```
INFO:     Will watch for changes in these directories: ['.....']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)    
INFO:     Started reloader process [17480] using statreload
WARNING:  The --reload flag should not be used in production on Windows.
INFO:     Started server process [11700]
INFO:     Waiting for application startup.
INFO:     Application startup complete.  
```

### Description of files:

- `api.py` - creating endpoints
- `crud.py` - 'logic' of endpoints
- `database.py` - configuration of connection with database
- `exceptions.py` - custom exceptions used in `crud.py`
- `main.py` - main place of starting application
- `models.py` - database models
- `models.py` - DTOs(Data Transfer Objects)

### Quick documentation of endpoints:

##### Create connection between cities

HTTP POST
`{api}/api/addConnection` \
Request body:

```
{
  "from_city_name": "firstCityName",
  "to_city_name": "secondCityName",
  "distance": distanceAsNumber
}
```

Should respond with 200 and created object of connection

##### Find connection between cities

HTTP POST
`{api}/api/findConnection` \
Request body:

```
{
  "from_city": "fromCityName",
  "to_city": "toCityName"
}
```

Should respond with 200 and whole distance in km if found connection between cities, or 404 if there is no connection
between this two cities

### Bibliography

- `https://stackabuse.com/dijkstras-algorithm-in-python/` - Helper with djikstra algorithm
- `https://blog.balasundar.com/getting-started-with-fastapi` - Whole application was created based on repository from
  this article
- `https://fastapi.tiangolo.com/` - Official documentation of FastAPI