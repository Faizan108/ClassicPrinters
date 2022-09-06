from django.contrib import admin
from .models import visiting_card, brochure, letter_head, envelope
# Register your models here.

admin.site.register(visiting_card)
admin.site.register(letter_head)
admin.site.register(brochure)
admin.site.register(envelope)