from django.views import generic
from .models import Album

class IndexView(generic.ListView):
    template_name ='music/index.html'
    context_object_name = 'all_albums' #By default it gives object_list
    
    def get_queryset(self):
        return Album.objects.all()

class DetailsView(generic.DetailView):
    model = Album # here model passes value to details.html
    template_name ='music/details.html'

'''
    from django.shortcuts import render, get_object_or_404
    from .models import Album, Song
 
    def index(request):
        all_albums = Album.objects.all()
        return render(request, 'music/index.html', {'all_albums': all_albums})

    def details(request, album_id):
        album= get_object_or_404(Album, pk= album_id)
        return render(request, 'music/details.html', {'album':album})
   
    def favorite(request, album_id):
        album= get_object_or_404(Album, pk= album_id)
        try:
            selected_song = album.song_set.get(pk= request.POST['song'])
        except(KeyError, Song.DoesNotExist):
            return render(request, 'music/details.html', {'album': album,
            'error_message':'You did not select a valid song',})
        else:
            if selected_song.is_favorite:
                selected_song.is_favorite= False
            else:
                selected_song.is_favorite= True        
                selected_song.save()
            return render(request, 'music/details.html', {'album': album})
'''