import json


class Event:
    def __init__(self, timestamp, activity, case_id, sensor_name):
        self.timestamp = timestamp
        self.sensor_value: any = activity
        self.case_id: str = case_id
        self.sensor_name: str = sensor_name

    def __str__(self):
        return json.dumps(self.__dict__)
