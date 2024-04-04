from django.shortcuts import render
from django.http import HttpResponse
from .bmi import *
from .forms import *

def home(request):
    height_result = None
    height_result_meters = None
    weight_result = None
    bmi_result = None
    bmi_label = None
    if request.method == 'POST':
        form = HeightForm(request.POST)
        if form.is_valid():
            feet = form.cleaned_data['feet']
            inches = form.cleaned_data['inches']
            lbs = form.cleaned_data['lbs']
            height_result = calc_height_in_inches(feet, inches)
            height_result_meters = calc_height_in_meters(height_result)
            weight_result = calc_weight_in_kg(lbs)
            bmi_result = calculate_bmi(height_result_meters, weight_result)
            bmi_label = find_bmi_label(bmi_result)
    else:
        form = HeightForm()

    context = {
        'form': form,
        'height_result': height_result,
        'height_result_meters': height_result_meters,
        'weight_result': weight_result,
        'bmi_result': bmi_result,
        'bmi_label': bmi_label,
    }
    return render(request, 'home.html', context)
