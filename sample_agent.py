import simplemodernpy.Client as client
from time import sleep

class Agent(object):

    def initialize(self,info):
        """
        ゲーム開始時に呼ばれる
        __init__ではない
        """
        print(info)
        return

    def purchase(self,purchase,info):
        """
        購入が成立した時に呼ばれる
        purchaseには買い手、絵、価格、売り手
        """
        print(purchase)
        #print(info)
        return

    def sell(self,info):
        """
        自分が出品する番になったら呼ばれる
        絵の番号を返せば良い
        手札にない番号を指定するとランダムで勝手に出品される
        """
        #print(info)
        sleep(1)
        return 0

    def bid(self,item,info):
        """
        入札する時に呼ばれる
        入札価格を返せば良い
        itemは購入する絵
        所持金を超える入札は所持金と同額にクランプされる
        """
        print(item)
        sleep(1)
        return 0
        
    def roundover(self,payment,info):
        """
        ラウンド終了時に呼ばれる
        """
        print(payment)
        return

    def finish(self,info):
        """
        ゲーム終了時に呼ばれる
        ここで得られるinfoには全てのゲームデータが格納されている
        """
        print(info)
        return

agent=Agent()

# run
if __name__ == '__main__':
    client.connect(agent)