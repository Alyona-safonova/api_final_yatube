## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке: :shipit:
```
git clone https://github.com/Alyona-safonova/api_final_yatube.git
```
```
cd yatube_api
```
Cоздать и активировать виртуальное окружение: :snake:

```
python3 -m venv venv
```
- Если у вас Linux/macOS

```
source venv/bin/activate
```
- Если у вас windows

```
source venv/scripts/activate
```
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Выполнить миграции:

```
python manage.py migrate
```
Запустить проект:

```
python manage.py runserver
```
![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)
