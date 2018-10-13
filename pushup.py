import datetime
import json


def get_pushup_data():
    while True:
        user_input = input("Enter number of push-ups performed: ")
        try:
            pushup = int(user_input)
            if pushup > 0:
                break
            else:
                print(f"Only positive whole numbers are allowed, you entered {user_input}")
        except ValueError:
            print(f"Only positive whole numbers are allowed, you entered {user_input}")

    return pushup


filename = "pushup.json"
# check if file exists
try:
    with open("pushup.json", 'r') as fh:
        data = json.load(fh)
except FileNotFoundError:
    print("File could not be found")


num_pushups = get_pushup_data()
date_string = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M%S')
newdata = {'date': date_string, 'set1': num_pushups}

with open('pushup.json', 'w+') as fh:
    data.append(newdata)
    json.dump(data, fh, indent=4, separators=(',', ':'))
