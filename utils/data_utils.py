def flatten_yaml(nested_dict, parent_key='', separator='.'):
    flat_dict = {}
    for key, value in nested_dict.items():
        full_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            flat_dict.update(flatten_yaml(value, full_key, separator))
        else:
            flat_dict[full_key] = value
    return flat_dict
