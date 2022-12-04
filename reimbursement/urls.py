import json

from django.http import Http404
from django.shortcuts import render, redirect
from backend.CRUD.crud_dana import reimbursement_create, reimbursement_read, reimbursement_read_all, reimbursement_read_all_line
from backend.CRUD.crud_user import user_read
from backend.misc import firebase_init


# Initialize Firebase Database
fauth = firebase_init

# ---------------------
# Form Request Reimbursement
# --------------------
