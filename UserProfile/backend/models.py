from django.db import models


class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)


class Profile(TimeBasedModel):
    patient_number = models.CharField("ID пользователя в Лотусе", max_length=100, unique=True, blank=False, null=False)
    name_last = models.CharField("Фамилия", max_length=256)
    name_first = models.CharField("Имя", max_length=256)
    name_middle = models.CharField("Отчество", max_length=256)
    sex = models.CharField("Пол", max_length=20)
    bday = models.CharField("Дата рождения", max_length=20)
    doc_name = models.CharField("На основе какого документа", max_length=256)
    doc_series = models.CharField("Серия", max_length=64)
    doc_number = models.CharField("Номер", max_length=128)
    doc_agancy = models.CharField("Кем выдан", max_length=256)
    doc_date = models.CharField("Дата выдачи", max_length=20)
    address = models.CharField("Адрес", max_length=1024)
    phone1 = models.CharField("Номер телефона 1", max_length=36)
    phone2 = models.CharField("Номер телефона 1", max_length=36)
    email = models.CharField("Электронаня почта", max_length=128)
    polis = models.CharField("Полис", max_length=512)
    policlinika = models.CharField("Номер поликлиники в системе", max_length=32)
    isFizikPerson = models.BooleanField("Физ. лицо?")
    dog1 = models.BooleanField("договор 1")
    dog2 = models.BooleanField("договор 2")
    isAmb = models.BooleanField("Амбулаторный?")
    dms_num = models.CharField("ДМС номер", max_length=512)
    dms_org = models.CharField("ДМС организация", max_length=512)
    dms_inn = models.CharField("ДМС инн", max_length=512)
    password = models.CharField("Пароль", max_length=32)
