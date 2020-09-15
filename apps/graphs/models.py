from django.db import models


class Result(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    AuditID = models.CharField(max_length=45)
    RevisionNumber = models.CharField(max_length=45)
    FacilityName = models.CharField(max_length=100)
    FacilityID = models.CharField(max_length=45)
    Auditor1 = models.CharField(max_length=45)
    Auditor2 = models.CharField(max_length=45, null=True)
    Auditor3 = models.CharField(max_length=45, null=True)
    AuditDate = models.DateTimeField()
    RepDate = models.CharField(max_length=45)
    LinacModel = models.CharField(max_length=45)
    LinacManufacturer = models.CharField(max_length=45)
    PlanningSystemManufacturer = models.CharField(max_length=45)
    tps = models.CharField(max_length=45)
    Algorithm = models.CharField(max_length=45)
    kqFac = models.CharField(max_length=10)
    ACDS = models.CharField(max_length=10)
    Phantom = models.CharField(max_length=45)
    user = models.ForeignKey('auth.User', related_name='result', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class FacilityOutput(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    energy_6 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_10 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_15 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_18 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_6FFF = models.DecimalField(max_digits=6, decimal_places=3)
    energy_10FFF = models.DecimalField(max_digits=6, decimal_places=3)
    result = models.ForeignKey(Result, related_name='facilityOutput', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class TPR(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    energy_6 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_10 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_15 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_18 = models.DecimalField(max_digits=6, decimal_places=3)
    energy_6FFF = models.DecimalField(max_digits=6, decimal_places=3)
    energy_10FFF = models.DecimalField(max_digits=6, decimal_places=3)
    result = models.ForeignKey(Result, related_name='TPR', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Reading(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    Reading_101106 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_110106 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_205106 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_208106 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_205206 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_208206 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_205306 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_208306 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_303106 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_305106 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_403106 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_405106 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_103110 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_110110 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_303110 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_305110 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_403110 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_405110 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_103115 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_110115 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_303115 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_305115 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_403115 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_405115 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_103118 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_110118 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_303118 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_305118 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_403118 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_405118 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_101105 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_110105 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_303105 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_305105 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_103109 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_110109 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_303109 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    Reading_305109 = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    result = models.ForeignKey(Result, related_name='Reading', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Misdelivery(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    Misdelivery_101106 = models.SmallIntegerField(null=True)
    Misdelivery_110106 = models.SmallIntegerField(null=True)
    Misdelivery_205106 = models.SmallIntegerField(null=True)
    Misdelivery_208106 = models.SmallIntegerField(null=True)
    Misdelivery_205206 = models.SmallIntegerField(null=True)
    Misdelivery_208206 = models.SmallIntegerField(null=True)
    Misdelivery_205306 = models.SmallIntegerField(null=True)
    Misdelivery_208306 = models.SmallIntegerField(null=True)
    Misdelivery_303106 = models.SmallIntegerField(null=True)
    Misdelivery_305106 = models.SmallIntegerField(null=True)
    Misdelivery_403106 = models.SmallIntegerField(null=True)
    Misdelivery_405106 = models.SmallIntegerField(null=True)
    Misdelivery_103110 = models.SmallIntegerField(null=True)
    Misdelivery_110110 = models.SmallIntegerField(null=True)
    Misdelivery_303110 = models.SmallIntegerField(null=True)
    Misdelivery_305110 = models.SmallIntegerField(null=True)
    Misdelivery_403110 = models.SmallIntegerField(null=True)
    Misdelivery_405110 = models.SmallIntegerField(null=True)
    Misdelivery_103115 = models.SmallIntegerField(null=True)
    Misdelivery_110115 = models.SmallIntegerField(null=True)
    Misdelivery_303115 = models.SmallIntegerField(null=True)
    Misdelivery_305115 = models.SmallIntegerField(null=True)
    Misdelivery_403115 = models.SmallIntegerField(null=True)
    Misdelivery_405115 = models.SmallIntegerField(null=True)
    Misdelivery_103118 = models.SmallIntegerField(null=True)
    Misdelivery_110118 = models.SmallIntegerField(null=True)
    Misdelivery_303118 = models.SmallIntegerField(null=True)
    Misdelivery_305118 = models.SmallIntegerField(null=True)
    Misdelivery_403118 = models.SmallIntegerField(null=True)
    Misdelivery_405118 = models.SmallIntegerField(null=True)
    Misdelivery_101105 = models.SmallIntegerField(null=True)
    Misdelivery_110105 = models.SmallIntegerField(null=True)
    Misdelivery_303105 = models.SmallIntegerField(null=True)
    Misdelivery_305105 = models.SmallIntegerField(null=True)
    Misdelivery_103109 = models.SmallIntegerField(null=True)
    Misdelivery_110109 = models.SmallIntegerField(null=True)
    Misdelivery_303109 = models.SmallIntegerField(null=True)
    Misdelivery_305109 = models.SmallIntegerField(null=True)
    result = models.ForeignKey(Result, related_name='Misdelivery', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Graph(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=250)
    result = models.ManyToManyField('Result')

    class Meta:
        ordering = ['created']