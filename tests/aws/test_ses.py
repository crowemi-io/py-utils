from py_utils.core import bootstrap_config
from py_utils.aws.ses import *


def test_ses():
    config = bootstrap_config(".secret/config.json")
    client = Ses(AwsConfig(**config))
    email = SesConfig(
        source="no-reply@crowemi.com",
        destination=Destination(
            to_address=["crowemi@hotmail.com"]
        ),
        message=Message(
            subject=Contents(data="Test", charset="UTF-8"),
            body=Body(html=Contents(data="<h1>Test</h1>", charset="UTF-8"))
        ),
    )
    client.send_email(email)