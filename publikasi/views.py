import json

from django.http import Http404
from django.shortcuts import render, redirect
from backend.CRUD.crud_publikasi import publikasi_create, publikasi_read,publikasi_delete
from backend.CRUD.crud_user import user_read
from backend.misc import firebase_init, getPhoto

# Initialize Firebase Database
fauth = firebase_init


# ---------------------
# Form Request Publikasi Keluar
# --------------------
def formPublikasi(request):
    try:
        if (request.session['uid']):
            print(1)
            if (fauth.get_account_info(request.session['uid'])):
                print(2)
                return render(request, 'form_publikasi.html')
            else:
                return redirect("/user/logout")
    except:
        return redirect("/user/login")


def postFormPublikasi(request):
    judul_konten = request.POST.get("judul_konten")
    deskripsi_kegiatan = request.POST.get("deskripsi_kegiatan")
    kanal_publikasi = request.POST.get("kanal_publikasi")
    link = request.POST.get("link")
    insidental = request.POST.get("insidental")
    id_feedback = ""
    
    if (insidental == "True"):
        insidental = True
    else:
        insidental = False
        bukti = ""

    message = publikasi_create(request, judul_konten, id_feedback, deskripsi_kegiatan, kanal_publikasi, link, insidental)
    print(message)
    if message != "terjadi error":
        return redirect("/publikasi/detail/" + message)
    else:
        return redirect("user:logout")


# ---------------------
# Detail Publikasi Keluar
# --------------------
def detail(request, id):
    try:
        if (request.session['uid']):
            print(1)
            user_session = fauth.get_account_info(request.session['uid'])
            print(1)
            if (user_session):
                print(1)
                data_detail = publikasi_read(id)
                print(1)
                user = user_read(user_session['users'][0]['localId'])
                print(1)
                print(user)
                if (data_detail != []):
                    print(1)
                    print(data_detail)
                    if (user["id"] == data_detail["idPemohon"] or "publikasi" in user["admin"]):
                        print(1)
                        # Get Dokumen Files
                        if ("publikasi" in user["admin"]):
                            admin = "true"
                        else:
                            admin = "false"
                        try:
                            url = getPhoto.getPhoto(data_detail["token_dokumen"][0])
                            dokumen = url
                        except:
                            dokumen = ""
                        return render(request, 'publikasi_details.html', {
                            'data': data_detail,
                            'user': user,
                            'admin': admin,
                            'id': id,
                            'dokumen': dokumen,
                        })
                    else:
                        raise Http404
            else:
                return redirect("/user/logout")
        else:
            return redirect("/user/signin")
    except:
        return redirect("/user/signin")


def delete(request):
    try:
        if (request.session['uid']):
            user_session = fauth.get_account_info(request.session['uid'])
            if (user_session):
                user = user_read(user_session['users'][0]['localId'])
                if ("publikasi" in user["admin"]):
                    print('masuk')
                    id_request = request.POST.get("id_request")
                    print(id_request)
                    data = publikasi_delete(id_request)
                    print(data)
                    return redirect('../user/dashboard_pengurus/publikasi/semua')
            else:
                return redirect('user:logout')
    except:
        return redirect('user:signin')