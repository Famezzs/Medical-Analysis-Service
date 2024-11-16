from module.data.entity.Illness import Illness

class IllnessesToArray():
    @staticmethod
    def convert_list(illnesses_list):
        illnesses_array = []
        for illness in illnesses_list:
            illnesses_array.append({
                "name": illness.name,
                "description": illness.description
            })
        return illnesses_array