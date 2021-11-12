from Feedback.models import FeedbackEntity
from django.http import HttpResponse
def do_feedback(request):
    _app_user_id = request.GET.get("userid")
    _wb_user_id = request.GET.get("wbid")
    _user_customize_score=request.GET.get("score")
    _info=request.GET.get("info")
    fb1=FeedbackEntity(app_user_id=_app_user_id,wb_user_id=_wb_user_id,user_customize_score=_user_customize_score,info=_info)
    fb1.save()
    return HttpResponse("OK")