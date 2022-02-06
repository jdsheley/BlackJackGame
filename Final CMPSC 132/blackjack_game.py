from player import Player
from dealer import Dealer


class BlackjackGame:
    def __init__(self, player_names):
        self.dealer=Dealer()
        self.dealer.name="Dealer"
        self.player_list=[]
        for i in player_names:
            self.player_list.append(Player(i,self.dealer))
        return None

    def play_rounds(self, num_rounds=1):
        """
        >>> import random; random.seed(1)
        >>> game = BlackjackGame(["Lawrence","Melissa"])
        >>> print(game.play_rounds(2))
        Round 1
        Dealer: [10, 9] 0/0/0
        Lawrence: [10, 6, 3] 0/1/0
        Melissa: [8, 8] 0/0/1
        Round 2
        Dealer: [10, 10] 0/0/0
        Lawrence: [10, 3] 0/1/1
        Melissa: [9, 10] 0/0/2
        """
        results=[]
        n=0
        for i in range(num_rounds):
            self.dealer.shuffle_deck()
            for i in range(2):
                for i in self.player_list:                          
                    i.deal_to(self.dealer.deck.draw())              
                self.dealer.deal_to(self.dealer.deck.draw())        
            for i in self.player_list:                          
                i.play_round()
            self.dealer.play_round()                            
            for i in self.player_list:                          
                if self.dealer.card_sum == 21:
                    if i.card_sum == 21:                        
                        i.record_tie()
                    else:
                        i.record_loss()
                elif self.dealer.card_sum > 21:                 
                    if i.card_sum > 21:
                        i.record_loss()
                    else:
                        i.record_win()
                else:                                           
                    if i.card_sum > 21:
                        i.record_loss()
                    if i.card_sum > self.dealer.card_sum and i.card_sum < 22:
                        i.record_win()
                    if i.card_sum == self.dealer.card_sum:
                        i.record_tie()
                    if self.dealer.card_sum > i.card_sum:
                        i.record_loss()
            n+=1
            results.append('Round '+str(n))                   
            results.append(str(self.dealer.__repr__()))         
            for i in self.player_list:
                results.append(i.__repr__())                    
                i.discard_hand()                                
            self.dealer.discard_hand()    
        results='\n'.join(results)                              
        return results

    def reset_game(self):
        """
        >>> game = BlackjackGame(["Lawrence", "Melissa"])
        >>> _ = game.play_rounds()
        >>> game.reset_game()
        >>> game.player_list[0]
        Lawrence: [] 0/0/0
        >>> game.player_list[1]
        Melissa: [] 0/0/0
        """
        for i in self.player_list:      
            i.reset_stats()
            i.discard_hand()
        self.dealer.reset_stats()
        self.dealer.discard_hand()
        return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()

