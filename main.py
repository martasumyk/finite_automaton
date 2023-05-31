'''
Main module to implement simulator of life on finite automaton model.
The model has such states: eat, sleep, study, cry, train.
'''
import time
import random


class State:
    '''
    Class to create a general state.
    '''
    def __init__(self, name):
        '''
        Initializes the data of the state.
        '''
        self.name = name

    def __str__(self):
        '''
        Class to return the name of the state.
        '''
        return f'Now you are {self.name}ing.'


class Eat(State):
    '''
    Class to eat something at trapezna.
    '''
    def __init__(self):
        '''
        Initializes the class data.
        '''
        super().__init__(name='eat')
        self.food = {
            'Breakfast': ['porridge', 'English breakfast'],
            'Dinner': ['soup', 'French fries'],
            'Supper': ['Grilled chicken', 'pizza']
        }
    def __str__(self):
        '''
        Returns the string of the food.
        '''
        return 'Mmm... Yummy!'


class Sleep(State):
    '''
    Class sleep a little bit between deadlines.
    '''
    def __init__(self):
        '''
        Initializes the class data.
        '''
        super().__init__(name='sleep')


class Study(State):
    '''
    Class to study something.
    '''
    def __init__(self):
        '''
        Initializes the class data.
        '''
        super().__init__(name='study')
        self.subjects = ['Discrete math', 'Calculus', 'OP']
        self.subject = random.choice(self.subjects)

    def __str__(self):
        '''
        Returns the string with the name of the subject we are studying.
        '''
        return f'Now you are {self.name}ing {self.subject}.'


class Train(State):
    '''
    Class to train yourself.
    '''
    def __init__(self):
        '''
        Initializes the class data.
        '''
        super().__init__(name='train')


class Rest(State):
    '''
    Class to rest a little bit.
    '''
    def __init__(self):
        '''
        Initializes the class data.
        '''
        super().__init__(name='rest')


class Walk(State):
    '''
    Class to walk with friends.
    '''
    def __init__(self):
        '''
        Initializes the class data.
        '''
        super().__init__(name='walk')


class AirAlarm:
    '''
    Class to fo to shelter when there is an air alarm.
    '''
    def __str__(self):
        '''
        Returns the air alarm state.
        '''
        return f'Going to the shelter...'



def go_eating(current_state, time):
    '''
    Function to go and eat something.
    '''
    if 5 <= time <= 6:
        current_state = Eat()
        food = random.choice((current_state.food)['Breakfast'])

    elif 12 <= time <= 14:
        current_state = Eat()
        food = random.choice((current_state.food)['Dinner'])

    elif time >= 20:
        current_state = Eat()
        food = random.choice((current_state.food)['Supper'])
    print(f'You are eating {food}.')
    return current_state




