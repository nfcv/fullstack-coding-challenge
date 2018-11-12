# Translatewise 

## Setup

Create an .env file with this example keys:
```python
export UNBABEL_API_KEY="..."
export UNBABEL_API_USERNAME="..."
export APP_CONFIG="config.DevelopmentConfig"
export DATABASE_URL="postgresql://127.0.0.1/translatewise"
```

## Run it locally

```shel
$ pip install -r requirements.txt
$ python manage.py runserver
```

## Watch rq-redis
```shell
$ rq worker translatewise
```

## Requirements

__Python Version:__ 3.7.0
