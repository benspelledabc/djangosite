from django.db import models
from datetime import date


class MommaPhoto(models.Model):
    momma_shot = models.ImageField(upload_to='uploads/puppy_fostering/', null=True, blank=True)
    photo_date = models.DateField(default=date.today)

    def __str__(self):
        return "%s - %s - %s" % (self.id, self.photo_date, self.momma_shot.url)

    class Meta:
        ordering = ('-photo_date', '-id')


class Momma(models.Model):
    nickname = models.CharField(max_length=150, default=None, blank=True, null=True)
    momma_photos = models.ManyToManyField(MommaPhoto, blank=True)
    note = models.TextField(blank=True, null=True)  # i like big comments...

    def __str__(self):
        return "%s" % self.nickname

    class Meta:
        ordering = ('nickname', 'id')
        verbose_name = 'Momma'
        verbose_name_plural = 'Mommas'


class Puppy(models.Model):
    momma = models.ForeignKey(Momma, on_delete=models.CASCADE, null=True, blank=True)
    nickname = models.CharField(max_length=150, default='Unnamed Puppy')
    birth_date = models.DateField(default=date.today)

    MALE = 'Male'
    FEMALE = 'Female'

    puppy_sex_choices = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    sex = models.CharField(
        max_length=20,
        choices=puppy_sex_choices,
        default=MALE,
    )

    def __str__(self):
        return "%s - %s" % (self.momma, self.nickname)

    class Meta:
        ordering = ('momma__nickname', 'nickname', 'id')
        verbose_name = 'Puppy'
        verbose_name_plural = 'Puppies'


class PuppyNotes(models.Model):
    puppy = models.ForeignKey(Puppy, on_delete=models.CASCADE, null=True, blank=True)
    note_date = models.DateField(default=date.today)
    puppy_shot = models.ImageField(upload_to='uploads/puppy_fostering/', null=True, blank=True)
    note = models.TextField(blank=True, null=True)  # i like big comments...

    def __str__(self):
        return "%s - %s" % (self.puppy, self.note_date)

    class Meta:
        ordering = ('puppy', 'note_date')
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
