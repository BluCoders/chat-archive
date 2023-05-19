import logging
from logging.handlers import SocketHandler


def create_logger(name, level=1):
    log_instance = logging.getLogger(name)
    log_instance.setLevel(level)
    socket_handler = SocketHandler('127.0.0.1', 19996)  # default listening address
    log_instance.addHandler(socket_handler)

    return log_instance


# Global root logger
root_log = create_logger("Chat Archive")
