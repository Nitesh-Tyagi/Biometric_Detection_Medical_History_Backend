from django.shortcuts import render

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        # Save the image to a folder on the server
        with open('media/' + image.name, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)
        # Render a template with the image name
        return render(request, 'myapp/image_upload.html', {'name': image.name})
    else:
        return render(request, 'myapp/image_upload.html')
