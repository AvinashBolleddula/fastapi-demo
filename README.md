# FastAPI
- super fast python web framework, others are django, flask etc.
- very nice feature of asynchronous programming, this lacks in django framework
- this makes your life easy by having lots of features
- First is Auomatic Documentations
# Automatic Docs
- fastapi provides swagger ui, we can check what routes or apis we created and we can also try them out
- if you dont like swagger ui, fast api provides ReDoc UI, this is same but very minimal design for the documentation
# uses moder python
- python 3.6 with type using pydantic
# Based on open standard
- json schema (returns json, which other apps need)
- open api (creating api standards)
# vscode editor support
- fastapi has aoutocomplete feature in vscode, similarly pycharm
- achieved using typing pydantic library of python
# security and authentication
- http basic
- OAuth2 (also with JW2 Tokens)
- API keys in header, query parameters, cookies etc.
# Dependency Injection
# Unlimited Plugins
# Testing (Pytest)
# Starlette features
- fastapi built over starlette, so it provides websocket support, graphql support, in process background tasks, startup and shutdown events, test client built on requests, CORS, Gzip, Static files, streaming responses, session and cookie support
# other supports
- sql databases
- nosql databases
- graphql

so fastapi is a package of full web framework.
-----

# Getting Started
- Install and Setup
- Break it down, how it structured
# Basic Concepts
- Path Parameters
- API Docs - swagger/redocs
- Query parameters
- Request Body
# Intermediate Concepts
- Debugging FastAPI
- Pydantic Schemas
- SqlAlchemy database connection
- Models and table
# Database Tasks
- Store blog to database
- Get blogs from database
- Delete
- Update
# Response
- Handling Exceptions
- Return Response
- Define response model (show only certain fields that we want)
# User and Password
- Create user
- Hash user password
- show single user
- Define docs tags
# Relationship
- Define user to blog relationship
- Define blog to user relationship
# Refactor for bigger application
- API Router
- API router with parameters
# Authentication using JWT (Json web token)
- Create login route
- Login and verify password
- Return JWT access token
- Routes behind authentication
# Deploy FastAPI
- Using Deta.sh website to deploy
