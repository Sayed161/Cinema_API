from celery import shared_task
from .models import Movie

@shared_task
def update_ranking():
    for movie in Movie.objects.all():
        if movie.status == 'coming_up' or movie.status =='starting' :
            movie.ranking +=10
            movie.save()
        
