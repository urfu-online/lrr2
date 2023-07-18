docker-compose up # запуск в консоли
docker-compose up -d # запуск как службы 
docker-compose stop
docker-compose up -d --build # запуск в фоне с ребилдом
docker system prune #почистить систему от неиспользуемых данных докером

docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser