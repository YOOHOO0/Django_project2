from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200) # 글자수를 제한하고 싶은 데이터는 Charfield 사용
    content = models.TextField() # 글자수 제한이 없는 데이터는 TextField 사용
    create_date = models.DateTimeField(); # 날짜, 시간 관련 데이터는 DateTimeField 사용

class Answer(models.Model):
    # 어떤 모델이 다른 모델을 속성으로 가지면 Forignkey 사용 (다른 모델과의 연결을 의미)
    # 질문이 삭제되면 답변도 삭제 : on_delete=models.CASCADE
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    creat_date = models.DateTimeField()