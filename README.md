# Lancer le projet


## Start
```bash
git clone git@github.com:DeadPool92600/c.git
cd whodat
```

## Services
To start the database and rabbitmq services:
```bash
docker-compose up
```

## Backend

Start backend
```bash
cd back
pip install -r requirements.txt
python app.py
```

Start celery worker
```bash
cd back
 celery worker -A app.celery --loglevel=info
```

## Frontend
```bash
cd front
npm install
npm run serve
```


