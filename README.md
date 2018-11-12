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

## Notes
- This project uses heavily type hinting instead of "kwargs" approach. I think it provides a lot of value, not only helps the IDE, it also helps the team working on the code, since it knows exactly what arguments a function or an object needs and what it returns.
- The front-end is very simplistic and probably wouldn't scale very well. Because I lost too much time with the back-end, I didn't spend to much time on front-end tooling.
