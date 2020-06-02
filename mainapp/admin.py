from django.contrib import admin
from .models import Challenges, ChallengeAudience, Preapproved_challenge, ChallengeTag

admin.site.site_header = "Research Administration"

admin.site.register(Challenges)
admin.site.register(ChallengeAudience)
admin.site.register(Preapproved_challenge)
admin.site.register(ChallengeTag)
