import requests
import sys


def send_message(message, priority):
    url = "https://ntfy.sh/raf-py"
    requests.post(url, data=message.encode(encoding='utf-8'),
                  headers={"Priority": priority, "Tags": 'strawberry', "topic": "python test".upper()})


def main(message, priority):
    send_message(message, priority)
    return '(done)'


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
