from django.db import models


class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)


class Profile(TimeBasedModel):
    patient_number = models.CharField("ID пользователя в Лотусе", max_length=100, unique=True, blank=False, null=False)
    name_last = models.CharField("Фамилия", max_length=256, blank=True, null=True)
    name_first = models.CharField("Имя", max_length=256, blank=True, null=True)
    name_middle = models.CharField("Отчество", max_length=256, blank=True, null=True)
    sex = models.CharField("Пол", max_length=20, blank=True, null=True)
    bday = models.CharField("Дата рождения", max_length=20, blank=True, null=True)
    doc_name = models.CharField("На основе какого документа", max_length=256, blank=True, null=True)
    doc_series = models.CharField("Серия", max_length=64, blank=True, null=True)
    doc_number = models.CharField("Номер", max_length=128, blank=True, null=True)
    doc_agancy = models.CharField("Кем выдан", max_length=256, blank=True, null=True)
    doc_date = models.CharField("Дата выдачи", max_length=20, blank=True, null=True)
    address = models.CharField("Адрес", max_length=1024, blank=True, null=True)
    phone1 = models.CharField("Номер телефона 1", max_length=36, blank=True, null=True)
    phone2 = models.CharField("Номер телефона 1", max_length=36, blank=True, null=True)
    email = models.CharField("Электронаня почта", max_length=128, blank=True, null=True)
    polis = models.CharField("Полис", max_length=512, blank=True, null=True)
    policlinika = models.CharField("Номер поликлиники в системе", max_length=32, blank=True, null=True)
    isFizikPerson = models.BooleanField("Физ. лицо?", blank=True, null=True)
    dog1 = models.BooleanField("договор 1", blank=True, null=True)
    dog2 = models.BooleanField("договор 2", blank=True, null=True)
    isAmb = models.BooleanField("Амбулаторный?", blank=True, null=True)
    dms_num = models.CharField("ДМС номер", max_length=512, blank=True, null=True)
    dms_org = models.CharField("ДМС организация", max_length=512, blank=True, null=True)
    dms_inn = models.CharField("ДМС инн", max_length=512, blank=True, null=True)
    password = models.CharField("Пароль", max_length=32, blank=True, null=True)
