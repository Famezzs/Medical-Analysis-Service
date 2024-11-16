from module.data.entity.Illness import Illness
from module.abstract.Converter import Converter

class IllnessesToArrayConverter(Converter):
    def convert(self, to_convert):
        illnesses_array = []
        for illness in to_convert:
            illnesses_array.append({
                "name": illness.name,
                "description": illness.description
            })
        return illnesses_array