class DaySimulation:
    '''
    Class to simulate my day.
    '''
    def __init__(self):
        '''
        Initializes day data with the sleep state.
        '''
        self.current_state = Sleep()

        # Attribute to indicate wheather it is raining now:
        if random.random() <= 0.2:
            self.rain = True
        else:
            self.rain = False

        self.time = 0

        # Attribute to indicate if there is an air alarm now:
        self.air_alarm = AirAlarm()
        self.eat = Eat()
        self.sleep = Sleep()
        self.study = Study()
        self.train = Train()
        self.walk = Walk()
        self.rest = Rest()


        # Attribute to indicate if the person is alive:
        self.alive = True

        # Also I have some attributes:
        self.energy = 0
        self.intelect = 0
        self.hunger = 0



    def change_state(self, next_state):
        '''
        Changes the state of FMA.
        '''
        self.current_state = next_state
        print(str(self.current_state))


    def check_alive(self):
        '''
        Checks if I`m alive.
        '''
        if self.energy < 0 or self.hunger < 0:
            return False
        return True


    def main(self):
        '''
        Main method to simulate my life.
        '''
        print('Let`s start our simulation!')
        time.sleep(1)
        print(f'It`s {self.time} o`clock.')
        time.sleep(1)
        print('Of course, it`s night, so you need to sleep a little bit.')
        time.sleep(1)
        # Now i`m sleeping:
        print(self.current_state)
        self.energy += 10
        time.sleep(1)
        print('...')
        time.sleep(1)

        while self.time != 5:
            # There is a possibility that there will be an air alarm at night:
            if random.random() <= 0.3:
                print('Air alarm!!!')
                time.sleep(1)
                self.change_state(self.air_alarm)
                # It`s so hard going to the shelter at night so i lose my energy:
                self.energy -= 10
                print('Not very good morning, buuut we will try to start our day cool.')
            self.time += 5
            time.sleep(1)
            print(f'It`s {self.time} o`clock.')
            time.sleep(1)
            print('Good morning!')
            time.sleep(1)
            print('...')

        time.sleep(1)
        # Morning, it`s time to eat something:
        print('Time to eat something for breakfast.')
        time.sleep(1)
        self.current_state = go_eating(self.current_state, self.time)
        print('...')
        self.hunger += 10
        self.time += 1
        time.sleep(1)
        print(f'It`s {self.time} o`clock.')
        time.sleep(1)

        # Most probably i`m going training (running) after my breakfast if it`s not raining:
        if not self.rain:
            self.current_state = self.train
            print(self.current_state)
            self.energy += 20
            self.hunger -= 5
            self.time += 1
            time.sleep(1)
            print('It was a great running!')
            print('...')
        else:
            print('Unfortunately, it`s raining outside(')
            time.sleep(1)
            print('So you go to study something before going to univercity')
            time.sleep(1)
            self.change_state(self.study)
            self.time += 2
            self.intelect += 1
            print('...')
            time.sleep(1)

        print(f'It`s {self.time} o`clock.')
        if self.time >= 8:
            print('You have been studying for so long and now you`re running out of time.')
            time.sleep(1)
            self.time += 1
            print('But you decided to be on time in uni so you hurry up and go to univercity.')
        else:
            print('You have finished all the morning tasks earlier so you may rest a little bit.')
            self.change_state(self.rest)
            self.time += 1
        print('...')
        time.sleep(1)
        print(f'It`s {self.time} o`clock.')
        time.sleep(1)
        print('Now it`s time to go to univercity.')
        time.sleep(1)
        self.change_state(self.walk)
        self.time += 1
        print('...')
        time.sleep(1)
        print(f'It`s {self.time} o`clock.')
        time.sleep(1)
        print('Now it`s time to study.')
        time.sleep(1)
        self.change_state(self.study)
        self.intelect += 1
        self.hunger -= 1
        self.energy -= 1
        self.time += 1
        time.sleep(1)
        print('...')
        time.sleep(1)
        print(f'It`s {self.time} o`clock.')
        time.sleep(1)
        print('Now i`m going to prepare to one of my exams.')
        time.sleep(1)
        self.change_state(self.study)
        self.intelect += 1
        self.energy -= 1
        self.hunger -= 1
        self.time += 1
        time.sleep(1)
        print(f'It`s {self.time} o`clock.')
        time.sleep(1)
        print('It was hard but you must study a little bit more.')
        time.sleep(1)
        self.change_state(self.study)
        self.intelect += 1
        self.energy -= 1
        self.hunger -= 1
        self.time += 1
        print('...')
        time.sleep(1)
        print(f'It`s {self.time} o`clock.')
        time.sleep(1)
        if not self.check_alive():
            print('You have done too much work today and died...')
        else:
            print('You have studied a lot so it`s time to relax a little bit now.')
            time.sleep(1)
            if random.random() <= 0.5:
                self.change_state(self.rest)
                self.energy += 20
                time.sleep(1)
            else:
                if random.random () <= 0.25:
                    print('You decided to go to trapezna and eat.')
                    self.current_state = go_eating(self.current_state, self.time)
                    self.hunger += 1
                    time.sleep(1)
                else:
                    print('You decided to go to park and rest there a little bit.')
                    time.sleep(1)
                    self.change_state(self.walk)
                    self.energy += 20
                    time.sleep(1)
            self.time += 1
            print('...')
            time.sleep(1)
            print(f'It`s {self.time} o`clock.')
            time.sleep(1)
            print('You have relax a little bit and now return to studying.')
            time.sleep(1)
            self.change_state(self.study)
            self.intelect += 5
            self.energy -= 5
            self.time += 1
            time.sleep(1)
            print('...')
            time.sleep(1)
            print(f'It`s {self.time} o`clock.')
            if random.random() <= 0.9:
                print('You was so tired that you`ve decided to sleep during a day.')
                self.energy += 5
                time.sleep(1)
                self.change_state(self.sleep)
                time.sleep(1)
                self.time += 3
            else:
                print('You decided to relax a little bit.')
                self.energy += 5
                time.sleep(1)
                self.change_state(self.rest)
                time.sleep(1)
                self.time += 3
            print('...')
            time.sleep(1)
            print(f'It`s {self.time} o`clock.')
            time.sleep(1)
            print('You have relaxed and now ready to study.')
            self.change_state(self.study)
            self.intelect += 1
            self.energy -= 2
            self.time += 2
            print('...')
            time.sleep(1)
            print(f'It`s {self.time} o`clock.')
            time.sleep(1)
            print('It`s time to eat something!')
            time.sleep(1)
            self.change_state(self.eat)
            self.time += 2
            print('...')
            time.sleep(1)
            print(f'It`s {self.time} o`clock.')
            time.sleep(1)
            print('It`s time to go to bed!')
            time.sleep(1)
            print('zzz')

            
            










if __name__ == '__main__':
    day = DaySimulation()
    day.main()

