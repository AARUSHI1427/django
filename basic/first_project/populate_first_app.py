import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

#fake pop script

import random
from first_app.models import AccessRecord,Topic,webpage
from faker import Faker

fakegen=Faker()
topics=['search','social','marketplace','news','games']

def add_topic():
   t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
   t.save()
   return t

def populate(N=5):

    for entry in range(N):

        #get the topic for entry
        top=add_topic()

        #Create the fake data for that entry
        fake_url=fakegen.url()
        fake_name=fakegen.name()
        fake_date=fakegen.date()

        #create new webpage entry
        webpg= webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create a fake access record for that webpage
        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__=='__main__':
    print("populating script")
    populate(20)
    print("populated")
