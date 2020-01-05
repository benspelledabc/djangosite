from django.db import models


class Powder(models.Model):
    name = models.CharField(max_length=150, default=None, blank=True, null=True)
    is_smokeless = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name', 'is_smokeless')


class Projectile(models.Model):
    Manufacture = models.CharField(max_length=150, default=None, blank=True, null=True)
    Name = models.CharField(max_length=150, default=None, blank=True, null=True)
    WeightGR = models.DecimalField(max_digits=5, decimal_places=1)
    Diameter = models.DecimalField(max_digits=5, decimal_places=3)
    Ballistic_Coefficient = models.DecimalField(max_digits=5, decimal_places=4, default=0.24)

    def __str__(self):
        return "%s %s %s" % (self.WeightGR, self.Manufacture, self.Name)

    class Meta:
        ordering = ('WeightGR', 'Manufacture')


class HandLoad(models.Model):
    # powder = models.CharField(max_length=30, choices=POWDER_CHOICES, default="UNLISTED")
    powder = models.ForeignKey(Powder, default=1, on_delete=models.CASCADE)

    projectile = models.ForeignKey(Projectile, related_name='bullet', on_delete=models.CASCADE)
    Powder_Charge = models.DecimalField(max_digits=5, decimal_places=1)
    Chamber = models.CharField(max_length=150, default=None, blank=True, null=True)
    Velocity = models.IntegerField(default=1200, null=True)
    Barrel_Length = models.DecimalField(max_digits=5, decimal_places=1, default=18.0, null=True)
    Is_Shamus_OCW = models.BooleanField(default=True)
    Is_Sven_OCW = models.BooleanField(default=True)
    Is_Sheriff_Load = models.BooleanField(default=True)

    def __str__(self):
        return "%s (%sgr %s %s {%s [%sgr of %s]})" % (self.Chamber,
                                                      self.projectile.WeightGR,
                                                      self.projectile.Manufacture,
                                                      self.projectile.Name,
                                                      self.Velocity,
                                                      self.Powder_Charge,
                                                      self.powder.name,
                                                      )

    class Meta:
        ordering = ('Chamber', '-projectile', '-Velocity')
