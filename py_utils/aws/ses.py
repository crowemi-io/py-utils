from dataclasses import dataclass, field

from py_utils.aws.core import AwsCore, AwsConfig, AwsTags


@dataclass
class Destination:
    to_address: list[str] = field(metadata={"key": "ToAddresses"})
    cc_address: list[str] | None = field(default=None, metadata={"key": "ToAddresses"})
    bcc_address: list[str] | None = field(default=None, metadata={"key": "ToAddresses"})


@dataclass
class Contents:
    data: str | None = None
    charset: str | None = None


@dataclass
class Body:
    text: Contents | None = None
    html: Contents | None = None


@dataclass
class Message:
    subject: Contents
    body: Body


@dataclass
class SesConfig:
    # required
    source: str
    # required
    destination: Destination
    # required
    message: Message
    reply_to_address: list[str] | None = None
    return_path: str | None = None
    source_arn: str | None = None
    return_path_arn: str | None = None
    tags: list[AwsTags] | None = None
    configuration_set_name: str | None = None


class Ses(AwsCore):
    def __init__(self, config: AwsConfig):
        super().__init__(config, "ses")

    def build_email(self, email: SesConfig) -> dict:
        # build destination
        destination = dict()
        for destination_type in email.destination.__dataclass_fields__.items():
            v = email.destination.__getattribute__(destination_type[0])
            if v:
                t = type(email.destination)
                k = t.__dataclass_fields__[destination_type[0]].metadata.get("key")
                destination[k] = v
        return destination


    def send_email(self, email: SesConfig):
        
        config = {
            "Source": email.source,
            "Destination": self.build_email(email),
            "Message": {
                "Subject": {
                    "Data": email.message.subject.data,
                    "Charset": email.message.subject.charset,
                },
                "Body": {
                    "Html": {
                        "Data": email.message.body.html.data,
                        "Charset": email.message.body.html.charset,
                    },
                },
            }
        }
        ret = self.client.send_email(**config)
        print(ret)