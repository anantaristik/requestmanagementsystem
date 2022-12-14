import json

from django.http import Http404
from django.shortcuts import render, redirect
from backend.CRUD.crud_user import user_read
from backend.CRUD.crud_keuangan import *
from backend.misc import firebase_init, getPhoto

# Initialize Firebase Database
fauth = firebase_init

# ---------------------
# Form Request Reimbursement
# --------------------
def form_reimbursement(request):
    try:
        if (request.session['uid']):
            if (fauth.get_account_info(request.session['uid'])):
                return render(request, 'form_reimbursement.html')
            else:
                return redirect("/user/logout")
    except:
        return redirect("/user/login")

def post_form_reimbursement(request):
    judul = request.POST.get("judul")
    nama_kegiatan = request.POST.get("nama_kegiatan")
    deskripsi_kegiatan = request.POST.get("deskripsi_kegiatan")
    nama_bank = request.POST.get("nama_bank")
    nomor_rekening = request.POST.get("nomor_rekening")
    atas_nama_rekening = request.POST.get("atas_nama_rekening")
    jumlah_dana = request.POST.get("jumlah_dana")
    photos = request.POST.get("uploadFiles")
    photos = json.loads(photos)
    print(photos)

    # Upload data to firebase
    if photos[0]["successful"]:
        photos_meta = []
        for i in photos[0]["successful"]:
            photos_meta.append(i["meta"]["id_firebase"])
        message = reimbursement_create(request, judul, nama_kegiatan, deskripsi_kegiatan, jumlah_dana, nomor_rekening, atas_nama_rekening, nama_bank, photos_meta)
        if message != "terjadi error":
            return redirect("/keuangan/detail/" + message)
        else:
            message = "Gagal Upload"
            return redirect('reimbursement:form_reimbursement')
    else:
        message = "Gagal Upload"
        return redirect('reimbursement:form_reimbursement')

# ---------------------
# Detail Reimbursement
# --------------------
def detail(request, id):
    try:
        if (request.session['uid']):
            user_session = fauth.get_account_info(request.session['uid'])
            if (user_session):
                data_detail = reimbursement_read(id)
                user = user_read(user_session['users'][0]['localId'])
                if (data_detail != []):
                    if (user["id"] == data_detail["id_pemohon"] or "keuangan" in user["admin"]):
                        # Get Dokumen Files
                        if ("keuangan" in user["admin"]):
                            admin = "true"
                        else:
                            admin = "false"
                    data_photo = []
                    # Get Photos Bukti Pembayaran
                    for photo in data_detail['bukti_pembayaran']:
                        url = getPhoto.getPhoto(photo)
                        data_photo.append(url)
                    # Get Bukti Transfer
                    try:
                        url = getPhoto.getPhoto(data_detail['bukti_transfer'][0])
                        transfer = url
                    except:
                        transfer = ''
                    print(data_detail)
                    print(data_photo)
                    return render(request, 'reimbursement_details.html', {
                        'data': data_detail,
                        'id': id,
                        'admin':admin,
                        'photos': data_photo,
                        'transfer': transfer,
                        'user': user
                    })
                else:
                    return redirect("/user/logout")
        else:
            return redirect("/user/login")
    except:
        return redirect("/user/login")

def delete(request):
    try:
        if (request.session['uid']):
            user_session = fauth.get_account_info(request.session['uid'])
            if (user_session):
                user = user_read(user_session['users'][0]['localId'])
                if ("keuangan" in user["admin"]):
                    print('masuk')
                    id_request = request.POST.get("id_request")
                    print(id_request)
                    data = reimbursement_delete(id_request)
                    print(data)
                    return redirect('home:publikasi')
            else:
                return redirect('user:logout')
    except:
        return redirect('user:signin')
