from py_utils.core import bootstrap_config


def test_bootstrap_config():
    d = bootstrap_config(".secret/config.json")
    assert len(d) > 0
