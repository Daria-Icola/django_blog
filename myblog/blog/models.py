from django.db import models


class PostBlog(models.Model):
    '''Шаблон записи в блог'''
    title = models.CharField("Заголовок записи", max_length=100)
    descriptions = models.TextField("Текст записи")
    author = models.CharField("Имя автора", max_length=100)
    date = models.DateField("Дата публикации")
    img = models.ImageField('Изображение', upload_to='image/%Y')

    def __str__(self):
        return f"{self.title}, {self.author}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


