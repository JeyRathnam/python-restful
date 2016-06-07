class JsonSerializer:
    __attributes__ = None
    __attribute_serializer__ = None
    serializers = None

    def serialize(self):
        """ taken from : http://www.prschmid.com/2012/12/json-serializing-sqlalchemy-objects.html
        Serialize an object to a dictionary.

        Take all of the attributes defined in self.__attributes__ and create
        a dictionary containing those values.

        Args:
            obj: The object to serialize
        Returns:
            A dictionary containing all of the serialized data from the object.
        """
        d = dict()
        for attr in self.__attributes__:
            val = getattr(self, attr)
            if val is None:
                continue
            serializer = self.__attribute_serializer__.get(attr)
            if serializer:
                d[attr] = self.serializers[serializer]['serialize'](val)
            else:
                d[attr] = val
        return d

    def deserialize(self, json, **kwargs):
        """Deserialize a JSON dictionary and return a populated object.

        This takes the JSON data, and deserializes it appropriately and then calls
        the constructor of the object to be created with all of the attributes.

        Args:
            json: The JSON dict with all of the data
            **kwargs: Optional values that can be used as defaults if they are not
                present in the JSON data
        Returns:
            The deserialized object.
        Raises:
            ValueError: If any of the required attributes are not present
        """
        d = dict()
        for attr in self.__attributes__:
            if attr in json:
                val = json[attr]
            elif attr in self.__required__:
                try:
                    val = kwargs[attr]
                except KeyError:
                    raise ValueError("{} must be set".format(attr))

            serializer = self.__attribute_serializer__.get(attr)
            if serializer:
                d[attr] = self.serializers[serializer]['deserialize'](val)
            else:
                d[attr] = val

        return self.__object_class__(**d)
