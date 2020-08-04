from random import choice as chc

class SPS():
    
    Options = ['Stone', 'Paper', 'Scissors']
    Positive_feedback = ['Bravo','Well done', 'Congrats', 'Me noob, you pro',
    'Looks like someone learned from the  best']
    Negative_feedback = ['Suck it, loser' , 'ahhhaa down and out' , 'Noob af' ,
    'Time to go back to training' , 'See ya loser']
    
    human_score = comp_score = 0
    rounds = 0
    gamesplayed = 0
    tied = 0

    def Greetings(self, player_name):
        print('Hi!', player_name, 'Let the games begin!\n')
        obj.Start()

    def Start(self):
        SPS.gamesplayed += 1
        chance = [0,1]
        turn = chc(chance)
        if turn == 0:
            print('It\'s computer\'s turn\n')
        else:
            print('You go first. No I\'m not cheating xD\n')
        
        obj.gamebegins(turn)

    def gamebegins(self, turn):
        while SPS.rounds < 3:
            if turn == 0:
                comp_play = chc(SPS.Options)
                human_play = input('Choose one from Stone, paper or scissors\n').capitalize()
            if turn == 1:
                human_play = input('Choose one from Stone, paper or scissors\n').capitalize()
                comp_play = chc(SPS.Options)
            if (comp_play == 'Stone' and human_play == 'Paper') or (comp_play == 'Paper'
            and human_play == 'Scissors') or (comp_play == 'Scissors' and human_play == 'Stone'):
                print(chc(SPS.Positive_feedback), '\n')
                SPS.human_score += 1
                SPS.rounds += 1

            if (human_play == 'Stone' and comp_play == 'Paper') or (human_play == 'Paper'
            and comp_play == 'Scissors') or (human_play == 'Scissors' and comp_play == 'Stone'):
                print(chc(SPS.Negative_feedback), '\n')
                SPS.comp_score += 1
                SPS.rounds += 1

            if human_play == comp_play:
                SPS.tied += 1
                print('Can\'t believe I think like a human :(. It is a tie.\n')

        tired = input('Are you tired ?\n').capitalize()
        if tired == 'Yes':
            obj.GameEnded()
            
        if tired == 'No':
            SPS.rounds = 0
            obj.Start()
            

    def GameEnded(self):
        print('GGWP: Good game. Well Played\n')
        print('You played', SPS.gamesplayed, 'games. \n')
        print('Computer Score:', SPS.comp_score, 'Your score:', SPS.human_score, '\n')
        if SPS.comp_score > SPS.human_score:
            print('You are good but not as good as me')

        elif SPS.comp_score < SPS.human_score:
            print('Teach me Senpai')
        else:
            print('It is a tie. We should play often')

obj = SPS()
name = input('Enter the player name')       
obj.Greetings(name)





            







