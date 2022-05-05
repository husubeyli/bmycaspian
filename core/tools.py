from time import time
import random, string, calendar, datetime
from datetime import date
from django.utils import timezone



def get_about_page_signature(instance, filename):
    return "about-page/signature%s_%s" % (str(time()).replace('.', '_'), filename)

