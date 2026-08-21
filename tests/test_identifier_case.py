from core.identifier_case import IdentifierCase


def test_identifier_case():
    assert IdentifierCase.normalize("  Example.COM  ") == "example.com"
