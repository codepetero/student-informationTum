from django import forms
from . models import Feedback
from . models import Students
#from . models import Department



class feedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback

        fields =['feedback','feedback_reply', 'unit_name']
        widgets = {'student_id': forms.HiddenInput()}

class studentForm(forms.ModelForm):

    class Meta:
        model= Students

        fields ="__all__"

#class DepartmentForm(forms.ModelForm):

  #class Meta:
        #model= Department

        #fields="__all__"