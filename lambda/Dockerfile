FROM public.ecr.aws/lambda/python:3.8

RUN pip install slack-bolt sympy

COPY handler.py ./

CMD [ "handler.handler" ]
