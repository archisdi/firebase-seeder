from firebase_admin import initialize_app, credentials, db
from dotenv import load_dotenv
from os import getenv, listdir
from json import loads as loadJson

load_dotenv()

SEED_DATA_FOLDER_PATH = './seeds/'

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
    for file in listdir(SEED_DATA_FOLDER_PATH):
        collection = file.split('.')[0]
        print("- seeding " + collection + " data")

        seed_data = openJSON(SEED_DATA_FOLDER_PATH + file)
        db.reference(collection, app).set(seed_data)


if __name__ == '__main__':
    main()
