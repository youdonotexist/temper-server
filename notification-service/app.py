from apscheduler.schedulers.blocking import BlockingScheduler

import requests

def tempCheck():

    # TODO Update internal IP to reference global (or learn how to enable hairpin NAT on router)
    temperApiUrl = "http://192.168.0.11:5022/latest"

    response = requests.get(temperApiUrl)
    if response.status_code == 200:
        temp = response.json()[0]["temp"]
    else:
        temp = "A TERRIBLE ERROR"

    upperBound = 45.0
    isNumber = (type(temp) == int or float)

    if isNumber and temp >= upperBound:
        # TODO Inject key via en varbs
        alexaTrigger = "https://maker.ifttt.com/trigger/fridge_door_open/with/key/gxpFX4NxZiaBcLHPowQjNuOMYycauE5FiXnJ841cmca"
        dictToPost = {'value1': temp}
        response = requests.post(alexaTrigger, json=dictToPost)
        if response.status_code == 200:
            print("Success!")
    else:
        print("Temperatures are nominal")

if __name__ == "__main__":
    print("Initializing Temper Notification Service...")

    scheduler = BlockingScheduler()
    job = scheduler.add_job(tempCheck, 'interval', minutes=5)
    scheduler.start()   