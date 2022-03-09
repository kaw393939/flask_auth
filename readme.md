# Project Setup

[![Production Workflow](https://github.com/kaw393939/docker_flask/actions/workflows/prod.yml/badge.svg)](https://github.com/kaw393939/docker_flask/actions/workflows/prod.yml)

* [Production Deployment](https://kwilliam-prod.herokuapp.com/)


[![Development Workflow](https://github.com/kaw393939/docker_flask/actions/workflows/dev.yml/badge.svg)](https://github.com/kaw393939/docker_flask/actions/workflows/dev.yml)

* [Developmental Deployment](https://kwilliam-dev.herokuapp.com/)

## Setting up CI/CD

The result of this will be that when you create a pull request to merge a branch to master, it will deploy to your
heroku development app/dyno and when you merge or push to master on github, it will deploy the app to the production heroku
app/dyno.
### Instructions

1. Clone this repo to your local (DO NOT FORK THIS REPO, IF YOU DO YOU HAVE TO ENABLE ACTIONS BEFORE ANYTHING RUNS)
2. Create a new repo on your own Github account
3. Change the origin by replacing it with your own new repo.  (Do not add a readme or any other file while creating the repository)
4. Create an account with Heroku, create an app for production and an app for development
5. Create a new repo in Docker hub

#### Setup Docker and Heroku Credentials In the Repository Settings under Action -> Secret

6. In your newly created Github repository, add new repository secrets for DOCKER_USERNAME, DOCKER_PASSWORD, HEROKU_API_KEY (Values are DOCKER_USERNAME: your docker hub username; DOCKER_PASSWORD: your docker hub password; HEROKU_API_KEY: API key from the heroku app)
### GitHub Notes:  Set the action secrets repository in: -> settings -> actions -> secrets
### Heroku Notes: Get the heroku API key from account in: -> applications -> create authorization button

#### Change GitHub Actions Workflows for Dev and Prod

6. Change line 42 to have your docker repo address in: .github/workflows/prod.yml
7. change lines 58 to have your heroku app name in: .github/workflows/prod.yml
8. change line 59 to have your heroku email in: .github/workflows/prod.yml
9. change line 31 to have your heroku app name in .github/workflows/dev.yml
10. change line 32 to have your heroku email in .github/workflows/dev.yml
11. Push code to your local repo and check for any errors and fix any errors that appear when the workflow is running. You can check the workflow in the
    actions.

## Running Locally

1. To Build with docker compose:
   docker compose up --build
2. To run tests, Lint, and Coverage report use this command: pytest --pylint --cov

.pylintrc is the config for pylint, .coveragerc is the config for coverage and setup.py is a config file for pytest


### Future Notes and Resources
* https://flask-user.readthedocs.io/en/latest/basic_app.html
* https://hackersandslackers.com/flask-application-factory/
* https://suryasankar.medium.com/a-basic-app-factory-pattern-for-production-ready-websites-using-flask-and-sqlalchemy-dbb891cdf69f
