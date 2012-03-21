from django.forms import ModelForm
from twitter_auth.models import movie_dataset


class StoreTweetsForm(ModelForm):
	class Meta:
		model = movie_dataset
