# Create your models here.
import datetime
from typing import Optional

from ninja import ModelSchema, Schema






class ProfileIn(Schema):
    patient_number:str
    name_last:str = None
    name_first:str = None
    name_middle:str = None
    sex:str = None
    bday:str = None
    doc_name:str = None
    doc_series:str = None
    doc_number:str = None
    doc_agancy:str = None
    doc_date:str = None
    address:str = None
    phone1:str = None
    phone2:str = None
    email:str = None
    polis:str = None
    policlinika:str = None
    isFizikPerson:bool = None
    dog1:bool = None
    dog2:bool = None
    isAmb:bool = None
    dms_num:str = None
    dms_org:str = None
    dms_inn:str = None



class Error(Schema):
    message: str
