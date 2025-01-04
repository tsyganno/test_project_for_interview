# Пример информации из БД
USERS_DATA = [{"username": "admin", "password": "adminpass"}, {"username": "user", "password": "userpass"}]

# в реальной БД мы храним только ХЭШИ паролей (можете прочитать про библиотеку, к примеру, 'passlib') + соль (известная только нам добавка к паролю)
