"""Return report dictionaries with stable field ordering."""

class FieldOrder:
    @staticmethod
    def apply(data: dict, fields: list[str]) -> dict:
        result = {}
        for field in fields:
            if field in data:
                result[field] = data[field]
        for key, value in data.items():
            if key not in result:
                result[key] = value
        return result
