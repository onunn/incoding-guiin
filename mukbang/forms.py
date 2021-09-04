# from django import forms
from django.forms import ModelForm
from django import forms
from mukbang.models import Muckbang, Group
from django.utils.translation import gettext_lazy as _


# class PostForm(forms.Form):
#     title = forms.CharField(label='제목', max_length=20)
#     content = forms.CharField(label='내용', widget=forms.Textarea)

class Muckbangform(ModelForm):
    class Meta:
        model = Muckbang
        fields = ['group','name', 'tag', 'link', 'image']
        labels = {
            # 'group': _('속한 그룹'),
            'name': _('이름'),
            'tag' : _('태그'),
            'link' : _("유튜버 링크"),
            'image' : _("대표 사진"),
        }
        help_texts = {
            # 'group': _('속할 그룹을 적어주세요.'),
            'name': _('이름을 적어주세요.'),
            'tag' : _('태그 입력해주세요.'),
            'link' : _("유튜버 링크"),
            'image' : _("대표 사진"),
        }
        error_messages = {
            'name': {
                'max_length': _("이름은 20자 이내로 해주세요")
            },
            'tag' : {
                'max_length' : _("이름은 20자 이내로 해주세요")
            },

        }
        widgets = {
            'group': forms.HiddenInput(),
        }

class Groupform(ModelForm) :
    class meta :
        model = Group
        field = ['group_classifier', 'description']
        label = {
            'group_classifier': _('그룹명'),
            'description' : _('그룹 설명'),
        }
        help_texts = {
            'group_classifier': _('속할 그룹을 적어주세요.'),
            'description': _('그룹 설명을 적어주세요.'),
        }
        error_messages = {
            'group_classifier': {
                'max_length' :  _("그룹 이름은 2자 이내로 해주세요")
            },
        }