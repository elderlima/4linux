import sys
import logging
import logging.handlers

stdout_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("logs.txt")
sock_handler = logging.handlers.SocketHandler(
    "localhost", "10000"
)

handlers = [stdout_handler, file_handler, sock_handler]

fmt = logging.Formatter(
    "%(asctime)s:%(levelname)s:%(name)s:%(message)s",
    "%d/%m/%Y %H:%M:%S"
)

for handler in handlers:
    stdout_handler.setFormatter(fmt)
    stdout_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(fmt)
    file_handler.setLevel(logging.DEBUG)
    sock_handler.setFormatter(fmt)
    sock_handler.setLevel(logging.DEBUG)