from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Investments,Transactions,Packages
from accounts.models import LoginHistory
from appi import utils
User = get_user_model()





class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'





class TransactionSerializer(serializers.ModelSerializer):
    user = ProfileSerializer( read_only=True)
    class Meta:
        model = Transactions
        fields = '__all__'


class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = '__all__'
        
        
class InvestmentSerializer(serializers.ModelSerializer):
    user = ProfileSerializer( read_only=True)
    package = PackagesSerializer(read_only=True)
    class Meta:
        model = Investments
        fields = '__all__'


class LoginhistorySerializer(serializers.ModelSerializer):
    user = ProfileSerializer( read_only=True)
    class Meta:
        model = LoginHistory
        fields = '__all__'



# class UpdatePayinfoSerializer(serializers.ModelSerializer):

#     class Meta:
#         model : User
#         fields = (
#             "btc_id",
#             "usdt_id",
#             "perfect_money_id",
#         )

#         extra_kwargs = {
#              "btc_id": {'write_only':True,"required": False},
#              "usdt_id": {'write_only':True,"required": False},
#              "perfect_money_id": {'write_only':True,"required": False},
#         }
