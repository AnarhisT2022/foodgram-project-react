# Foodgram

![Foodgramm workflow status](https://github.com/AnarhisT2022/foodgram-project-react/actions/workflows/main.yml/badge.svg)

### Сервис доступен по адресу: PS. В разработке!!!
```
https://insta-foodgram.ddns.net/
```
### Запуск проекта:
1. Клонируйте проект:
```
git clone https://github.com/ruzhova/foodgram-project-react.git
```
2. Подготовьте сервер:
```
scp docker-compose.yml <username>@<host>:/home/<username>/
scp nginx.conf <username>@<host>:/home/<username>/
scp .env <username>@<host>:/home/<username>/
```
3. Установите docker и docker-compose:
```
sudo apt install docker.io 
sudo apt install docker-compose
```
4. Соберите контейнер и выполните миграции:
```
sudo docker-compose up -d --build
sudo docker-compose exec backend python manage.py migrate
```
5. Создайте суперюзера и соберите статику:
```
sudo docker-compose exec backend python manage.py createsuperuser
sudo docker-compose exec backend python manage.py collectstatic --no-input
```
6. Скопируйте предустановленные данные json:
```
sudo docker-compose exec backend python manage.py loadmodels --path 'recipes/data/ingredients.json'
sudo docker-compose exec backend python manage.py loadmodels --path 'recipes/data/tags.json'
```
### Суперпользователь:
```
email: admin@ya.ru
password: admin
```
