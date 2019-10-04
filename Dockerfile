FROM python:3

WORKDIR /opt/firestore

COPY uploadFirestore.py .

RUN pip install --upgrade firebase-admin

ENTRYPOINT [ "python", "/opt/firestore/uploadFirestore.py" ]
