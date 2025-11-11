import json
import os

FIlE_NAME = 'db.json'

if not os.path.exists(FIlE_NAME):
    with open(FIlE_NAME, 'w') as f:
        json.dump(
            {
                'users': {},
                'orders': {}
            }, f, indent=4
        )
else:
    try:
        with open(FIlE_NAME) as f:
            json.load(f)
    except:
        with open(FIlE_NAME, 'w') as f:
            json.dump(
                {
                    'users': {},
                    'orders': {}
                }, f, indent=4
            )


def is_user(tg_id: int) -> bool:
    with open(FIlE_NAME) as f:
        users = json.load(f)['users']

    return str(tg_id) in users

def add_user(tg_id, user_data):
    with open(FIlE_NAME) as f:
        users = json.load(f)

    users['users'][str(tg_id)] = user_data

    with open(FIlE_NAME, 'w') as f:
        json.dump(users, f, indent=4)
        