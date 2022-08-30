def remove_input_prefixes(data: dict) -> dict:
    """Removes prefix 'input_' from dict keys"""
    return {key.replace("input_", ""): val for key, val in data.items()}
