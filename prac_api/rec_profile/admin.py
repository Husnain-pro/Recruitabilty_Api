from django.contrib import admin

from .models import (FactorsModel,ProfileModel, RecruitOverviewModel, RecruitSkillsModel,
                     RecruitSkillsTypeModel)

admin.register(ProfileModel, RecruitOverviewModel, RecruitSkillsModel,
               RecruitSkillsTypeModel,FactorsModel)(admin.ModelAdmin)
