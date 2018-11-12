# Translatewise 

## Requirements

__Python Version:__ 3.7.0

## Setup

1. Create an .env file with this example keys:
```shell
export UNBABEL_API_KEY="..."
export UNBABEL_API_USERNAME="..."
export APP_CONFIG="config.DevelopmentConfig"
export DATABASE_URL="postgresql://127.0.0.1/translatewise"
```

2. Install redis
```shell
$ brew install redis
```

## Run it locally

```shel
$ redis-server
$ pip install -r requirements.txt
$ python manage.py runserver
```

## Running the Tests
```shel
$ python manage.py test
```

## Watch rq worker
```shell
$ rq worker translatewise
```
