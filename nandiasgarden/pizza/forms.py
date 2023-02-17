from django import forms
from .models import Pizza, Size
# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label = 'Topping 1', max_length = 100, widget=forms.PasswordInput)
#     topping2 = forms.CharField(label = 'Topping 2', max_length = 100)
#     size = forms.ChoiceField(label = 'Size', choices=[('Small','Small'),('Large','Large'),('Medium', 'Medium')])    

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['toppings1','toppings2','size']
        labels = {'toppings1': 'Topping 1','toppings2': 'Topping 2'}

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2,max_value=6)
