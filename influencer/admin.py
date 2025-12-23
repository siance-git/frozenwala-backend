from django.contrib import admin
from .models import Influencer,InfluencerOtp,InfluencerAmount,InfluencerLink
admin.site.register(Influencer)
admin.site.register(InfluencerAmount)
admin.site.register(InfluencerOtp)
admin.site.register(InfluencerLink)

# Register your models here.
