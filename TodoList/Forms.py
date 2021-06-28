from django.forms import ModelForm
from TodoList.models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'important', 'due_time', 'due_date', 'tags']
