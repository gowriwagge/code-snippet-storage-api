# Code Snippet Storage API

## Overview

A RESTful API to store, update, delete, and version code snippets per user.

## Tech Stack

- Python 3.x
- Flask
- SQLAlchemy
- SQLite

## API Endpoints

### Create/Update Snippet

`POST /users/<user_id>/snippets`

### Get Snippet

`GET /users/<user_id>/snippets/<snippet_name>`

### List Snippets

`GET /users/<user_id>/snippets`

### Delete Snippet

`DELETE /users/<user_id>/snippets/<snippet_name>`

## How to Run

```bash
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
