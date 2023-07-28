import datetime


def get_datetime_from_string(dt: str):
    try:
        date_time_obj = datetime.datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S')
    except:
        date_time_obj = datetime.datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.%f')
    return date_time_obj
