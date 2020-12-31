def get_value(json, keys):
    if not json:
        return None

    result = json
    for key_value in keys:
        try:
            result = result[key_value]
        except KeyError:
            return None
        if not result:
            return None
    return result


if __name__ == "__main__":
    print(get_value({"a": {"b": {"c": "1"}}}, ["a", "b", "c"]))  # 1
