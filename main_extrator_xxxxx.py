from receivers.redis_receiver import RedisReceiver

receiver = RedisReceiver()


def main():
    try:
        receiver.receive_extrator()
    except (KeyboardInterrupt, SystemExit):
        return


if __name__ == '__main__':
    main()
