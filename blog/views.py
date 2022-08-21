from turtle import title
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class BlogListView(View):
    def get(self, request, *args, **kwargs):
        # Para listar primero llamamos a los Post de la BD
        posts = Post.objects.all()
        context = {
            'posts':posts
            #El primer posts es el nombre con el que 
            #vamos a llamar al html y el segundo la variable
            # que creamos posts = Post.objects.all()
        }
        return render(request,'blog_list.html', context)


# La vista del PostCreateForm
"""
METODO GET: Es todo el requerimiento que se le pide 
al servidor para mostrar la informacion al usuario 

METODO POST: Es todo requerimiento que se le pide al 
usuario 

"""
class BlogCreateView(View): 
    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        context = {
            'form':form
            #'Form' es el nombre con el que puedo 
            #llamar en el html a lo que hay dentro del 
            # PostCraeteForm
            #Que es el titulo y content del post a crear
        }
        return render(request, 'blog_create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method=="POST":

            """
            Si al enviar es un metodo post se llama al
            formulario con el requerimiento post 

            """
            form = PostCreateForm(request.POST)

            
            if form.is_valid():
                # Si el form es valido queremos obtener el contenido
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                #Creamos el post 
                p, created = Post.objects.get_or_create(title=title, content=content)
                """ 
                El title y el content de la izquierda vienen del post de modelos.py
                que contiene un title y un content.

                Los de la derecha vienen del title = form.cleaned_data de aqui
                lo que estamos diciendole es que guarde la info que se obtuvo 
                en el formulario 

                """
                #Guardamos todo 
                p.save() 
                return redirect('blog:home')

        context = {
            
        }
        return render(request, 'blog_create.html', context)

class BlogDetailView(View):
    # Una vez registrado el pk en urls podemos hacer uso 
    def get(self, request, pk, *args, **kwargs):
        """ 
        Esta variable post llama al post con cierto id
        en caso que no exista llama la pagina que contiene 
        el error 404
        
        """
        post = get_object_or_404(Post, pk=pk)
        context = {
            "post":post
        }
        return render(request, 'blog_detail.html', context)

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog_update.html'

    def get_success_url(self):
        # Referenciamos al id del post 
        """
        self.kwargs es la informacion que esta dentro 
        del dato que estamos llamando en este caso pk 

        """
        pk = self.kwargs['pk']
        # Usamos el kwargs pk para refrescar el detail del blog 
        return reverse_lazy('blog:detail', kwargs={'pk':pk})


class BlogDeleteView(DeleteView):
    model = Post
    template_name= 'blog_delete.html'
    success_url = reverse_lazy('blog:home')