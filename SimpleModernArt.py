import numpy as np
import random
from collections import Counter


class SimpleModernArt(object):

    def __init__(self, player_size):
        self.base_info = {
            "player_size": player_size,
            "sell_price": [30, 20, 10],
            "total_paintings": [12, 13, 14, 15, 16],
            "unlisted_paintings": [12, 13, 14, 15, 16],
            "base_value": [0, 0, 0, 0, 0],
            "hand_will_receive": None,
            "remaining_round": 4,
            "hand_receive_per_round": [8, 3, 3, 0],
            "player": [{
                "id": i,
                "cash": 100,
                "hand": [],
                "purchased": []
            } for i in range(player_size)],
            "game_modifier": {
                "deal_evenly": False,
                "seed": 6
            }

        }
        self.base_info["hand_will_receive"] = initialize_hand(self.base_info)

    def auctuon(self, seller):
        painting = request_auction(seller)
        bid = []
        psize = len(self.base_info["player"])
        for priority in range(psize):
            bidder = (seller+priority+1) % psize
            bid.append((
                request_bid(painting, self.base_info["player"][bidder]["id"]),
                -priority,
                bidder
            ))
        print(bid)
        bid = list(sorted(bid, reverse=True))
        buyer = bid[0][2]
        return self.transaction(buyer, seller, bid[0][0], painting)

    def round_finish(self,):
        """
        ラウンド終了時の処理
        """
        self.base_info["remaining_round"] -= 1
        self.deal()
        return self.settle()

    def settle(self,):
        """
        購入カードの清算
        """
        purchased = []
        selp = self.base_info["sell_price"]
        for player in self.base_info["player"]:
            purchased.extend(player["purchased"])
        c = Counter(purchased)
        top = list(zip(*c.most_common(len(selp))))[0]
        print(top)
        payment = [0 for i in range(len(self.base_info["player"]))]
        for i in range(len(selp)):
            self.base_info["base_value"][top[i]] += selp[i]
            tmp = 0
            for player in self.base_info["player"]:
                while top[i] in player["purchased"]:
                    player["purchased"].remove(top[i])
                    player["cash"] += selp[i]
                    payment[tmp] += selp[i]
                tmp += 1

        for player in self.base_info["player"]:
            player["purchased"].clear()

        ret = "settle"
        for i in payment:
            ret += (" "+str(i))

        return ret

    def deal(self):
        """
        カードを配る
        """

        # 手札補充
        # print(self.base_info["hand_will_receive"][0])
        if self.base_info["hand_will_receive"][0] == []:
            print("a")
            return
        for player in range(self.base_info["player_size"]):
            self.base_info["player"][player]["hand"].extend(
                self.base_info["hand_will_receive"][player].pop(0))
            self.base_info["player"][player]["hand"] = sorted(
                self.base_info["player"][player]["hand"])
        return

    def transaction(self, buyer, seller, cost, painting):
        """
        取引成立時
        """
        if self.base_info["player"][buyer]["cash"] - cost <= 0:
            raise Exception("お金が足りません")
        if painting not in self.base_info["player"][seller]["hand"]:
            raise Exception("売る絵がありません")

        # 自分で購入
        if buyer == seller:
            self.base_info["player"][seller]["cash"] -= cost
            self.base_info["player"][seller]["hand"].remove(painting)
            self.base_info["player"][seller]["purchased"].append(painting)
            return "purchased "+agent(seller)+" "+agent(seller)+" "+str(painting)+" "+str(cost)

        # 普通の取引
        self.base_info["player"][buyer]["cash"] -= cost
        self.base_info["player"][buyer]["purchased"].append(painting)
        self.base_info["player"][seller]["cash"] += cost
        self.base_info["player"][seller]["hand"].remove(painting)
        return "purchased "+agent(seller)+" "+agent(buyer)+" "+str(painting)+" "+str(cost)


def agent(num):
    return "Agent["+"{0:02d}".format(num) + "]"


def request_auction(seller):
    """
    出品リクエスト
    """
    item = random.randint(0, 4)
    send("sell "+agent(seller)+" "+str(item))
    return item


def request_bid(item, bidder):
    """
    見積もりリクエスト
    """
    bid = random.randint(10, 13)
    send("bid " + agent(bidder)+" "+str(item)+" "+str(bid))
    return bid


def send(s):
    print("SEND:", s)
    return


def initialize_hand(info,):
    """
    手札の初期化
    """
    if sum(info["hand_receive_per_round"]) * info["player_size"] > sum(info["total_paintings"]):
        raise Exception("配布予定の絵が全体の枚数を超えています")
    if info["game_modifier"]["seed"] != None:
        np.random.seed(info["game_modifier"]["seed"])

    hand = [[] for i in range(info["player_size"])]
    paintings = []
    c = 0
    for i in info["total_paintings"]:
        paintings.extend([c]*i)
        c += 1

    if info["game_modifier"]["deal_evenly"]:

        pass
    else:
        np.random.shuffle(paintings)
    # print(paintings)

    for i in range(info["player_size"]):
        c = 0
        for j in info["hand_receive_per_round"]:
            hand[i].append(paintings[: j])
            paintings = paintings[j:]
            c += 1

    return hand


from pprint import pprint as pprint
s = SimpleModernArt(5)
s.deal()
# pprint(s.base_info)
"""
print(s.transaction(0, 1, 20, 0))
print(s.transaction(1, 2, 20, 1))
print(s.transaction(2, 3, 20, 2))
print(s.transaction(3, 4, 20, 2))
print(s.transaction(4, 0, 20, 1))
pprint(s.base_info)
print(s.round_finish())
pprint(s.base_info)
"""
print(s.auctuon(0))
pprint(s.base_info)
