from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.db import transaction

# from .models import Member,User

# class MemberSignUpForm(UserCreationForm):
    
#     class Meta(UserCreationForm.Meta):
#         model = User

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_member = True
#         if commit:
#             user.save()
#         return user

# class LeadSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_lead = True
#         if commit:
#             user.save()
#         return user
