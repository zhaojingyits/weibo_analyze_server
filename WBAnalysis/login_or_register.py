from django.http import HttpResponse, JsonResponse
from AppUser.models import AppUserInfo
succeed={"result":"succeed"}
def login(request):
    _id=request.GET.get("id")
    _password=request.GET.get("passwd")
    
    if AppUserInfo.objects.filter(id=_id).exists()==False:
        res={"error":"user_not_exists"}
        return JsonResponse(res)
    else:
        user=AppUserInfo.objects.get(id=_id)
        if user.password!=_password:
            res={"error":"password_invalid"}
            return JsonResponse(res)
        else:
            return JsonResponse(succeed)

def register(request):
    _id=request.GET.get("id")
    _password=request.GET.get("passwd")
    _email = request.GET.get("email")

    if AppUserInfo.objects.filter(id=_id).exists() or AppUserInfo.objects.filter(email=_email).exists():
        res={"error":"user_exists"}
        return JsonResponse(res)
    us1=AppUserInfo()
    us1.id=_id
    us1.password=_password
    us1.email=_email
    us1.save()
    return JsonResponse(succeed)

def change_password(request):
    _id=request.GET.get("id")
    _password_former=request.GET.get("passwd_old")
    _password_new = request.GET.get("passwd_new")

    if _id==None or _id.strip()=="" or _password_former==None or _password_former.strip()=="" or _password_new==None or _password_new.strip()=="":
        res={"error":"empty_query"}
        return JsonResponse(res)
    if AppUserInfo.objects.filter(id=_id).exists() == False:
        res={"error":"user_not_exists"}
        return JsonResponse(res)
    elif AppUserInfo.objects.get(id=_id).password!=_password_former:
        res={"error":"former_password_invalid"}
        return JsonResponse(res)
    else:
        s = AppUserInfo.objects.get(id=_id)
        s.password=_password_new
        s.save()
        return JsonResponse(succeed)