from decimal import DefaultContext
from email.policy import default
from unicodedata import category
from django.db import models

# Create your models here.


# Visitig_Cards


card_categ=(
    ('General','General'),
    ('Health & Care','Health & Care'),
    ('Construct & Real Estate','Construction & Real Estate'),
    ('Fashion','Fashion'),
    ('Legal','Legal'),
    ('Beauty Shop','Beauty Shop'),
    ('Manufacturing','Manufacturing'),
    ('Automobile','Automobile'),
    ('Print & Technology','Print & Technology'),
    ('Food & Restraunt','Food & Restraunt'),
    ('Education','Education'),
    ('Tour & Travels','Tour & Travels'),
)

card_quality=(
    ('matt','matt'),
    ('UV','UV'),
    ('glossy','glossy'),
    ('texture','texture'),
    ('varnish','varnish'),
)

orien=(
    ('horizontal', 'horizontal'),
    ('vertical', 'vertical')
)

class visiting_card(models.Model):
    card_id=models.AutoField
    card_name=models.CharField(default="", max_length=30)
    card_cat=models.CharField(choices=card_categ, default="", max_length=30)
    card_qual=models.CharField(choices=card_quality, max_length=20, default='matt')
    card_orien=models.CharField(max_length=15, choices=orien, default='horizontal')
    card_price=models.IntegerField(default=300)
    card_image=models.ImageField(upload_to='Visiting Cards/',default='')



# LetterHead

size=(
    ('A4','A4'),
)

lh_quality=(
    ('matte','matte'),
    ('Bond','Bond'),
)


class letter_head(models.Model):
    lh_id=models.AutoField
    lh_name=models.CharField(default="", max_length=30)
    lh_qual=models.CharField(choices=lh_quality, default='matte', max_length=20)
    lh_size=models.CharField(choices=size, default='A4',max_length=5)
    lh_price=models.IntegerField(default=300)
    lh_image=models.ImageField(upload_to='Letter Heads/',default='')

# Brochure


bsize=(
    ('A4','A4'),
    ('A3', 'A3')
)

class brochure(models.Model):
    bro_id=models.AutoField
    bro_name=models.CharField(default='', max_length=30)
    bro_size=models.CharField(choices=bsize, default='A4', max_length=5),
    bro_art_paper=models.IntegerField(default=100)
    bro_price=models.IntegerField(default=300)
    bro_image=models.ImageField(upload_to='Brochure/',default='')


#envelope


esize=(
    ('A4','A4'),
)

ecat=(
    ('Doctors', 'Doctors'),
)

class envelope(models.Model):
    env_id=models.AutoField
    env_name=models.CharField(default='', max_length=30)
    env_size=models.CharField(choices=esize, default='A4', max_length=5)
    env_cat=models.CharField(choices=ecat, default='Doctors', max_length=25)
    env_price=models.IntegerField(default=300)
    env_image=models.ImageField(upload_to='Envelope/',default='')