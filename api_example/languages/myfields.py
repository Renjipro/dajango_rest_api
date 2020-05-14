import jsonfield

class MyJsonField(jsonfield.JSONField):
    def get_prep_value(self, value):
        if isinstance(value, str):
            return value
        return super(MyJsonField,self).get_prep_value(value)