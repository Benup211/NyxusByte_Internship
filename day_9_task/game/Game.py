import os
import json
class Quiz:
    def __init__(self):
        print(f"{'Welcome to Quiz Game':#^100}")
        self._player=''
        self._score=0
    def registerPlayer(self):
        self._player=input("Enter Player name:")
    def getPlayer(self):
        if self._player=='':
            self.registerPlayer()
        else:
            return self._player
    def play(self):
        player_name=self.getPlayer()
        current_dir=os.path.dirname(os.path.abspath(__file__))
        ques_file=open(current_dir+'/game_data.json','r')
        all_questions=json.load(ques_file)['questions']
        for index,q in enumerate(all_questions):
            print(f"{'Question ' + str(index+1):#^100}\n")
            print(f"Question:{q['question']}\n")
            for i,o in enumerate(q['options']):
                print(f'\t{i+1} {o}')
            try:
                choice=int(input("Enter your choice[1,2,3,4]:"))
                match choice:
                    case 1:
                        if q['correct_answer']==q['options'][0]:
                            self._score+=1
                    case 2:
                        if q['correct_answer']==q['options'][1]:
                            self._score+=1
                    case 3:
                        if q['correct_answer']==q['options'][2]:
                            self._score+=1
                    case 4:
                        if q['correct_answer']==q['options'][3]:
                            self._score+=1
            except Exception as E:
                print(f"Error:{E}")
    def score(self):
        return {'player name':self._player,'score':self._score}      
quiz=Quiz()
quiz.play()
current_dir=os.path.dirname(os.path.abspath(__file__))
game_log=open(current_dir+'/game.log','a')
game_log.write(str(quiz.score())+'\n')
game_log.close()