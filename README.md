# Solution for Cybervize Sample Task

## Tech stack
    Python: 3.9
    Django: 4.2
    DRF: 3.14
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

## Example Query
    http://127.0.0.1:8000/api/drug-disease-search/?query=Fludara
