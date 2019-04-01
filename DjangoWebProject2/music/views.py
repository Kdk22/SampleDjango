from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView):
    template_name ='music/index.html'
    context_object_name = 'all_albums' #By default it gives object_list
    
    def get_queryset(self):
        return Album.objects.all()

class DetailsView(generic.DetailView):
    model = Album # here model passes value to details.html
    template_name ='music/details.html'


class AlbumCreate(CreateView):
    model = Album
    fields =['artist', 'album_title', 'genre', 'album_logo']

    
class AlbumUpdate(UpdateView):
    model = Album
    fields =['artist', 'album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class= UserForm
    template_name ='music/registration_form.html'

    #displays black form when user wants to register
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
        
    # IT registers the data to the database
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user= form.save(commit= False) #It does not saves to the database yet

            #cleaned (normalized or formated ) data is only entered in database

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #to change the users the password
            user.set_password(password)
            user.save()

            #return user objects if credentials are correct

            user = authenticate(username= username, password= password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})
                    









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