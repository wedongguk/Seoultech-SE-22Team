import random

class pile: # pile 클래스 생성
    cardList = []

    def __init__(self, cardList = []): # player 클래스 생성자
        self.cardList = cardList.copy()

    def __del__(self): # player class 소멸자
        pass
    
    def shuffle(self): # pile의 카드를 섞습니다.
        random.shuffle(self.cardList)
        
    def takeTopCard(self): # 가장 위의 카드를 가져옵니다.
        result = self.cardList.pop()
        
        return result
    
    def __add__(self, op_2): # pile_2의 카드를 전부 옮깁니다.
        for i in op_2:
            self.cardList.append(i)
        op_2.clear() # 카드 옮겼으니 전부 지움
        
    def printlist(self):
        lst = [x.info() for x in self.cardList]
        return lst