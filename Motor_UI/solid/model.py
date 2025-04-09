from typing import List

class Model():
    def __init__(self, name, label_list, value_list, movement):
        self.name = name
        self.label_list : List[str] = label_list
        self.value_list : List[str] = value_list
        self.movement : float = movement
        self.distance : float = 0.0

    def calculate_distance(self,input_distance) -> str | int:
        '''
        이동거리 계산
        '''
        now = self.distance
        _cw = ""
        r_distance = 0
        if self.distance > input_distance:
            r_distance = now - input_distance
            _cw = 'U'
        elif self.distance < input_distance:
            r_distance = input_distance - now
            _cw = 'D'
        elif now == input_distance or now == 0:
            return
        return _cw, int(r_distance)
    
    def update_distance(self, direction: str) -> None | bool:
        '''
        이동거리 업데이트
        '''
        if direction == "U":
            self.distance -= self.movement
        elif direction == "D":
            self.distance += self.movement
        else:
            return False
