from django.db import models


class ProfileModel(models.Model):
    id = models.AutoField(primary_key=True)
    profile_name = models.CharField(max_length = 20,default='SOME STRING')

    def __str__(self):
        return self.profile_name

class RecruitOverviewModel(models.Model):
    id = models.AutoField(primary_key=True)
    rank = models.CharField(max_length = 10,default='SOME STRING')
    percentile = models.PositiveIntegerField()
    average_rank = models.CharField(max_length = 10,default='SOME STRING')
    rank_evaluation = models.CharField(max_length = 10,default='SOME STRING')
    r_overview = models.ForeignKey(ProfileModel,related_name='overview',on_delete=models.CASCADE)

    def __str__(self):
            return self.rank_evaluation 

class RecruitSkillsModel(models.Model):
    id = models.AutoField(primary_key=True)
    skill = models.CharField(max_length = 20,default='SOME STRING')

    def __str__(self):
        return self.skill

class RecruitSkillsTypeModel(models.Model):
    id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length = 20,default='SOME STRING')
    skill_number = models.PositiveIntegerField()
    skill_t = models.ForeignKey(RecruitSkillsModel,related_name="skill_type",on_delete=models.CASCADE)
    def __str__(self):
        return self.skill_name

class FactorsModel(models.Model):
    reference_factors = models.CharField(max_length = 20,default='SOME STRING')
    def __str__(self):
        return self.reference_factors


    