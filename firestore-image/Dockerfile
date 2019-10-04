FROM python:3

ADD uploadfirestore.py /

RUN pip install --upgrade firebase-admin

ENTRYPOINT [ "python", "./uploadFirestore.py" ]
