from django import forms

TUTORIAL_CATEGORIES = (
    ('article', 'article'),
    ('video', 'video'),
    ('course', 'course'),
    ('docs', 'docs'),
)


class TutorialForm(forms.Form):
    link = forms.URLField(label='Tutorial Link', max_length=100)
    category = forms.ChoiceField(choices=TUTORIAL_CATEGORIES)