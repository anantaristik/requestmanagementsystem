import json

from django.http import Http404
from django.shortcuts import render, redirect
from backend.CRUD.crud_feedback import feedback_create, feedback_read, feedback_delete
from backend.CRUD.crud_user import user_read
from backend.misc import firebase_init, getPhoto

# Initialize Firebase Database
fauth = firebase_init


# ---------------------
# Form Request Feedback
# --------------------
def formFeedback(request, id, jenis):
    try:
        if (request.session['uid']):
            print(1)
            if (fauth.get_account_info(request.session['uid'])):
                print(2)
                return render(request, 'form_feedback.html', {
                    'id': id,
                    'jenis': jenis
                })
            else:
                return redirect("/user/logout")
    except:
        return redirect("/user/login")


def postFormFeedback(request):
    berkas = request.POST.get("uploadFiles")
    berkas = json.loads(berkas)
    id_permohonan = request.POST.get("id")
    status = request.POST.get("status")
    komentar = request.POST.get("komentar")
    jenis = request.POST.get("jenis")

    try:
        if berkas[0]["successful"]:
            bukti_meta = []
            bukti_meta.append(berkas[0]["successful"][0]["meta"]["id_firebase"])
            message = feedback_create(request, id_permohonan, status, komentar, bukti_meta, jenis)
            if message != "terjadi error":
                return redirect("/" + jenis + "/detail/" + id_permohonan)
            else:
                message = "Gagal Upload"
                return redirect("/" + jenis + "/detail/" + id_permohonan)
        else:
            message = "Gagal Upload"
            return redirect("/" + jenis + "/detail/" + id_permohonan)
    except:
        return redirect("/")

    print(message)
    if message != "terjadi error":
        return redirect("/feedback/detail/" + message)
    else:
        return redirect("user:logout")


# ---------------------
# Detail Feedback
# --------------------
def detail(request, id):
    # try:
        if (request.session['uid']):
            print(1)
            user_session = fauth.get_account_info(request.session['uid'])
            print(1)
            if (user_session):
                print(id)
                data_detail = feedback_read(id)
                print(1)
                user = user_read(user_session['users'][0]['localId'])
                print(1)
                print(user)
                if (data_detail != []):
                    print(1)
                    print(data_detail)
                    if (user["id"] == data_detail["id_pengurus"] or user["admin"]):
                        print(1)
                        # Get Dokumen Files
                        if (user["admin"]):
                            admin = "true"
                        else:
                            admin = "false"
                        try:
                            url = getPhoto.getPhoto(data_detail["token_dokumen"][0])
                            dokumen = url
                        except:
                            dokumen = ""
                        return render(request, 'feedback_details.html', {
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
            return redirect("/user/login")
    # except:
    #     return redirect("/user/login")


def delete(request):
    try:
        if (request.session['uid']):
            user_session = fauth.get_account_info(request.session['uid'])
            if (user_session):
                user = user_read(user_session['users'][0]['localId'])
                if (user["admin"]):
                    print('masuk')
                    id_request = request.POST.get("id_request")
                    print(id_request)
                    data = feedback_delete(id_request)
                    print(data)
                    return redirect('../user/dashboard_pengurus/feedback/semua')
            else:
                return redirect('user:logout')
    except:
        return redirect('user:login')