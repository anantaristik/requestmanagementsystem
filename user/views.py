from django.shortcuts import render, redirect
from django.contrib import auth
from backend.crud.crud_user import user_create, user_read
from backend.misc import firebase_init
from backend.constant.birdeptim import pi, birdeptim, kode_fungsionaris

def login(request):
	return render(request, 'login.html')

def postLogin(request):
    try :
        email = request.POST.get("email")
        password = request.POST.get("password")

        try :
            user = firebase_init.sign_in_with_email_and_password(email, password)
        except:
            return redirect(login)

        print(user)
        session_id = user['idToken']
        request.session['uid'] = str(session_id)
        
        return redirect('/')

    except:
        return redirect("user:login")

def signUp(request):
	return render(request, 'register.html', {
		"pi": pi,
		"birdeptim": birdeptim,
		"kode_fungsionaris": kode_fungsionaris
	})

def postSignUp(request):
    try:
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        password2 = request.POST.get("password2")
        nama = request.POST.get("nama")
        divisi = request.POST.get("birdeptim")
        if (password == password2):
            message = user_create(uname, email, password, divisi, nama, "pemohon")
		
        print(message)
        if message == "":
            return redirect("user:login")
        else:
            return redirect("user:signup")

    except:
        return redirect("user:signup")

def logout(request):
    auth.logout(request)
    return redirect("user:login")