from typing import Union


def filter_dict(keys: list[str], dict_object: dict) -> dict[any, any]:
    """Take a list of keys, and a dictionary, then return only the fields in the dictionary where key
        is specified in the keys list.
        Args:
            keys - List of keys
            dict_object - dictionary that'll be looked up
    """
    filtered = {}
    for key, value in dict_object.items():
        if key in keys:
            filtered[key] = value
    return filtered


def extract_keys(keys: list[str], data: Union[dict, list[dict]]) -> Union[dict, list[dict]]:
    """Take a list of keys, and either a dictionary or a list of dictionaries, then extract the
        fields in the dictionary that matches the keys. The lookup is shallow and doesn't go past the first level.
       Args:
            keys - list of keys to lookup
            data - object containing either a dictionary or list of dictionaries, the content is going to be looked up
    """
    if isinstance(data, list):
        filtered = []
        for item in data:
            filtered.append(filter_dict(keys, item))
        return filtered
    else:
        return filter_dict(keys, data)


def transform_orders(establishments: list[dict]):
    filtered_order = []
    for establishment in establishments:
        f_dict = {
            "establishment_id": establishment["id"],
            "timezone": establishment.get("time_zone"),
            "name": establishment.get("name"),
        }
        filtered_order.append(f_dict)

    return filtered_order
