"""
Hier maken we custom exceptions, is vooral leuk voor het oog en om scripts overzichtelijk te houden
"""

class MissingISSPositionError(Exception):
    pass

class MissingSunDataError(Exception):
    pass

class InvalidEmailException(Exception):
    pass