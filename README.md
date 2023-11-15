# pillwatch

## running the api server 
make sure that your `config.py` has the following: 
- `ROBOFLOW_API_KEY_PRIVATE` Your Roboflow private key
- `ROBOFLOW_API_KEY_PUBLIC` Your Roboflow public key
- `POSTGRESQL_USERNAME` Your Azure PostgreSQL account username 
- `POSTGRESQL_PASSWORD` Your Azure PostgreSQL account password

in `backend/` 

```flask run``` 

## running the front end 
navigate to `frontend/pillwatch` 

```yarn dev```

## installation 
`pip install flask-cors`

in your virtual environment:
`pip install -r requirements.txt` 

after installing new packages 
`pip freeze > requirements.txt`
