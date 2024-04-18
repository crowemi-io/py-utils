from core import AwsCore, AwsConfig


class Ses(AwsCore):
    def __init__(self, config: AwsConfig):
        super().__init__(config, "ses")
