from django.shortcuts import render
from .forms import BMPImageForm

def upload_image(request):
    if request.method == 'POST':
        form = BMPImageForm(request.POST, request.FILES)
        print("form submitted")
        if form.is_valid():
            instance = form.save()
            print("form saved")
            # Extracting patient details from the name of the image file
            import re
            instance = form.save(commit=False)
            name = instance.image.name
            # Use regex to extract patient information from the image name
            match = re.match(r'^images/(\d+)__(M|F)_(Left|Right)_(\w+)_\w+\.BMP$', name)
            if match:
                patient_id = match.group(1)
                patient_gender = 'Male' if match.group(2) == 'M' else 'Female'
                patient_hand = match.group(3)
                patient_finger = match.group(4)

            else:
                patient_id = None
                patient_gender = None
                patient_hand = None
                patient_finger = None
            
            # Generating random values for other fields
            import random
            from faker import Faker
            fake = Faker()
            patient_name = fake.name()
            patient_height = random.randint(160, 190)
            patient_weight = random.randint(50, 100)
            match_value = random.randint(80, 95)
            
            return render(request, 'index.html', {'form': form, 
                                                  'patient_id': patient_id,
                                                  'patient_gender': patient_gender,
                                                  'patient_hand': patient_hand,
                                                  'patient_finger': patient_finger,
                                                  'patient_name': patient_name,
                                                  'patient_height': patient_height,
                                                  'patient_weight': patient_weight,
                                                  'match_value': match_value})
        else:
            print(form.errors)
    else:
        form = BMPImageForm()
        print("form displayed")
    return render(request, 'index.html', {'form': form})

