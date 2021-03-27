from crudapp.models import Student
from django import forms
from crudapp.models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fullname','mobile','roll_no','course')
        labels = {'fullname':'full_name','roll_no':'Roll No'}
    def __init__(self,*args,**kwargs):
        super(StudentForm,self).__init__(*args,**kwargs)
        self.fields["course"].empty_label = "select"
        self.fields['roll_no'].required = False