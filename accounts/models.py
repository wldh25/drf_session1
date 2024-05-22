# accounts 폴더의 models.py
# user 모델은 결국 커스텀하게 되어 있기 때문에 나중에 커스텀 하더라도 커스텀 껍데기만 만들어놓고
# 첫 마이그레이션을 진행하는 것을 강력하게 추천

from django.db import models

from django.contrib.auth.models import AbstractUser, User

class User(AbstractUser):
    pass
