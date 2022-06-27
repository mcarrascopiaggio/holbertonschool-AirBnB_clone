#!/usr/bin/python3
"""
Module for creating a base class: BaseModel
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """class base"""
    def __init__(self):
        """
        Initialize an instance of BaseModel
        id: string - assign with an uuid when an instance is created:
        you can use uuid.uuid4() to generate unique id.
        created_at: datetime - assign with the current datetime when an
        instance is created
        updated_at: datetime - assign with the current datetime when an
        instance is created and it will be updated every time you change
        your object
        """
        self.id = str(uuid4())  # convert the id to string
        self.created_at = datetime.now()  # Use method now() of datetime module
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[<{self.__class__.__name__}>] (<{self.id}>) <{self.__dict__}>"

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        instance.
        __dict__ is a pecial attribute of every module, is the dictionary
        containing the module’s symbol table.
        - Usamos la funcion "getattr", a la misma se le pasa la instancia
        correspondiente (con self) y el attribute del cual se quiere
        obtener el valor.
        """
        new_dict = {}

        for attribute in self.__dict__:
            if attribute == "created_at" or attribute == "updated_at":
                new_dict[attribute] = getattr(self, attribute).isoformat()
            else:
                new_dict[attribute] = getattr(self, attribute)
        new_dict['__class__'] = self.__class__.__name__
        # Se agrega la key: "__class__" y se le asigna el nombre de la clase.
        return (new_dict)
