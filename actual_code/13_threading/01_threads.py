from time import sleep
import random
from threading import Thread
import datetime

current_state = {

}

def door_sensor(sensor_id, check_interval=2):
    for _ in range(5):
        sleep(check_interval)
        door_state = random.choice(["open", "closed"])
        current_state[sensor_id] = door_state
    print(f"[{sensor_id}] is deactivated")

def log_printer():
    while True:
        sleep(2)
        print("=" * 20)
        print(f"{datetime.datetime.now()}")
        for sensor, state in current_state.items():
            print(f"{sensor}: {state}")



# front_door = Thread(target=door_sensor, args = ("front", 2))
# back_door = Thread(target=door_sensor, args = ("back", 2))
# side_door = Thread(target=door_sensor, args = ("side", 2))
log_thread = Thread(target=log_printer, daemon=True)

threads = [Thread(target=door_sensor, args=(sensor, 2))
           for sensor in ["front", "back", "side", "attic"]
        ]
for thread in threads:
    thread.start()


print("Threads have been created.")


log_thread.start()

print("Threads have been started.")

for thread in threads:
    thread.join()


print("All done.")
