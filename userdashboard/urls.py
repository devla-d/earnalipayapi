from django.urls import path
from .views import  DashAPIView,get_pacakges,create_investment,end_user_investment,WithdrawApiview,TransactionApiview,SettingsApiview


urlpatterns = [
    path('dashboard/',DashAPIView.as_view()),
    path('packages/',get_pacakges),
    path('create-investment/',create_investment),
    path('end-investment/',end_user_investment),
    path('withdrawal/',WithdrawApiview.as_view()),
    path('transactions/',TransactionApiview.as_view()),
    path('settings/',SettingsApiview.as_view()),
]
