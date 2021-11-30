# Whodat Project


## Start
```bash
git clone git@github.com:DeadPool92600/c.git
cd whodat
```

### Start using `Tilt`

First, follow instructions [here](https://docs.tilt.dev/install.html) to install Tilt.
Then run as follow:
```bash
tilt up
```

### Start using `docker-compose`
To start the database and rabbitmq services:
```bash
docker-compose up
```

#### Backend

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

#### Frontend
```bash
cd front
npm install
npm run serve
```


