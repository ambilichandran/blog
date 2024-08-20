from django import forms
from.models import Post
from django.forms import TextInput,FileInput,Textarea
class AddPost(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','image','content']
        widgets={
            'title':TextInput(
                attrs={
                  "class":"form-control",
                   "name":"title",
                   "type":"text", 
                   "placeholder":"Type ur title here"
                }
            ),
            'image':FileInput(
                attrs={
                    "name":"image",
                    "type":"file",
                    "class":"form-control"
                }
            ),
            'content':Textarea(
                attrs={
                    "name":"message",
                    "rows":"60",
                    "class":"form-control"
                }
            )
                
                    
                
            
            }