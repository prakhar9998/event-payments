from django.forms import ModelForm
from paytm.models import PlayersInfo

class PlayersInfoForm(ModelForm):
    class Meta:
        model = PlayersInfo
        fields = [
            'team_leader_fullname',
            'leader_username',
            'participant_1',
            'participant_2',
            'participant_3',
            'contact_no',
        ]