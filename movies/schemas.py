from ninja import ModelSchema,Schema
from .models import Movie
from datetime import datetime

class MovieSchema(ModelSchema):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieCreateSchema(Schema):
    name : str
    protagonist: str
    poster:str
    trailer:str
    start_date: datetime
    status:str
    ranking:int

class ranking_Update(Schema):
    ranking : int 
    
class status_Update(Schema):
    status : str 
    