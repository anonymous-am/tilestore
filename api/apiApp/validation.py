import re

class Validation:
    # order_id validation................
    def is_idValid(value):
        id_regex = re.compile(r'^[a-zA-Z0-9_]{3,}$')
        if not id_regex.match(value):
            return False
        return True

    # name validation....................
    def is_nameValid(value):
        name_regex = re.compile(r'^[a-zA-Z ]{3,}$')
        if not name_regex.match(value):
            return False
        return True

    # contact validation.................... 
    def is_contactValid(value):
        contact_regex = re.compile(r'^[7-9]\d{9}$')
        if not contact_regex.match(value):
            return False
        return True

    # price validation....................
    def is_priceValid(value):
        price_regex = re.compile(r'^[1-9]\d*(\.\d+)?|0(\.\d+)?$')
        if not price_regex.match(value):
            return False
        return True

    # quantity validation....................
    def is_quantityValid(value):
        qty_regex = re.compile(r'^[1-9]\d*$')
        if not qty_regex.match(value):
            return False
        return True

    # size validation....................
    def is_sizeValid(value):
        size_regex = re.compile(r'^[6-9]\d{9}$')
        if not size_regex.match(value):
            return False
        return True