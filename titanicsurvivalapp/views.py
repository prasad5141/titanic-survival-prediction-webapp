from django.shortcuts import render
import pickle
import pandas as pd
from .forms import *
from django.contrib import messages
from .models import *
# Create your views here.

def home(request):
    titanic_model = pickle.load(open("titanic.pkl", "rb"))
    input_data = [[2.0, 18.0, 0.0, 1.0]]
    data = pd.DataFrame(input_data, columns=['Pclass','Age', 'Sex_female', 'Sex_male'])
    print(titanic_model.predict(data))
    return render(request, 'home.html')

def predict(request):
    print(request.method)
    if request.method == "GET":
        form = InputForm()
        history = History.objects.all()
        return render(request, 'predict.html', {"form":form, 'history':history})
    if request.method == "POST":
        form = InputForm(request.POST)
        print(request.POST.get('gender'))
        print(request.POST.get('age'))
        print(request.POST.get('name'))
        print(request.POST.get('passenger_class'))
        if form.is_valid():
            print('inside valid form')
            Sex_female = 0
            Sex_male = 0
            print(type(form['gender'].value()))
            if form['gender'].value() == 'Female':
                Sex_female = 1
            else:
                Sex_male = 1

            if form['passenger_class'].value() == 'Class 1':
                Pclass = 1
            elif form['passenger_class'].value() == 'Class 2':
                Pclass = 2
            else:
                Pclass = 3
            input_data = [Pclass, request.POST.get('age'), Sex_female, Sex_male ]
            h = History.objects.create(name=request.POST.get('name'), age=request.POST.get('age'), passenger_class=int(request.POST.get('passenger_class')), gender=form['gender'].value())
            print(input_data)
            data = pd.Series(input_data, index=['Pclass','Age', 'Sex_female', 'Sex_male'])
            print(data)
            titanic_model = pickle.load(open("random_forest_titanic.pkl", "rb"))
            result = titanic_model.predict([data])
            print(result)
            h.survived = result
            if result == 0:
                print("inside o")
                msg = "Sorry {} Cannot survive".format(request.POST.get('name'))
                messages.success(request, msg)
                h.survived = False
            if result == 1:
                print("inside 1")
                msg = "Good luck {}, survive".format(request.POST.get('name'))
                messages.success(request, msg)
                h.survived = True
            h.save()
            history = History.objects.all()
            # context = {
            #     "history":history
            # }
            return render(request, 'predict.html', {"form":form, 'history':history})