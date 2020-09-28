class ResourceExistsException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class ResourceNotFoundException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class InvalidHttpHeaderException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class TokenNotFoundException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class InvalidTokenException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class EnvironmentVariableNotFoundException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class DatabaseTransactionException(Exception):
    def __init__(self, *args, **kwargs):
        if kwargs and kwargs.get("args"):
            self.message = "There was an error saving the data to the database: {}".format(
                kwargs.get("args")
            )
            if kwargs.get("message"):
                self.message += " - {}".format(kwargs.get("message"))
        else:
            self.message = "There was an error saving the data to the database."

    def __str__(self):
        return f"{self.message}"
