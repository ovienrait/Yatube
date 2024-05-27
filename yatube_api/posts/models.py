from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель для категорий публикаций"""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Группа'

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель для публикаций"""

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Публикация'
        default_related_name = 'posts'

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель для комментариев к публикациям"""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Комментарий'
        default_related_name = 'comments'

    def __str__(self):
        return self.text[:20]


class Follow(models.Model):
    """Модель для подписок"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followings')

    class Meta:
        verbose_name = 'Подписки'
        constraints = (models.UniqueConstraint(
            fields=('user', 'following'),
            name='unique_follow'
        ),)

    def __str__(self):
        return self.user
