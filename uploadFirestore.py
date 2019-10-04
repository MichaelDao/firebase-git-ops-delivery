import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import argparse


def authenticateFirestore(PROJECT_ID):
    # Find and apply application default credentials
    cred = credentials.ApplicationDefault()

    # Initialize firebase admin with the credentials
    firebase_admin.initialize_app(cred, {
        'projectId': PROJECT_ID,
    })

    # initialize the firestore client
    db = firestore.client()

    # add test documents
    addDocument(db)
    addDocumentExtra(db)

    # read back from firestore (debug)
    readFirestore(db)


def addDocument(db):
    # Add a document for our 'users' collection
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })


def addDocumentExtra(db):
    # Create another sample that is slightly different
    doc_ref = db.collection(u'users').document(u'aturing')
    doc_ref.set({
        u'first': u'Alan',
        u'middle': u'Mathison',
        u'last': u'Turing',
        u'born': 1912
    })


def readFirestore(db):
    # Read back all the documents in firestore and print them to console
    users_ref = db.collection(u'users')
    docs = users_ref.stream()
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))


def main():
    # add argument for setting project
    parser = argparse.ArgumentParser()
    parser.add_argument('--projectid')
    args = parser.parse_args()

    # check if a projectid has been entered or not
    if args.projectid is not None:
        authenticateFirestore(args.projectid)
    else:
        print('please run `python uploadFirestore.py --projectid=<YOUR GCP PROJECT ID>')


if __name__ == '__main__':
    main()
