# REST API with FAST API & PostgreSQL+PgAdmin(Dockerized)

## Pre-requisite:
- Docker

# How to Run

## Docker Compose
1. Open terminal in the project directory.
2. Type `docker-compose build` and wait for it to complete
3. Type `docker-compose up` and wait for it.
4. Now you can use the app on `127.0.0.1:8000/docs` or `127.0.0.1:8000/redoc`
5. Similarly, you can see the admin dashboard on `http://localhost:5050/`

All the credentials for DB are in `.env` file, you can edit it as well but do it wisely.
NOTE: "Never Upload `.env` or `.env.local` on Github or public repos. I uploaded it so that you can learn. 

## Database Migrations
You can migrate database as well after running the container using the above steps, steps for migrations are:
1. Type `docker-compose run app alembic revision --autogenerate -m "YOUR_MESSAGE_HERE"`
2. Then simply use the command `docker-compose run app alembic upgrade head` to save the changes.

## Run Without Docker
Without docker, setting up PostgreSQL, PgAdmin, MongoDB, Mongo-Express or any other Database is a tedious task, that is why Docker is here for rescue.
You can setup PostgreSQL and Pg-Admin yourself using any good resources from Youtube. After that, you have to make changes in the `.env` for `DATABASE_URL` value.
After all that, you can follow the steps below:
1. Create Virtual Environment using `python -m venv YOUR_ENV_NAME` in your project directory
2. Activate the environment using `YOUR_ENV_NAME\Scripts\activate` (Window Users)
3. Then type the command `pip install -r requirements.txt`
4. After that is done, you can run the app using `uvicorn main:app --host 0.0.0.0 --port 8000`

