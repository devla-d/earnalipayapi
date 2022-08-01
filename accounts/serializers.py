from rest_framework import serializers
#from countryinfo import CountryInfo
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from appi import utils
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    
    ref_code = serializers.CharField(
         required=False
    )

    class Meta:
        model = User
        fields = [
            "full_name",
            "username",
            "email",
            "zipcode",
            "address",
            "city",
            "state",
            # "date_of_birth",
            "phone",
           
            "country_of_residence",
            "citizenship",
            "btc_id",
            "usdt_id",
            "perfect_money_id",
            "password",
            "ref_code",
        ]

        extra_kwargs = {
            "btc_id": {"required": False},
            "usdt_id": {"required": False},
            "perfect_money_id": {"required": False},
        }

    def save(self):
        #currencies = CountryInfo(self.validated_data["country_of_residence"]).currencies()
        account = User(
            full_name=self.validated_data["full_name"],
            username=f"{utils.user_unique_id()}@{self.validated_data['username']}",
            
            email=self.validated_data["email"],
            zipcode=self.validated_data["zipcode"],
            address=self.validated_data["address"],
            city=self.validated_data["city"],
            state=self.validated_data["state"],
            # date_of_birth=self.validated_data["date_of_birth"],
            phone=self.validated_data["phone"],
            country_of_residence=self.validated_data["country_of_residence"],
            citizenship=self.validated_data["citizenship"],
            btc_id=self.validated_data["btc_id"],
            usdt_id=self.validated_data["usdt_id"],
            perfect_money_id=self.validated_data["perfect_money_id"],
            local_currency = "USD",
        )
        password = self.validated_data["password"]
        account.set_password(password)
        
        account.save()
        return account
