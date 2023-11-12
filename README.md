# Solution for Moberries Sample Task

## Tech stack
    Python: 3.9
    Django: 4.2
    DRF: 3.14
    Flake8: 6.1
    Pytest: 7.4
    Postgres: 13
    Docker, docker-compose

## How to run
**Make sure you have docker/docker-compose installed and running**

- Clone the project: `git@github.com:Ibrokhimjon0823/cybervize.git`
- Change directory: `cd cybervize`
- Build docker image: `docker-compose build`
- Run docker container: `docker-compose up -d`
  application runs on: `127.0.0.1`
  
## Endpoints:
  - Drug-Diseases-Search: `127.0.0.1/api/drug-disease-search/`
  - Drug-Search: `127.0.0.1/api/drugs//`
  - Diseases-Search: `127.0.0.1/api/diseases/`
  
## Test 
- Run tests: `docker-compose exec app python manage.py test`
- Run flake: `docker-compose exec app flake8`
