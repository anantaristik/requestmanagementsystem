import json

from django.http import Http404
from django.shortcuts import render, redirect
from backend.CRUD.crud_user import user_read
from backend.CRUD.crud_dana import *
from backend.misc import firebase_init

# Initialize Firebase Database
fauth = firebase_init

# ---------------------
# Form Request Reimbursement
# --------------------
def form_reimbursement(request):
    return render(request, 'reimbursement/form_reimbursement.html')

def post_form_reimbursement(request):
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
        message = reimbursement_create(request, nama_kegiatan, deskripsi_kegiatan, jumlah_dana, nomor_rekening, atas_nama_rekening, nama_bank, photos_meta)
        if message != "terjadi error":
            return redirect("/reimbursement/detail/" + message)
        else:
            message = "Gagal Upload"
            return redirect('reimbursement:form_reimbursement')
    else:
        message = "Gagal Upload"
        return redirect('reimbursement:form_reimbursement')