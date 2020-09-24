from background_task import background
from .models import Good
from datetime import timedelta
from scrapping import interpark , crawlingyes24
from django.shortcuts import HttpResponse

@background(schedule=timedelta(seconds=20))

def update_table():
    inter_data = interpark.interpark()
    yes24_data = crawlingyes24.get_data()
    data = inter_data + yes24_data
    Good.objects.all().delete()

    for value in data:
        if (value['category'] == '전시') or (value['category'] =='관람'):
            category_num=1

        elif (value['category'] == '콘서트') or (value['category'] =='공연'):
            category_num=2

        elif (value['category'] == '연극' ) or (value['category'] == '뮤지컬'):
            category_num=3

        Good.objects.create(
            enddate = value['enddate'],
            startdate = value['startdate'],
            href = value['href'],
            img = value['img'],
            title = value['title'],
            players = value['players'],
            category = category_num
            )


def background_view():
    update_table()
    print('Data Updated!')
    return HttpResponse("Data updated!")