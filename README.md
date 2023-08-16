# monitora-task

1. [Create](https://docs.python.org/3/library/venv.html) an empty venv and [activate](https://python.land/virtual-environments/virtualenv) it
2. install requirements 
```console
pip install -r requirements.txt
```
3.  run tests
```console
python manage.py test
```
4. run server (db with data is already provided, so no need for migrate command)
```console
python manage.py runserver
```
To download movie and actor data on an empty db
```console
python manage.py download_movies_and_actors
```

