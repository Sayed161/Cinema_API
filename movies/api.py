from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from .models import Movie
from .schemas import MovieSchema,MovieCreateSchema,ranking_Update,status_Update
app = NinjaAPI()

@app.get("", response={200:list[MovieSchema]})
def get_movie(request):
    return Movie.objects.order_by('-ranking').all()

@app.get("/{slug}",response=MovieSchema)
def get_movie(request,slug:str):
    movie = get_object_or_404(Movie, slug=slug)
    return movie

@app.post("",response=MovieSchema)
def create_movie(request,movie:MovieCreateSchema):
    movie_data = movie.model_dump()
    movie_model = Movie.objects.create(**movie_data)
    return movie_model

@app.post("{slug}/ranking",response=MovieSchema)
def update_ranking(request,slug,ranking:ranking_Update):
    movie = get_object_or_404(Movie, slug=slug)
    movie.ranking = ranking.ranking
    movie.save()
    return movie

@app.post("{slug}/status",response=MovieSchema)
def update_ranking(request,slug,status:status_Update):
    movie = get_object_or_404(Movie, slug=slug)
    movie.status = status.status
    movie.save()
    return movie