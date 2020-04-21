from django.db import models
from stdimage.models import StdImageField

class Base(models.Model):
    created = models.DateTimeField('Criação', auto_now_add=True)
    modified = models.DateTimeField('Atualizado', auto_now=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Service(Base):
    ICON_CHOICES = {
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    }
    service = models.CharField('Serviço', max_length=100)
    description = models.TextField('Descrição', max_length=200)
    icon = models.CharField('Icone', max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.service

class Role(Base):
    role = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.role

class Employee(Base):
    name = models.CharField('Nome', max_length=100)
    role = models.ForeignKey('core.Role', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    image = StdImageField('Imagem', upload_to='team', variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.name