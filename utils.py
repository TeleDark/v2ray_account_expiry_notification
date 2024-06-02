
import json
import pickle
import requests
from time import sleep
from keys import *
import ast
from datetime import datetime


def send_message(msg):
    requests.post(
        f'https://api.telegram.org/bot{token_bot}/sendMessage?chat_id={chat_id}&text={msg}')


def read_json():
    os.system(f'python3 {login_file}')
    with open(json_file) as f:
        return json.load(f)

def save_to_pickle(data, filename):
    try:
        with open(filename, 'wb') as f:
            pickle.dump(data, f)
    except (IOError, pickle.PickleError) as e:
        print(f"Error saving data to pickle file: {e}")


def load_from_pickle(filename):
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        return data
    except (FileNotFoundError, EOFError, pickle.UnpicklingError) as e:
        #print(f"Error loading data from pickle file: {e}")
        return []


def check_disable(data, inactives_list):
    for conf in data:
        disable = False
        data_dict = ast.literal_eval(conf['settings'])
        timestamp_ms = data_dict['expiryTime']

        if timestamp_ms <= 0:
            continue

        timestamp_s = timestamp_ms / 1000
        expiry_date = datetime.fromtimestamp(timestamp_s)
        if expiry_date < datetime.now():
            disable = True

        email = data_dict['email']
        if disable and email not in inactives_list:
            send_message(f"یوزر {email} غیرفعال شد")
            inactives_list.append(email)
            save_to_pickle(inactives_list, inactives_file)


def check_enable(data, inactives_list):
    for conf in data:
        disable = False
        data_dict = ast.literal_eval(conf['settings'])
        timestamp_ms = data_dict['expiryTime']

        if timestamp_ms <= 0:
            if data_dict['email'] in inactives_list:
                inactives_list.remove(data_dict['email'])
                save_to_pickle(inactives_list, inactives_file)
                continue
        
        timestamp_s = timestamp_ms / 1000
        expiry_date = datetime.fromtimestamp(timestamp_s)
        if expiry_date < datetime.now():
            disable = True
        
        if not disable and data_dict['email'] in inactives_list:
            inactives_list.remove(data_dict['email'])
            save_to_pickle(inactives_list, inactives_file)


def main():
    while True:
        data = read_json()
        if not data:
            sleep(10)
            continue

        inactives_list = load_from_pickle(inactives_file)
        check_disable(data, inactives_list)
        check_enable(data, inactives_list)
        sleep(300)


if __name__ == "__main__":
    main()
