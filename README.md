# Stocks Tracking API
* In this repository I'm going to build an REST API with django to track a users stock transaction history, to give a full overview of stocks management.

# curl requests:
* **GET on endpoint with Token**: `curl -X GET "http://127.0.0.1:8000/api/" -H "Authorization: Token <token>"`
* **Auth with POST**: `curl -X POST "http://127.0.0.1:8000/api/rest-auth/login/" -H "Content-Type: application/json" -d '{"username": "<usr>", "email": "<email>", "password": "<pwd>"}'`
