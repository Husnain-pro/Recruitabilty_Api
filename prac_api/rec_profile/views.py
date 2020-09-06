from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import (FactorsModel, ProfileModel, RecruitOverviewModel,
                     RecruitSkillsModel, RecruitSkillsTypeModel)
from .serializers import (FactorsSerializer, ProfileSerializer,
                          RecruitOverviewSerializer, RecruitSkillsSerializer,
                          RecruitSkillsTypeGetSerializer)





class ProfileView(generics.ListCreateAPIView):
    queryset = RecruitOverviewModel.objects.all()
    serializer_class = RecruitOverviewSerializer


class ProfileViewList(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecruitOverviewModel.objects.all()
    serializer_class = RecruitOverviewSerializer


class ProfileRecView(generics.ListCreateAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer


class ProfileRecViewList(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer



class RecruitOverview(generics.ListCreateAPIView):
    queryset = RecruitOverviewModel.objects.all()
    serializer_class = RecruitOverviewSerializer


class RecruitOverviewViewList(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecruitOverviewModel.objects.all()
    serializer_class = RecruitOverviewSerializer

class RecruitSkillsView(generics.ListCreateAPIView):
    queryset = RecruitSkillsModel.objects.all()
    serializer_class = RecruitSkillsSerializer



class FactorView(generics.ListCreateAPIView):
    queryset = FactorsModel.objects.all()
    serializer_class = FactorsSerializer


class FactorViewList(generics.RetrieveUpdateDestroyAPIView):
    queryset = FactorsModel.objects.all()
    serializer_class = FactorsSerializer



class SkillView(generics.ListCreateAPIView):
    queryset = RecruitSkillsTypeModel.objects.all()
    serializer_class = RecruitSkillsTypeGetSerializer


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecruitSkillsTypeModel.objects.all()
    serializer_class = RecruitSkillsTypeGetSerializer
