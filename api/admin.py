from django.contrib import admin

from api.models import Game, Slide, Tourney

# Register your models here.
admin.site.register(Game)
admin.site.register(Tourney)
admin.site.register(Slide)