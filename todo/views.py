from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext # For CSRF
#from django.forms.formsets import formset_factory, BaseFormSet
from django.forms.models import modelformset_factory, BaseModelFormSet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from forms import *

# This class is used to make empty formset forms required
# See http://stackoverflow.com/questions/2406537/django-formsets-make-first-required/4951032#4951032
class RequiredFormset(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormset, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False

def index(request):
    """Shows all the todo lists in the system"""
    # For CSRF protection
    # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/ 
    c = {
    	 'lists': List.objects.all(),
        }
    c.update(csrf(request))
    
    return render_to_response('index.html', c)

def edit_items_in_list(request, pk):
    """Shows the todo items in a list and allows you to edit them"""
    
    l = get_object_or_404(List, pk=pk)

    # Display one empty form if there are no items already in existence
    if Item.objects.count():
        # No need to have an extra form, as the client-side JavaScript will allow for adding new items
        no_of_forms = 0
    else:
        no_of_forms = 1
        
    # You can use a formset_factory, which allows you to use _forms_
    # (and forms allow for a lot of customisability)
    ItemFormset = modelformset_factory(Item, can_delete=True, max_num=6, extra=no_of_forms, exclude=('list',))#, formset=RequiredFormset)

    if request.method == 'POST': # If the form has been submitted...
        # Create a formset from the submitted data
        #print request.POST
        formset = ItemFormset(request.POST, request.FILES)
        
        #print formset.empty_form
        
#        print "---------"
#        print formset
        
        if formset.is_valid():
            print "Formset is bloody valid"
            
            # Save only changed instances
            # See: https://docs.djangoproject.com/en/1.4/topics/forms/modelforms/#saving-objects-in-the-formset
            instances = formset.save(commit=False)
            
            for instance in instances:
                print instance.name
                instance.list = l
                instance.save()
            
#            for form in formset:
#                form.save()

            return HttpResponseRedirect('thanks') # Redirect to a 'success' page
        else:
            print "Formset AIN'T VALID"
            print formset.errors
        
    else:
        #todo_list_form = ListForm()
        formset = ItemFormset(queryset=l.item_set.all())
    
    # For CSRF protection
    # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/ 
    c = {
    	 'list': l,
         'formset': formset,
         'origin_item': formset.empty_form,
        }
    c.update(csrf(request))
    
    return render_to_response('edit_items_in_list.html', c)