from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def ordered(request):
    multiplePizzaForm = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, request.FILES)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk  = created_pizza.id
            note = "Thank for ordering your %s %s and %s pizza is on it's way" %(filled_form.cleaned_data['size'],            
            filled_form.cleaned_data['toppings1'],
            filled_form.cleaned_data['toppings2'])
            filled_form = PizzaForm()
        else:
            created_pizza_pk = None
            note = 'Pizza order has failed. Try again.'
        return render(request, "pizza/order.html",{'created_pizza_pk':created_pizza_pk,'pizzaform':filled_form, 'note': note,'multiplePizzaForm':multiplePizzaForm})
    else:
        form = PizzaForm()
        return render(request, "pizza/order.html",{'pizzaform':form,'multiplePizzaForm':multiplePizzaForm })

def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':    
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['toppings1'])
            note  = 'Pizza have been ordered'
        else:
            note = 'Ordered was not created'
        return render(request, 'pizza/pizzas.html', {'note':note, 'formset': formset})

    else:
        return render(request, 'pizza/pizzas.html', {'formset': formset})


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk = pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order has been updated'
            return render(request, 'pizza/edit_order.html', {'pizzaform': form, 'pizza':pizza,'note':note})
    return render(request, 'pizza/edit_order.html', {'pizzaform': form, 'pizza':pizza})
