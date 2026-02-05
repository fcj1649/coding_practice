file = open('.\\ProjectEuler\\proj_euler_54_poker.txt', 'r')

def poker_get_hand_score(hand_suit: dict, hand_numb:dict):
    pl_score = -1
    hand_suit_list = list(hand_suit.values())
    hand_numb_list = list(hand_numb.values())

    #check if its straight
    first_num = hand_numb_list

    if(5 in hand_suit_list):
        check = True
        for i in range(10,16):
            if(hand_numb_list[i]==0):
                check = False
        if(check):
            #royal flush
            pl_score = 10
        else:
            #straight flush
            check_str = True
            first_num = hand_numb_list.index(1)
            if(first_num >= 10):
                check_str = False
            else:
                for j in range(first_num, first_num+5):
                    if(hand_numb_list[j]==0):
                        check_str = False
                        break

            if(check_str):
                pl_score = 9
            else:
                pl_score = 6

    if(pl_score != 10 and pl_score != 9):
        # normal flush or no flush
        if (4 in hand_numb_list):
            # check 4 of a kind
            pl_score = 8
        elif(3 in hand_numb_list and 2 in hand_numb_list):
            #full house
            pl_score = 7
        elif(pl_score == 6):
            #nothing better than flush
            pass
        else:
            # first check straight
            pass


    
    return pl_score


def poker_check_winner(hand1: list, hand2: list):
    #check if hand1 wins then return true else return false
    #assumption one hand wins out of hand1 and hand2
    hand1_suit = {"S":0, "C": 0, "D": 0, "H": 0}
    hand1_numb = {"0": 0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "T":0, "J":0, "Q":0, "K":0, "A":0 }

    hand2_suit = {"S":0, "C": 0, "D": 0, "H": 0}
    hand2_numb = {"0": 0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "T":0, "J":0, "Q":0, "K":0, "A":0 }    

    for card in hand1:
        hand1_suit[card[1]] = hand1_suit[card[1]] + 1
        hand1_numb[card[0]] = hand1_numb[card[0]] + 1

    for card in hand2:
        hand2_suit[card[1]] = hand2_suit[card[1]] + 1
        hand2_numb[card[0]] = hand2_numb[card[0]] + 1        
    
    pl1_win = True               
    pl1_score = poker_get_hand_score(hand1_suit, hand1_numb)
    pl2_score = poker_get_hand_score(hand2_suit, hand2_numb)

    if(pl1_score > pl2_score):
        pl1_win = True
    else:
        pl1_win = False

    print(pl1_win, " ", hand1, " ", hand2)
    return pl1_win

tot_pl1_win = 0

for line in file.readlines():
    hands = line.strip().replace('"','').split(" ")
    hand1 = list()
    hand2 = list()
    for i, hand in enumerate(hands):
        if i < 5:
            hand1.append(list(hand))
        else:
            hand2.append(list(hand))

    if(poker_check_winner(hand1, hand2)):
        tot_pl1_win = tot_pl1_win + 1  

print(tot_pl1_win)