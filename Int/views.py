from django.shortcuts import render, redirect,HttpResponse
from .forms import DocumentForm
from .convert import Image
def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        #if form.is_valid():
        form.save()
        save = form.instance.uploaded_file
        print(save.url)
        z=Image(save)
        #name=request.FILES['uploaded_file'].name.split(".")[0]+".jpg"
        if(z==200):
            return render(request, 'Display.html', {'name':save.url.split(".")[0]+".jpg"})
        return HttpResponse("API is Not Work")
    else:
        form = DocumentForm()
    return render(request, 'index.html', {'form': form})

def upload_success(request):
    return render(request, 'success.html')