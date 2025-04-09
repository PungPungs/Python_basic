import os

class TxtManager:
    def __init__(self, base_path='.\\record'):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)

    def load(self, model : str) -> float:
        '''
        txt 파일에서 이동거리 불러오기
        '''
        path = os.path.join(self.base_path,model + ".txt")
        try:
            with open(path,'x') as txt:
                if txt.readable():
                    distance = float(txt.read())
                else:
                    distance = 0
            return distance
        except Exception as e:
            print(e)
            return False

    def save(self, model : str, distance : float):
        '''
        txt 파일에 이동거리 저장
        '''
        path = os.path.join(self.base_path,model + ".txt")
        try:
            with open(path,'w') as txt:
                    txt.write(str(distance))
        except Exception as e:
            return e