from django.db import models


NATIONALITY_CHOICES = (
    ('AMERICANA', 'Americana'),
    ('ISRAELENSE', 'Israelense'),
    ('BRITANICA', 'Britânica'),
    ('ESPANHOLA', 'Espanhola'),
    ('AUSTRALIANA', 'Australiana'),
    ('QUENIANA', 'Queniana'),
    ('CANADENSE', 'Canadense'),
    ('FRANCESA', 'Francesa'),
    ('MEXICANA', 'Mexicana'),
    ('ALEMA', 'Alemã'),
    ('SUL_AFRICANA', 'Sul-africana'),
    ('DINAMARQUESA', 'Dinamarquesa'),
    ('IRLANDESA', 'Irlandesa'),
    ('BRASILEIRA', 'Brasileira'),
    ('NEOZELANDESA', 'Neozelandesa'),
    ('JAPONESA', 'Japonesa'),
    ('ITALIANA', 'Italiana'),
    ('CUBANA', 'Cubana'),
    ('COREANA', 'Coreana'),
    ('CHINESA', 'Chinesa'),
    ('AUSTRIACA', 'Austríaca'),
    ('NIGERIANA', 'Nigeriana'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
