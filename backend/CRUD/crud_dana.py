import firebase_admin
from firebase_admin import credentials, firestore, storage
# from backend.misc import firebase_init
# from .crud_user import user_read
import datetime
import pytz

# --------------------------
# Initialize Firebase Admin
# --------------------------
if not firebase_admin._apps:
    cred = credentials.Certificate("testing-key.json")
    firebase_admin.initialize_app(cred, {
        'storageBucket' : 'request-management-syste-62a37.appspot.com'
    })

# fauth = firebase_init
db = firestore.client()
ds = storage.bucket()

# --------------------------
# CRUD Functions
# --------------------------
def reimbursement_create(judul, nama_kegiatan, deskripsi_kegiatan, jumlah_dana, nomor_rekening, atas_nama_rekening, nama_bank, bukti_pembayaran):
    # print(request.session['uid'])
    # user_data = fauth.get_account_info(request.session['uid'])
    
    # uname = user_data['user'][0]['localId']
    # user_data = user_read(uname)['id']

    # id_pemohon = user_data

    id_permohonan_rb = "rb-" + nama_kegiatan.replace(" ", "-").lower()

    data = {
        'judul':judul,
        'id_permohonan_rb': id_permohonan_rb,
        'nama_kegiatan': nama_kegiatan,
        'deskripsi_kegiatan': deskripsi_kegiatan,
        'id_feedback': "",
        # 'id_pemohon': id_pemohon,
        'jumlah_dana': jumlah_dana,
        'nomor_rekening':nomor_rekening,
        'atas_nama_rekening':atas_nama_rekening,
        'nama_bank':nama_bank,
        'bukti_transaksi':[],
        'bukti_pembayaran':bukti_pembayaran,
        'waktu_permintaan': datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
    }

    collections = db.collection('InformasiPermohonan').document('keuangan')
    collections.collection('permohonanReimburse').document(id_permohonan_rb).set(data)

    return id_permohonan_rb


# --------------------------
# Read
# --------------------------
def reimbursement_read(id_permohonan_rb):
    data = db.collection('InformasiPermohonan').document('keuangan')
    data = data.collection('permohonanReimburse').document(id_permohonan_rb).get().to_dict()
    print(data)
    return data

reimbursement_read('reimburse-1')

def reimbursement_read_all():
    try:
        data_dict = []
        datas = db.collection('InformasiPermohonan').document('keuangan')
        datas = data.collection('permohonanReimburse').get()
        for data in datas:
            data_dict.append(data.to_dict())
        return data_dict
    except:
        data_dict = []
    return data_dict

def reimbursement_read_all_line():
    try:
        data_dict = []
        datas = db.collection('InformasiPermohonan').document('keuangan')
        datas = datas.collection('permohonanReimburse').order_by('waktu_permintaan').limit(10).get()
        for data in datas:
            data_dict.append(data.to_dict())
        return data_dict
    except:
        data_dict = []
    return data_dict

# --------------------------
# Update
# --------------------------
def reimbursement_update(id_permohonan_rb, nama_kegiatan, deskripsi_kegiatan, jumlah_dana, insidental):
    try:
        data = db.collection('InformasiPermohonan').document('keuangan')
        data.collection('permohonanReimburse').document(id_permohonan_rb).update({
            'nama_kegiatan': nama_kegiatan,
            'deskripsi_kegiatan': deskripsi_kegiatan,
            'jumlah_dana': jumlah_dana,
            'insidental': insidental,
    })
        return ""
    except:
        return "error"

# --------------------------
# Delete
# --------------------------
def reimbursement_delete(id_permohonan_rb):
    try:
        data = db.collection('InformasiPermohonan').document('keuangan')
        data = data.collection('permohonanReimburse').document(id_permohonan_rb).delete()
        return data
    except:
        return