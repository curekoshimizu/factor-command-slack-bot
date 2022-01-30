FROM public.ecr.aws/lambda/python:3.8

RUN pip install -U pip \
        && pip install slack-bolt python-lambda

COPY handler.py ./

CMD [ "handler.handler" ]
