"""Small list helpers used by report and scan code."""

class ListUtils:
    @staticmethod
    def unique(items):
        return list(dict.fromkeys(items))
