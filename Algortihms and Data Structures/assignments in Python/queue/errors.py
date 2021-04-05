"file holding exeptions"


class Error(Exception):
    """ User defined class for custom exceptions"""


class EmptyQueueException(Error):
    """ Rasied in peek() and dequeue methods in file queue.py when queue is Empty """
