from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from django.utils import timezone
from django.contrib.auth import authenticate


from appi import utils

from .serializers import RegisterSerializer
from .models import Referral,LoginHistory,Account
from userdashboard.serializers import ProfileSerializer

class RegisterUserAPIView(APIView):
	permission_classes = (AllowAny,)

	def post(self, request, format=None):
		serializer = RegisterSerializer(data=request.data)
		email = request.data.get('email', '0').lower()
		ref_code = request.data.get('ref_code', '0')
		username = request.data.get('username', '0')
		# referred = false
		

		if utils.validate_email(email) != None:
			return Response({"erro":'That email is already taken'})

		if utils.validate_username(username) != None:
			return Response({"erro":'That username is already taken'})



		if serializer.is_valid():
			if ref_code  and  utils.validate_username(ref_code)  != None:
				instance = serializer.save()
				try:
					old_user = Account.objects.get(username=ref_code)
					
				except Account.DoesNotExist:
					return Response({"erro":'UNKNOWN ERROR IN REFERRALS'})

				referred_by = Referral.objects.get(user=old_user)
				my_referral =  Referral.objects.get(user=instance)

				referred_by.referrals.add(instance)
				old_user.referral_bonus += 10
				old_user.referral += 1
				old_user.save()
				my_referral.referred_by = old_user
				my_referral.save()
			else:
				serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors)






class ObtainAuthTokenView(APIView):

	
	permission_classes = (AllowAny,)

	def post(self, request):
		context = {}

		email = request.POST.get('email')
		password = request.POST.get('password')
		browser_type = request.user_agent.browser.family
		browser_version = request.user_agent.browser.version_string
		
		account = authenticate(email=email, password=password)
		if account:
			LoginHistory.objects.create(user=account,ip_add=utils.get_client_ip(request),browser=f"{browser_type} {browser_version}")
			try:
				token = Token.objects.get(user=account)
			except Token.DoesNotExist:
				token = Token.objects.create(user=account)
			serializer = ProfileSerializer(account)
			context['res'] = 'Successfully authenticated.'
			context['user'] = serializer.data
			
			context['token'] = token.key
		else:
			context['erro'] = 'Invalid username or password'

		return Response(context)


