from django.db import models
from django.contrib.auth.models import User

ANSWERS = [
    {
        'id': i,
        'text': f'Text {i}',
        'correct answer': 0,
        'likes': i + 5,
    }for i in range(30)
]

MEMBERS = [
    {
        'name': f'Name_{i}',
    }for i in range(9)
]
QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'text': f'Text {i}',
        'likes': i + 5,
        'tags': [f'Tag_{i}', f'Tag_{i+1}'],
    } for i in range(30)
]

class LikeManager(models.Manager):
    def get_question_likes_total(self, question):
        likes = question.common_content.like_set.all()
        count = 0
        for like in likes:
            if like.state:
                count += 1
            else:
                count -= 1
        return count
    def get_question_likes_totals(self, questions):
        likes = list()
        for question in questions:
            count = self.get_question_likes_total(question)
            likes.append(count)
        return likes


class Like(models.Model):
    common_content = models.ForeignKey(
        'CommonContent', on_delete=models.PROTECT)
    state = models.BooleanField()
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    objects = LikeManager()

    def __str__(self):
        if (self.state):
            like_state = '+1'
        else:
            like_state = '-1'
        return str(self.user) + ': ' + like_state

class TagManager(models.Manager):
    def get_questions_tags(self, questions):
        questions_tags = list()
        for question in questions:
            tags = question.tags.all()
            questions_tags.append(tags)
        return questions_tags

class Tag(models.Model):
    name = models.CharField(max_length=255)
    objects = TagManager()

    def __str__(self):
        return self.name


class CommonContent(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class QuestionManager(models.Manager):
    def get_tag(tag):
        return Question.objects.filter(tag__contains=tag)

class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    common_content = models.OneToOneField(
        'CommonContent', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    creation_date = models.DateTimeField(auto_now_add=True)
    objects = QuestionManager()

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    avatar = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return self.user.get_username()


class Answer(models.Model):
    content = models.TextField()
    correct = models.BooleanField(default=False)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    common_content = models.OneToOneField(
        'CommonContent', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:40]
