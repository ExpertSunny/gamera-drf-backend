from django.db import models

# Create your models here.
def upload_poster(instance, filename):
    return 'images/posters/{filename}'.format(filename=filename)

def upload_orgimg(instance, filename):
    return 'images/orgimgs/{filename}'.format(filename=filename)

def upload_slide(instance, filename):
    return 'images/slides/{filename}'.format(filename=filename)

class Game(models.Model):
    game_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 50)
    # path = models.CharField(default = 'coming-soon', max_length = 20)
    gameImg = models.ImageField(upload_to=upload_poster)
    active = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Tourney(models.Model):   
    tourney_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length = 50)
    org_name = models.CharField(max_length = 50)
    org_img = models.ImageField(upload_to=upload_orgimg)
    game_id = models.IntegerField()
    event_place = models.CharField(max_length = 50)
    event_prize = models.CharField(max_length = 20)
    event_url = models.CharField(max_length = 200)
    event_time = models.DateTimeField()
    event_fees = models.CharField(max_length = 20)
    match_type = models.CharField(max_length = 20)
    active = models.BooleanField(default = True)

    def __str__(self):
        return self.event_name
    
class Slide(models.Model):
    slide_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 50)
    path = models.CharField(default = 'coming-soon', max_length = 20)
    slide_img = models.ImageField(upload_to=upload_slide)

    def __str__(self):
        return self.name