# from django import forms
from django.forms import ModelForm
from mukbang.models import Muckbang
from django.utils.translation import gettext_lazy as _


# class PostForm(forms.Form):
#     title = forms.CharField(label='제목', max_length=20)
#     content = forms.CharField(label='내용', widget=forms.Textarea)

class Muckbangform(ModelForm):
    class Meta:
        model = Muckbang
        fields = ['group', 'name', 'tag', 'link', 'description', 'image']
        labels = {
            'group': _('그룹 선택'),
            'name': _('이름'),
            'tag': _('태그'),
            'link': _("유튜버 링크"),
            'image': _("대표 사진"),
            'description': _("그룹 설명"),
        }
        help_texts = {
            'group': _('어떤 그룹의 유튜버인가요.'),
            'name': _('이름을 적어주세요.'),
            'tag' : _('태그 입력해주세요.'),
            'link' : _("유튜버 링크"),
            'image' : _("대표 사진"),
            'description': _("그룹 설명을 적어주세요.")
        }
        widgets = {

        }
        error_messages = {
            'group': {
                'max_length': _("그룹이 너무 깁니다. 10자 이하로 해주세요.")
            },
            'name': {
                'max_length': _("이름이 너무 깁니다. 20자 이하로 해주세요.")
            },
            'tag': {
                'max_length': _("태그가 너무 깁니다. 20자 이하로 해주세요.")
            },
            'link': {
                'max_length': _("링크가 너무 깁니다. 100자 이하로 해주세요.")
            },
            'image': {
                'max_length': _("이미지가 너무 깁니다. 300자 이하로 해주세요.")
            },
            'description': {
                'max_length': _("설명이 너무 깁니다. 100자 이하로 해주세요.")
            },
        }