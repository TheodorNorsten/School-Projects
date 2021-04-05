"file holding exeptions"


class Error(Exception):
    """ User defined class for custom exceptions"""


class SearchMiss(Error):
    """ Rasied when word dont exist in trie """
