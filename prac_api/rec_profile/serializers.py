from rest_framework import serializers
from .models import ProfileModel,FactorsModel,RecruitOverviewModel,RecruitSkillsTypeModel,RecruitSkillsModel


class RecruitOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitOverviewModel
        fields = ['id','rank', 'percentile', 'average_rank','rank_evaluation','r_overview']

    
class ProfileSerializer(serializers.ModelSerializer):
    overview = RecruitOverviewSerializer(many=True)
    class Meta:
        model = ProfileModel
        fields = ['id','profile_name','overview']

class RecruitSkillsSerializer(serializers.ModelSerializer):
    skill_type = serializers.StringRelatedField(many=True)

    class Meta:
        model = RecruitSkillsModel
        fields = ['id','skill','skill_type']

class RecruitSkillsTypeGetSerializer(serializers.ModelSerializer):

    # artist = ArtistListSerializer()

    class Meta:
         model = RecruitSkillsTypeModel
         fields = ['id','skill_name','skill_number','skill_t']

class FactorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactorsModel
        fields = ['id','reference_factors']
