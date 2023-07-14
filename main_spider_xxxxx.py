from receivers.redis_receiver import RedisReceiver

receiver = RedisReceiver()


def main():
    try:
        receiver.receive_spider()
    except (KeyboardInterrupt, SystemExit):
        return


if __name__ == '__main__':
    main()
