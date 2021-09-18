# REST API with FAST API & PostgreSQL+PgAdmin(Dockerized)

## Pre-requisite:
- Docker

# How to Run

## With Docker
1. Open terminal in the project directory.
2. Type `docker-compose build` and wait for it to complete
3. Type `docker-compose up` and wait for it.
4. Now you can use the app on `127.0.0.1:8000/docs` or `127.0.0.1:8000/redoc`
5. Similarly, you can see the admin dashboard on `http://localhost:5050/`

All the credentials for DB are in `.env` file, you can edit it as well but do it wisely.
NOTE: "Never Upload `.env` or `.env.local` on Github or public repos. I uploaded it so that you can learn. 
