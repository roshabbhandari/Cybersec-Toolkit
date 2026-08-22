"""Merge report mappings with later values taking precedence."""

def merge_maps(*mappings):
    result = {}
    for mapping in mappings:
        result.update(mapping)
    return result
