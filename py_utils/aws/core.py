import dataclasses
from dataclasses import dataclass

from boto3 import client, Session


@dataclass
class AwsConfig:
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_session_token: str
    region_name: str


class AwsCore:
    def __init__(self, config: AwsConfig, service_name: str):
        self.aws_session = Session(
            config.aws_access_key_id,
            config.aws_secret_access_key,
            config.aws_session_token,
            config.region_name,
        )
        self.client = self.aws_session.client(service_name)
