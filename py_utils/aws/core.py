import dataclasses
from dataclasses import dataclass, field

from boto3 import client, Session


@dataclass
class AwsConfig:
    aws_access_key_id: str | None = None
    aws_secret_access_key: str | None = None
    aws_session_token: str | None = None
    region_name: str = "us-west-2"


@dataclass
class AwsTags:
    name: str = field(metadata={"json_key": "Name"})
    value: str = field(metadata={"json_key": "Value"})


class AwsCore:
    def __init__(self, config: AwsConfig, service_name: str):
        self.aws_session = Session(
            config.aws_access_key_id,
            config.aws_secret_access_key,
            config.aws_session_token,
            config.region_name,
        )
        self.client = self.aws_session.client(service_name)
