# from django import forms
from django.forms import ModelForm
from mukbang.models import Muckbang
from django.utils.translation import gettext_lazy as _


# class PostForm(forms.Form):
#     title = forms.CharField(label='제목', max_length=20)
#     content = forms.CharField(label='내용', widget=forms.Textarea)

class Muckform(ModelForm):
    class Meta:
        model = Muckbang
        fields = ['group', 'name', 'tag', 'link', 'description', 'image']
        labels = {
            'group': _('그룹 선택'),
            'name': _('이름'),
            'tag' : _('태그'),
            'link' : _("유튜버 링크"),
            'image' : _("대표 사진"),
        }
        help_texts = {
            'group': _('어떤 그룹의 유튜버인가요.'),
            'name': _('이름을 적어주세요.'),
            'tag' : _('태그 입력해주세요.'),
            'link' : _("유튜버 링크"),
            'image' : _("대표 사진"),
        }
        error_messages = {
            'name': {
                'max_length': _("제목이 너무 깁니다. 30자 이하로 해주세요.")
            }
        }