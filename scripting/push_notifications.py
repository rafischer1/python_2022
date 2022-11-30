import requests
import sys


def send_message(message):
    url = "https://ntfy.sh/world_cup"
    priority = "4"
    requests.post(url, data=message.encode(encoding='utf-8'),
                  headers={"Priority": priority, "Tags": 'skull', "topic": "python test".upper()})


def main(message):
    send_message(message)
    return '(done)'


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
