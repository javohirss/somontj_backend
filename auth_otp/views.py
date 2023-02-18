from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django_otp.oath import totp
from django.conf import settings
from django.utils import timezone

def OTPView(request):
    secret_key = bytes(settings.OTP_SETTINGS['OTP_TOTP_SECRET'], 'utf-8')
    step = int(settings.OTP_SETTINGS['OTP_TOTP_STEP'])
    digits = int(settings.OTP_SETTINGS['OTP_TOTP_DIGITS'])
    now = int(timezone.now().timestamp())
    print(totp(key=secret_key, step=step, digits=digits))

    return redirect('/')
