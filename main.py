from firebase_admin import initialize_app, credentials, db
from dotenv import load_dotenv
from os import getenv
from json import loads as loadJson

load_dotenv()

def openJSON(path):
    with open(path, 'r') as outfile:
        data = outfile.read()

    return loadJson(data)

def initiateApp():
    account = openJSON(getenv('FIREBASE_ACCOUNT_URL'))
    return initialize_app(
        credential=credentials.Certificate(account),
        options={
            'databaseURL': getenv('FIREBASE_DB_URL')
        }
    )

def main():
    app = initiateApp()
    users = db.reference('retailer_app_user', app)
    print(users.get())


if __name__ == '__main__':
    main()
