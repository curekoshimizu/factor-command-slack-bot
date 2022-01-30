import os
from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw
)
from aws_cdk.aws_lambda import DockerImageFunction, DockerImageCode
from dotenv import load_dotenv

load_dotenv()

class PrimeFactorizationMessageStack(core.Stack):
    def __init__(self, scope: core.App, name: str, **kwargs) -> None:
        super().__init__(scope, name, **kwargs)

        backend = DockerImageFunction(
            scope=self, id='PrimeFactorizationMessageDocker', code=DockerImageCode.from_image_asset(
                directory='lambda',
            ), 
            memory_size=128,  # default 128MB
            timeout=core.Duration.seconds(3), # default 3 sec
            environment= {
                "SLACK_BOT_TOKEN": os.environ["SLACK_BOT_TOKEN"],
                "SLACK_SIGNING_SECRET": os.environ["SLACK_SIGNING_SECRET"],
            })


        # backend = _lambda.Function(
        #     self, "PrimeFactorizationMessageFunc",
        #     code=_lambda.Code.from_asset("lambda"),
        #     handler="handler.handler",
        #     runtime=_lambda.Runtime.PYTHON_3_8,
        #     environment= {
        #         "SLACK_BOT_TOKEN": os.environ["SLACK_BOT_TOKEN"],
        #         "SLACK_SIGNING_SECRET": os.environ["SLACK_SIGNING_SECRET"],
        #     },
        # )
        apigw.LambdaRestApi(scope=self, id="PrimeFactorizationMessageApi", handler=backend)

app = core.App()

PrimeFactorizationMessageStack(
    app, "PrimeFactorizationMessageStack",
    env={
        "region": os.environ["CDK_DEFAULT_REGION"],
        "account": os.environ["CDK_DEFAULT_ACCOUNT"]
    }
)
app.synth()
