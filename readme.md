# Project Setup

[![Production Workflow](https://github.com/vineethsudhir/cs601_proj1/actions/workflows/prod.yml/badge.svg)](https://github.com/vineethsudhir/cs601_proj1/blob/master/.github/workflows/dev.yml)

* [Production Deployment](https://vs56-prod.herokuapp.com/)


[![Development Workflow](https://github.com/vineethsudhir/cs601_proj1/actions/workflows/dev.yml/badge.svg)](https://github.com/vineethsudhir/cs601_proj1/blob/master/.github/workflows/prod.yml)

* [Developmental Deployment](https://vs56-dev.herokuapp.com/)

## CI/CD

The master branch gets deployed in the development. The other branches gets deployed on Production. Master won't allow to merge if any test case does't pass.

## Running Locally

1. To Build with docker compose:
   docker compose up --build
2. To run tests, Lint, and Coverage report use this command: pytest --pylint --cov


### Future Notes and Resources
* https://flask-user.readthedocs.io/en/latest/basic_app.html
* https://hackersandslackers.com/flask-application-factory/
* https://suryasankar.medium.com/a-basic-app-factory-pattern-for-production-ready-websites-using-flask-and-sqlalchemy-dbb891cdf69f
