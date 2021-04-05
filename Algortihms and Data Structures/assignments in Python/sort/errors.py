"file holding exeptions"


class Error(Exception):
    """ User defined class for custom exceptions"""


class IndexErrorException(Error):
    """ Rasied when index doesnt exist in Node-list """


class KeyErrorException(Error):
    """ Raised """


class EmptyListException(Error):
    """ Rasied in peek() and dequeue methods in file queue.py when queue is Empty """
