import os
import datetime

def folder():
    today = datetime.date.today()
    fish = 0

    try:
        os.mkdir(str(today))
        # print("folder Created")

    except FileExistsError:
        fish=1

folder()
