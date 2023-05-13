#!/usr/bin/python3

import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets the given object in __objects with key <obj class name>.id
        """

        key = f"{obj.__cass__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects if the file exists.
        """
        try:
            with open(self.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    class_ = globals()[class_name]
                    self.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass
