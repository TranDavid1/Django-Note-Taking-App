from tastypie.resources import ModelResource
from api.models import Note
from tastypie.authorization import Authorization

# create resource from imported model


class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()   # all note objects
        resource_name = 'note'          # important for URLs
        authorization = Authorization()     # basic Authorization class
        field = ['title', 'body']
