from django.urls import path
from mailing_list.views import Join, Unsubscribe, Bye, Thanks

urlpatterns = [
    path('', Join.as_view(), name="join_news"),
    path('unsubscribe', Unsubscribe.as_view(), name="leave_news"),
    path('bye', Bye.as_view(), name="bye_news"),
    path('thanks', Thanks.as_view(), name="hello_news"),
]
