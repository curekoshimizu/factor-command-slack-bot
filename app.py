import os
from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw
)

class HelloMessageStack(core.Stack):

    def __init__(self, scope: core.App, name: str, **kwargs) -> None:
        super().__init__(scope, name, **kwargs)

        lambda_func = _lambda.Function(
            self, "HelloMessageFunc",
            code=_lambda.Code.from_asset("lambda"),
            handler="handler.handler",
            runtime=_lambda.Runtime.PYTHON_3_8,
        )
        apigw.LambdaRestApi(scope=self, id="HelloMessageApi", handler=lambda_func)

        # api = apigw.RestApi(self, "HelloMessageApi")
        # api.root.add_method("GET", apigw.LambdaIntegration(lambda_func))

app = core.App()

HelloMessageStack(
    app, "HelloMessageStack",
    env={
        "region": os.environ["CDK_DEFAULT_REGION"],
        "account": os.environ["CDK_DEFAULT_ACCOUNT"]
    }
)
app.synth()
