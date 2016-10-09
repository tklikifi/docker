import datetime
import redis
import sys
import time


def debug(message):
    sys.stdout.write("{}: {}\n".format(
        datetime.datetime.now().isoformat(), message))
    sys.stdout.flush()


def main():
    debug("Subscribing to 'logger'...")

    client = redis.StrictRedis(host='redis', port=6379)
    channel = client.pubsub()
    channel.subscribe("logger")

    debug("Polling the message queue...")
    while True:
        message = channel.get_message()
        if not message:
            time.sleep(1)
            continue
        debug("Type: {type}, Data: {data}".format(**message))


if __name__ == "__main__":
    main()
