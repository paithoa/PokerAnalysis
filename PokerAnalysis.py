from __future__ import division
from deuces import Card
from deuces import Evaluator
import pydealer as pd

# Import the base classes:
from pydealer.const import POKER_RANKS

def main():
    evaluator = Evaluator()
    deck = pd.Deck(ranks=POKER_RANKS)
    deck.shuffle()
    me = deck.deal(2)
    player_2 = deck.deal(2)
    player_3 = deck.deal(2)
    player_4 = deck.deal(2)
    player_5 = deck.deal(2)
    player_6 = deck.deal(2)
    player_7 = deck.deal(2)
    player_8 = deck.deal(2)
    player_9 = deck.deal(2)
    players = [me,player_2,player_3,player_4,player_5,player_6,player_7,player_8,player_9]
    playersPlaying = []
    if(checkPlayable(me)):  
        for player in players:
            if(checkPlayable(player) == 1):
                playersPlaying.append(player)
        for x in playersPlaying:
            print(x.cards)
        board = deck.deal(5)
        first_card = "%s" % board[0].abbrev 
        second_card =  "%s" % board[1].abbrev 
        third_card =  "%s" % board[2].abbrev 
        fourth_card =  "%s" % board[3].abbrev 
        fifth_card =  "%s" % board[4].abbrev 
        community_cards = [Card.new(first_card),Card.new(second_card),
        Card.new(third_card),Card.new(fourth_card),Card.new(fifth_card)]
        my_first_card=  "%s" % me[0].abbrev 
        my_second_card =  "%s" % me[1].abbrev 

        player_2_first_card = "%s" % player_2[0].abbrev 
        player_2_second_card = "%s" % player_2[0].abbrev 

        player_3_first_card = "%s" % player_3[0].abbrev 
        player_3_second_card = "%s" % player_3[0].abbrev

        player_4_first_card = "%s" % player_4[0].abbrev 
        player_4_second_card = "%s" % player_4[0].abbrev

        player_5_first_card = "%s" % player_5[0].abbrev 
        player_5_second_card = "%s" % player_5[0].abbrev

        player_6_first_card = "%s" % player_6[0].abbrev 
        player_6_second_card = "%s" % player_6[0].abbrev

        player_7_first_card = "%s" % player_7[0].abbrev 
        player_7_second_card = "%s" % player_7[0].abbrev

        player_8_first_card = "%s" % player_8[0].abbrev 
        player_8_second_card = "%s" % player_8[0].abbrev

        player_9_first_card = "%s" % player_9[0].abbrev 
        player_9_second_card = "%s" % player_9[0].abbrev

        print(my_first_card,my_second_card)
        print("New Iteration")

        '''
        my_hands = [Card.new(my_first_card),Card.new(my_second_card) ]
        player_2_hands = [Card.new(player_2_first_card),Card.new(player_2_second_card)]
        player_3_hands = [Card.new(player_2_first_card),Card.new(player_2_second_card)]
        player_4_hands = [Card.new(player_2_first_card),Card.new(player_2_second_card)]
        player_5_hands = [Card.new(player_2_first_card),Card.new(player_2_second_card)]
        player_6_hands = [Card.new(player_2_first_card),Card.new(player_2_second_card)]
        player_7_hands = [Card.new(player_2_first_card),Card.new(player_2_second_card)]
        player_8_hands = [Card.new(player_2_first_card),Card.new(player_2_second_card)]
        #checkStatus(me,community_cards)
        print(community_cards)
        Card.print_pretty_cards(community_cards + my_hands + player_2_hands)
        my_score = evaluator.evaluate(community_cards, my_hands)
        opponent_score = evaluator.evaluate(community_cards, player_2_hands)
        if(my_score<opponent_score):
            print("you win at showdown")
        else:
            print("you lose at showdown")
        '''
        return checkPlayable(me)
    else:
        return checkPlayable(me)

def pair(playerCards):
    if(playerCards.cards[0].value == playerCards.cards[1].value):
        return True
    return False
def suitedConnectorLessThanOREqualToTwoGap(playerCards):
    if((playerCards.cards[0].suit == playerCards.cards[1].suit) & (abs(POKER_RANKS["values"][playerCards.cards[0].value] - POKER_RANKS["values"][playerCards.cards[1].value]) <= 2)):
        return True
    return False
def premiumHands(playerCards):
    if((POKER_RANKS["values"][playerCards.cards[0].value] > 9) & (POKER_RANKS["values"][playerCards.cards[0].value] <= 14) & (POKER_RANKS["values"][playerCards.cards[1].value] > 9) & (POKER_RANKS["values"][playerCards.cards[1].value] <= 14) ):
        return True
    return False
#def highCard():
    #if playerCards.cards[0].value != 
def checkPlayable(playerCards):
    if(suitedConnectorLessThanOREqualToTwoGap(playerCards) | premiumHands(playerCards) | pair(playerCards)):
        return 1
    return 0
#def checkStatus(playerCards,communityCards):
    #if :
        #return True
    #return False

playHand = 0
UnPlayHand = 0 
for i in range(30):
    if(main()== 1):
        playHand = playHand + 1
    else:
        UnPlayHand = UnPlayHand +1
print(playHand)
print(UnPlayHand)
print(playHand/UnPlayHand)


#(highCard()| onePair ()| twoPair() | setCombo() | straight() | flush() | fullhouse() | straightflush() | quads | royalflush())

#check one player hand

#check one vs two player
#check one vs 9 players for instance
# run it multiple time till showdown

# make it flop , turn , river

# how many players?
# type of players tight , gambler, random , combination?

# AI ??? BOT ???? 

#https://www.data-blogger.com/2017/11/01/pokerbot-create-your-poker-ai-bot-in-python/
#https://github.com/ishikota/PyPokerGUI