from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_one_to_ten_range, validate_title_year


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    CHOICES = [
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (USER, 'Пользователь'),
    ]
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        unique=True,
    )
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
    )
    role = models.CharField(
        max_length=16,
        choices=CHOICES,
        default='user'
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_user(self):
        return self.role == self.USER

    class Meta:
        ordering = ('username',)


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.slug

    class Meta:
        ordering = ('name',)


class Title(models.Model):
    name = models.CharField(max_length=255, blank=False)
    rating = models.PositiveSmallIntegerField(
        default=None,
        validators=[validate_one_to_ten_range],
        null=True,
        verbose_name='Рейтинг',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        help_text='Введите категорию произведения',
        null=True,
        related_name='category'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    genre = models.ManyToManyField(
        Genre, through='TitleGenre', verbose_name='Жанр'
    )
    year = models.IntegerField(
        'Год релиза',
        help_text='Введите год релиза',
        null=True,
        validators=[validate_title_year],
    )

    class Meta:
        ordering = (
            '-rating',
            'name',
        )
        verbose_name = 'Произведение'
        verbose_name_plural = 'произведения'

    def __str__(self):
        return f"{self.name[:15]}"


class TitleGenre(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.genre}"


class Review(models.Model):
    text = models.TextField(
        help_text='введите текст отзыва',
        verbose_name='текст отзыва'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='введите произведения',
        verbose_name='Произведения'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        help_text='введите дату публикации ',
        verbose_name='дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='введите автора',
        verbose_name='Автор'
    )
    score = models.IntegerField(
        validators=[validate_one_to_ten_range],
        blank=False,
        null=False,
        help_text='укажите оценку произведения',
        verbose_name='оценка'
    )

    class Meta:
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'], name='unique review'
            ),
        ]

    def __str__(self):
        return f"{self.text[:15]}"

    def recalculate_rating(self, *args, **kwargs):
        """Рассчитывает значение рейтинга как среднее арифметическое значений
        поля 'score' в обзорах, написанных для данного произведения, если
        обзоров у произведения нет, устанавливает рейтинг равный None"""

        query_review = Review.objects.filter(title=self.title)
        title = self.title
        if len(query_review) == 0:
            title.rating = None
            title.save()
            return
        rating = query_review.aggregate(models.Avg("score"))["score__avg"]
        title.rating = round(rating)
        title.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.recalculate_rating(self)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.recalculate_rating(self)


class Comment(models.Model):
    review = models.ForeignKey(
        'Review',
        on_delete=models.CASCADE,
        related_name='comments',
        help_text='введите отзыв',
        verbose_name='Отзыв',
    )
    text = models.TextField(
        help_text='введите текст комментария',
        verbose_name='текст комментария')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        help_text='введите дату публикации ',
        verbose_name='дата публикации')
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='comments',
        help_text='введите автора',
        verbose_name='Автор',
    )

    class Meta:
        ordering = ('-pub_date',)
