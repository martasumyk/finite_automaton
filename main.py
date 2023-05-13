'''
Main module to implement simulator of life onfinite automaton model.
The model has such states: eat, sleep, study, cry, train.
'''
class State:
    '''
    Class that represents the state of the person in current moment.
    '''
    def __init__(self):
        '''
        Initializes the data.
        '''
        self.energy = 10
        self.intelect = 0
        self.hungry = 5
        self.alive = True
        

    def change_state(self, state):
        '''
        Changes the state of the person.
        '''
        self.state = state

    def current_state(self):
        '''
        Method that shows the person`s current state.
        '''
        return self.state

    def check_alive(self):
        '''
        Checks if person is alive.
        '''
        if self.energy <= 0 or self.hungry >= 10:
            self.alive = False
        return f'You`re dead...'


class Eat:
    '''
    Class that allows person to eat.
    '''
    pass

class Sleep:
    '''
    Class that allows person to sleep.
    '''
    pass

class Cry:
    '''
    Class that allows to cry when all is bad.
    '''
    pass

class Study:
    '''
    Class that allows to study.
    '''
    pass

class Train:
    '''
    Class that allows to train yourself.
    '''
    pass




    