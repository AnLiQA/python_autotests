import requests

token = 'd8c83e07d524068134d57a233cd24938'
host = 'https://api.pokemonbattle.me:9104'

# Выполняем POST-запрос
response = requests.post(
    f'{host}/pokemons',
    json={
        "name": "Name1",
        "photo": "https://dolnikov.ru/pokemons/albums/642.png"
    },
    headers={'trainer_token': token, 'Content-Type': 'application/json'}
)
# Выводим результат POST-запроса
print(response.text)

try:
    # Преобразуем JSON-строку ответа в объект Python
    json_data = response.json()

    # Извлекаем значение 'id' из JSON-ответа
    id_newPok = json_data.get('id')

    
except ValueError as e:
    print(f"Ошибка декодирования JSON: {e}")

# Выполняем PUT-запрос с использованием id_newPok в теле запроса
response_put = requests.put(
    f'{host}/pokemons',
    json={
        "pokemon_id": id_newPok,
        "name": "Name2",
        "photo": "https://dolnikov.ru/pokemons/albums/642.png"
    },
    headers={'trainer_token': token, 'Content-Type': 'application/json'}
)

# Выводим результат PUT-запроса
print(response_put.text)

# Выполняем POST-запрос с использованием id_newPok в теле запроса
response_post = requests.post(
    f'{host}/trainers/add_pokeball',
    json={
        "pokemon_id": id_newPok,
    },
    headers={'trainer_token': token, 'Content-Type': 'application/json'}
)

# Выводим результат POST-запроса
print(response_post.text)