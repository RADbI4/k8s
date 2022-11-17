import datetime as dt
import time


def main_first_docker_script():
    print(dt.datetime.now())


if __name__ == "__main__":
    while True:
        main_first_docker_script()
        time.sleep(10)
