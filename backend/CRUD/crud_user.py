import firebase_admin
from firebase_admin import credentials, firestore, storage, auth
from backend.misc import firebase_init

# --------------------------
# Initialize Firebase Admin
# --------------------------
if not firebase_admin._apps:
    cred = credentials.Certificate("testing-key.json")
    firebase_admin.initialize_app(cred, {
        'storageBucket' : 'request-management-syste-62a37.appspot.com'
    })

fauth = firebase_init
db = firestore.client()
ds = storage.bucket()


# --------------------------
# CRUD Functions Dashboard
# --------------------------

def user_create(uname, email, password, divisi, nama, role):
    try:
        user = auth.create_user(
            uid=uname ,email=email, email_verified=False, password=password)
        print('Sucessfully created new user: {0}'.format(user.uid))
    except auth.EmailAlreadyExistsError:
        message = 'The user with the provided email already exists'
        return message;
    except auth.UidAlreadyExistsError:
        message = 'The user with the provided username already exists'
        return message;
    data = {
        'id': uname,
        'email': email,
        'nama': nama,
        'divisi': divisi,
        'role': role,
    }
    db.collection('user').document(uname).set(data)
    return ""

def user_read(uname):
    data = db.collection('user').document(uname).get().to_dict()
    print(data)
    return data

def user_all():
    users = db.collection('user').get()
    data_dict = [user.to_dict() for user in users]

    return data_dict

def user_update_email(uname, email):
    user = auth.update_user(
        uname,
        email=email)

    print('Sucessfully updated user: {0}'.format(user.uid))

def user_update_password(uname, password):
    user = auth.update_user(
        uname,
        password=password)

    print('Sucessfully updated user: {0}'.format(user.uid))

def user_update_data(uname, email, password, divisi, nama, role):
    data = {
        'id': uname,
        'email': email,
        'nama': nama,
        'divisi': divisi,
        'role': role,
    }
    db.collection('user').document(uname).set(data)
    return data

def user_delete(uname):
    try:
        data = db.collection('user').document(uname).delete()
        auth.delete_user(uname)
        print('Successfully deleted user')
        return data
    except:
        return