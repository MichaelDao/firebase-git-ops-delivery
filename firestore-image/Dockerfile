FROM python:3

ADD uploadFirestore.py /

RUN pip install --upgrade firebase-admin

ENTRYPOINT [ "python", "./uploadFirestore.py" ]
