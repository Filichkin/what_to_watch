# What to watch - веб-сервис для публикаций мнений о фильмах

<img src="app.png" width="800" height: auto>


## Стек технологий

![Flask](https://img.shields.io/badge/Flask-092E20)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-CC3300)
![Jinja2](https://img.shields.io/badge/Jinja2-%23DCDCDC
)

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd what_to_watch
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```
или для пользователей Windows

```
source env/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создание миграций:

```
flask db init

flask db migrate -m "some description"

flask db upgrade


```

Запустить проект:

```
flask run
```