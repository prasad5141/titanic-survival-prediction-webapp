from django.shortcuts import render
import pickle
import pandas as pd
from .forms import *

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
        if form.is_valid():
            print(form['gender'].value())
        return render(request, 'predict.html')