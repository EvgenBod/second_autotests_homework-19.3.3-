import requests

status = 'avalibale'

res = requests.get(f'https://petfriends.skillfactory.ru/api/key',
                    headers=({'accept': 'application/json', 'email': 'fara@list.ru', 'password': 'fara1234'}))

res1 = requests.post(f'https://petfriends.skillfactory.ru/api/create_pet_simple',
                    headers=({'accept': 'application/json','auth_key': 'a3581f693589f60a3bcd1831484d486e05ee7c81d5d236be44530aed'}),
                    data=({'Content-Type': 'multipart/form-data', 'name': 'Ходорковский', 'animal_type': 'Псина', 'age': '9'}))

res2 = requests.get(f'https://petfriends.skillfactory.ru/api/pets?filter=my_pets',
                    headers=({'accept': 'application/json',
                             'auth_key': 'a3581f693589f60a3bcd1831484d486e05ee7c81d5d236be44530aed'}))

res3 = requests.delete(f'https://petfriends.skillfactory.ru/api/pets/729f5fdf-cf84-49c0-bf5d-82e07acbda49',
                      headers=({'accept': 'application/json',
                                'auth_key': 'a3581f693589f60a3bcd1831484d486e05ee7c81d5d236be44530aed'}))

res4 = requests.put(f'https://petfriends.skillfactory.ru/api/pets/00c2c6cd-a0a8-4f77-9b01-cff8abae8df5',
                      headers=({'accept': 'application/json',
                             'auth_key': 'a3581f693589f60a3bcd1831484d486e05ee7c81d5d236be44530aed'}),
                      data=({'Content-Type': 'multipart/form-data', 'name': 'Dublin', 'animal_type': 'mouse', 'age': '12'}))


print(res.text)
print(res.status_code)
print(res1.text)
print(res1.status_code)
print(res2.text)
print(res2.status_code)
print(res3.text)
print(res3.status_code)
print(res4.text)
print(res4.status_code)