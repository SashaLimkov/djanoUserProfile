from api.utils.password_worker import generate_password_with_special_characters
from ninja import Router

from api.schema import  ProfileIn, ProfileDel
from api.utils.datetime_worker import get_datetime_from_string
from backend.models import Profile

profile_router = Router()


@profile_router.post("/")
def create_or_update_profile(request, payload: ProfileIn):
    print(request)
    payload_data = payload.dict()
    patient_number = payload_data.get("patient_number")
    if profile := Profile.objects.filter(patient_number=patient_number).first():
        for attr, value in payload.dict().items():
            if value == None:
                continue
            if attr in ["isFizikPerson", "dog1", "dog2", "isAmb"]:
                if value == "1":
                    setattr(profile, attr, True)
                else:
                    setattr(profile, attr, False)
            setattr(profile, attr, value)
        profile.save()
        return {"success": True}
    else:
        password = generate_password_with_special_characters(8)
        profile = Profile.objects.create(patient_number=patient_number, password=password)
        for attr, value in payload.dict().items():
            if value == None:
                continue
            if attr in ["isFizikPerson", "dog1", "dog2", "isAmb"]:
                if value == "1":
                    setattr(profile, attr, True)
                else:
                    setattr(profile, attr, False)
            setattr(profile, attr, value)
        profile.save()
        return {"password": password}

@profile_router.delete("/")
def create_or_update_profile(request, payload: ProfileDel):
    payload_data = payload.dict()
    print(payload_data)
    patient_number = payload_data.get("patient_number")
    profile = Profile.objects.filter(patient_number=patient_number).first()
    print(profile)
    profile.delete()
    return {"success": True}

@profile_router.post("/pass")
def create_or_update_profile(request, payload: ProfileDel):
    payload_data = payload.dict()
    patient_number = payload_data.get("patient_number")
    profile = Profile.objects.filter(patient_number=patient_number).first()
    password = generate_password_with_special_characters(8)
    profile.password = password
    profile.save()
    return {"password": password}