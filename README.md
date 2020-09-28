# Flask + GraphQL Starter App

Starter project for Flask + Graphene + Postgres Python app.

---

## Run Application

The preferred way to run this application is by using Docker

### Docker

> `docker build -t flaskql-starter .`  
> `docker run -p 8080:8080 flaskql-starter`  

### Locally

You can now access GraphiQL in your browser by accessing: [localhost:8080](localhost:8080)

You can also run it locally, this method requires a few dependencies such as Python 3+, pip and pipenv. The following needs to be performed to get the application to run locally:

> `pipenv shell`  
> `pipenv update`  
> `python wsgi.py`  
