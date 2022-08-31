from django import forms
# from accounts.models import Account
from userdashboard.models import Packages




class NewPackageForm(forms.ModelForm):

    class Meta:
        model = Packages
        fields = ('name','hours','percent','ref_percent','min_amount','max_amount')