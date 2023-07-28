from api.utils.password_worker import generate_password_with_special_characters
from ninja import Router

from api.schema import  ProfileIn
from api.utils.datetime_worker import get_datetime_from_string
from backend.models import Profile

profile_router = Router()


@profile_router.post("/")
def create_or_update_profile(request, payload: ProfileIn):
    payload_data = payload.dict()
    print(payload_data)
    patient_number = payload_data.get("patient_number")
    if profile := Profile.objects.filter(patient_number=patient_number).first():
        for attr, value in payload.dict().items():
            if value == None:
                continue
            setattr(profile, attr, value)
        profile.save()
        return {"success": True}
    else:
        password = generate_password_with_special_characters(8)
        profile = Profile.objects.create(**payload.dict(), password=password)
        return {"password": password}

