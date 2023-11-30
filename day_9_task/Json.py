import json
class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def to_json(self):
        return json.dumps({'name':self._name,'age':self._age},indent=4)
    def from_json(self,data):
        return json.loads(data)

person=Person("Ram",10)
json_value=person.to_json()
print(f"Json Value is:{json_value}")
person_data=person.from_json(json_value)
print(f"Actual Data is:{person_data}")