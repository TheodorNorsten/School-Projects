""" Person class """
import random

class Person:
    "Initiation of Person class."
    def __init__(self, name, id_nr=None):
        "init method for class Initiation"
        self.name = name #str
        self._id = id_nr if id_nr else self.set_id() #sets random id


    def set_id(self):
        "instance method, sets the attribute id to a random string of length 3."
        list_name = list(self.name)
        random.shuffle(list_name)
        id_random = ''.join(list_name)

        if len(id_random) >= 3:
            return id_random[:3]
        return id_random



    @property
    def id_(self):
        "get instance method of id attribute."
        return self._id


    def __str__(self):
        "str instance method, prints the person object."
        return "Person: {p} id: {i}".format(p=self.name, i=self._id)


    def to_json(self):
        "converts object to dictionary format"
        return {
            "name": self.name,
            "id": self._id
        }


    @classmethod
    def create_person(cls, data_json):
        "class method, creates person object."
        return cls(data_json["name"], data_json["id"])





if __name__ == '__main__':
    pass
