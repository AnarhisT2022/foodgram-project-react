# Foodgram

![Foodgramm workflow status](https://github.com/AnarhisT2022/foodgram-project-react/actions/workflows/main.yml/badge.svg)

### Сервис доступен по адресу: PS. В разработке!!!
```
https://insta-foodgram.ddns.net/
```
### Запуск проекта:
1. Клонируйте проект:
```
git clone https://github.com/AnarhisT2022/foodgram-project-react.git
```
2. Подготовьте сервер:
```
scp docker-compose.production.yml <username>@<host>:/home/<username>/
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
sudo docker compose -f docker-compose.production.yml up -d
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
```
5. Создайте суперюзера и соберите статику:
```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
```
6. Скопируйте предустановленные данные json:
```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py csvimport
```
### Суперпользователь:
```
email: admin@ya.ru
password: admin
```