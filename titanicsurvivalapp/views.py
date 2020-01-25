from django.shortcuts import render
import pickle
import pandas as pd
from .forms import *
from django.contrib import messages
# Create your views here.

def home(request):
    titanic_model = pickle.load(open("titanic.pkl", "rb"))
    input_data = [[2.0, 18.0, 0.0, 1.0]]
    data = pd.DataFrame(input_data, columns=['Pclass','Age', 'Sex_female', 'Sex_male'])
    print(titanic_model.predict(data))
    return render(request, 'home.html')

def predict(request):
    if request.method == "GET":
        form = InputForm()
        return render(request, 'predict.html', {"form":form})
    if request.method == "POST":
        form = InputForm(request.POST)
        print(request.POST.get('gender'))
        if form.is_valid():
            Sex_female = 0
            Sex_male = 0
            if form['gender'].value() == 0:
                Sex_female = 1
            else:
                Sex_male = 1
            input_data = [[request.POST.get('passenger_class'), request.POST.get('age'), Sex_female, Sex_male ]]
            data = pd.DataFrame(input_data, columns=['Pclass','Age', 'Sex_female', 'Sex_male'])
            titanic_model = pickle.load(open("titanic.pkl", "rb"))
            result = titanic_model.predict(data)
            print(result)
            if result == 0:
                print("inside o")
                msg = "Sorry {} Cannot survive".format(request.POST.get('name'))
                messages.success(request, msg)
            if result == 1:
                print("inside 1")
                msg = "Good luck {}, survive".format(request.POST.get('name'))
                messages.success(request, msg)
            return render(request, 'predict.html', {"form":form})