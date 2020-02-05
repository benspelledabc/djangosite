from django.db import models
from decimal import Decimal


class Caliber(models.Model):
    name = models.CharField(max_length=150)
    diameter = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)


class Firearm(models.Model):
    manufacture = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    barrel_length = models.DecimalField(max_digits=5, decimal_places=1, default=18.0, null=True)
    extra_info = models.TextField(blank=True, null=True)  # i like big comments...
    caliber = models.ForeignKey(Caliber, related_name='Caliber', on_delete=models.CASCADE)

    # todo: Add 'owner' to class to track owner based off userid drop down menu?

    def __str__(self):
        return "%s %s %s" % (self.manufacture, self.model, self.caliber)

    class Meta:
        ordering = ('manufacture', 'model')


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
    powder = models.ForeignKey(Powder, default=1, on_delete=models.CASCADE)
    firearm = models.ForeignKey(Firearm, related_name='firearm', on_delete=models.CASCADE, null=True)
    projectile = models.ForeignKey(Projectile, related_name='bullet', on_delete=models.CASCADE)
    Powder_Charge = models.DecimalField(max_digits=5, decimal_places=1)
    # todo: removed chamber per added 'firearm' class
    # Chamber = models.CharField(max_length=150, default=None, blank=True, null=True)
    Velocity = models.IntegerField(default=1200, null=True)
    # Barrel_Length = models.DecimalField(max_digits=5, decimal_places=1, default=18.0, null=True)
    Is_Shamus_OCW = models.BooleanField(default=True)
    Is_Sven_OCW = models.BooleanField(default=True)
    Is_Sheriff_Load = models.BooleanField(default=True)

    def __str__(self):
        return "[PK: %s] %s (%sgr %s %s {%s [%sgr of %s]})" % (self.pk, self.firearm.caliber,
                                                               self.projectile.WeightGR,
                                                               self.projectile.Manufacture,
                                                               self.projectile.Name,
                                                               self.Velocity,
                                                               self.Powder_Charge,
                                                               self.powder.name,
                                                               )

    class Meta:
        ordering = ('firearm', '-projectile', '-Velocity')


class EstimatedDope(models.Model):
    hand_load = models.ForeignKey(HandLoad, default=1, on_delete=models.CASCADE)
    moa_100 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_125 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_150 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_175 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_200 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_225 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_250 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_275 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_300 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_325 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_350 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_375 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_400 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_425 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_450 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_475 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_500 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_525 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_550 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_575 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_600 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_625 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_650 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_675 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_700 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_725 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_750 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_775 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_800 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_825 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_850 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_875 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_900 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_925 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_950 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_975 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_1000 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_1025 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_1050 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))
    moa_1075 = models.DecimalField(max_digits=4, decimal_places=1, default=Decimal('0.0'))

    def __str__(self):
        return str(self.hand_load)
