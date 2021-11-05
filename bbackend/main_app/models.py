from django.db import models


class NavigationButtons(models.Model):
    name = models.CharField('текст кнопки', max_length=20, null=True, blank=True)
    action_click_display = models.ForeignKey('NavigationDisplay', verbose_name='ссылка на дисплей',
                                             on_delete=models.DO_NOTHING, null=True, blank=True)
    description = models.CharField('описание', max_length=250, null=True, blank=True)
    value = models.IntegerField('значение', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Кнопку'
        verbose_name_plural = 'Кнопки навигации'


class NavigationDisplay(models.Model):
    description = models.CharField('описание', max_length=250, null=True, blank=True)
    value = models.IntegerField('значение', null=True, blank=True)
    deep = models.IntegerField('глубина', null=True, blank=True)
    text = models.TextField('текст дисплея')
    text_mode = models.CharField('мод текста', max_length=15, default='HTML')
    buttons = models.ManyToManyField(NavigationButtons, verbose_name='набор кнопок', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, verbose_name='родительский дисплей', null=True,
                               blank=True)
    content = models.CharField('ссылка на контент', max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.description)

    class Meta:
        verbose_name = 'Дисплей'
        verbose_name_plural = 'Дисплеи'


class Content(models.Model):
    name = models.CharField('название (название кнопки)', max_length=250, null=True, blank=True)
    text = models.TextField('текст')
    category = models.ForeignKey('ContentCategory', on_delete=models.DO_NOTHING, verbose_name='категория контента')
 #   image = models.ImageField(pload_to='content')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'


class ContentCategory(models.Model):
    category = models.CharField('категория', max_length=200)

    def __str__(self):
        return str(self.category)

    class Meta:
        verbose_name = 'категория контента'
        verbose_name_plural = 'категории контента'
