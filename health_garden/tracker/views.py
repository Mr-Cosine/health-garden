from django.shortcuts import render, redirect
from .models import food, water, medication
from .forms import food_form, water_form
from datetime import datetime
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.signing import Signer, BadSignature
from django.views.decorators.csrf import csrf_exempt
import json

#----------------------------------------------------------------------------------------------------------------
# Home

def dashboard(request):
    return render(request, 'tracker/home.html')

#----------------------------------------------------------------------------------------------------------------
# Daily calories intake panel

def calories_panel(request):
    if request.method == 'POST':
        form = food_form(request.POST)
        if form.is_valid():
            food.objects.create(
                name=form.cleaned_data['name'] or 'Food',
                calories=form.cleaned_data['calories'],
                date=datetime.now().date()
            )
            return redirect('calories_panel')
    else:
        form = food_form(initial={'unit_calories': 0, 'quantity': 1})

    return render(request, 'tracker/calories_panel.html', {'form': form})

@csrf_exempt
@require_http_methods(["POST"])
def food_add(request):
    try:
        body = json.loads(request.body)
        name = body.get('name')
        calories = body.get('calories')
        date = body.get('date')
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    if not all([name, calories, date]):
        return JsonResponse({'error': 'Missing fields'}, status=400)

    try:
        entry = food.objects.create(
            name=name,
            calories=int(calories),
            date=datetime.strptime(date, '%Y-%m-%d').date()
        )
    except ValueError:
        return JsonResponse({'error': 'Invalid date format'}, status=400)

    return JsonResponse({
        'name': entry.name,
        'calories': entry.calories,
        'date': entry.date.strftime('%Y-%m-%d')
    })
    
@csrf_exempt
@require_http_methods(["POST"])
def food_delete(request):
    body = json.loads(request.body)
    signer = Signer()
    try:
        entry_id = signer.unsign(body.get('ref_token'))
        entry = get_object_or_404(food, pk=int(entry_id))
        entry.delete()
    except BadSignature:
        return JsonResponse({'error': 'Invalid token'}, status=403)
    
    return JsonResponse({'success': True})

def get_food_list_json(request):
    signer = Signer()
    data = []
    for entry in food.objects.all().order_by('-date', '-id').values('id', 'date', 'name', 'calories'):
        if entry['date'] == datetime.now().date():
            data.append({
                'date': entry['date'].strftime('%Y-%m-%d'),
                'name': entry['name'],
                'calories': entry['calories'],
                'ref_token': signer.sign(str(entry['id']))
            })
    return JsonResponse(data, safe=False)

def get_food_list_json_full(request):
    signer = Signer()
    data = []
    for entry in food.objects.all().order_by('-date', '-id').values('id', 'date', 'name', 'calories'):
        data.append({
            'date': entry['date'].strftime('%Y-%m-%d'),
            'name': entry['name'],
            'calories': entry['calories'],
            'ref_token': signer.sign(str(entry['id']))
        })
    return JsonResponse(data, safe=False)

#----------------------------------------------------------------------------------------------------------------

def hydration_panel(request):
    if request.method == 'POST':
        form = water_form(request.POST)
        if form.is_valid():
            water.objects.create(
                name = 'Water intake',
                amount = form.cleaned_data['amount'],
                time = datetime.now().time(),
                date = datetime.now().date()
            )
            return redirect('hydration_panel')
    else:
        form = water_form(initial={'amount': 0})

    return render(request, 'tracker/hydration_panel.html', {'form': form})

@csrf_exempt
@require_http_methods(["POST"])
def water_add(request):
    try:
        body = json.loads(request.body)
        name = body.get('name')
        amount = body.get('amount')
        time = body.get('time')
        date = body.get('date')
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    if not all ([amount, name, time, date]):
        return JsonResponse({'error': 'Missing fields'}, status=400)

    try:
        entry = water.objects.create(
            name = name,
            amount=int(amount),
            time=datetime.strptime(time, '%H:%M:%S').time(),
            date=datetime.strptime(date, '%Y-%m-%d').date()
        )
    except ValueError:
        return JsonResponse({'error': 'Invalid date format'}, status=400)

    return JsonResponse({
        'amount': entry.amount,
        'time': entry.time.strftime('%H:%M:%S'),
        'date': entry.date.strftime('%Y-%m-%d')
    })

@csrf_exempt
@require_http_methods(["POST"])
def water_delete(request):
    body = json.loads(request.body)
    signer = Signer()
    try:
        entry_id = signer.unsign(body.get('ref_token'))
        entry = get_object_or_404(water, pk=int(entry_id))
        entry.delete()
    except BadSignature:
        return JsonResponse({'error': 'Invalid token'}, status=403)
    
    return JsonResponse({'success': True})

def get_water_list_json(request):
    signer = Signer()
    data = []
    for entry in water.objects.all().order_by('-date', '-time', '-id').values('id', 'name', 'date', 'time', 'amount'):
        if entry['date'] == datetime.now().date():
            data.append({
                'date': entry['date'].strftime('%Y-%m-%d'),
                'time': entry['time'].strftime('%H:%M:%S'),
                'name': entry['name'],
                'amount': entry['amount'],
                'ref_token': signer.sign(str(entry['id']))
            })
    return JsonResponse(data, safe=False)

def get_water_list_json_full(request):
    signer = Signer()
    data = []
    for entry in water.objects.all().order_by('-date', '-time', '-id').values('id', 'name', 'date', 'time', 'amount'):
        data.append({
            'date': entry['date'].strftime('%Y-%m-%d'),
            'time': entry['time'].strftime('%H:%M:%S'),
            'name': entry['name'],
            'amount': entry['amount'],
            'ref_token': signer.sign(str(entry['id']))
        })
    return JsonResponse(data, safe=False)

#----------------------------------------------------------------------------------------------------------------

def medication_panel(request):
    medication = medication.objects.all()
    return render(request, 'tracker/medication.html', {'medication': medication})