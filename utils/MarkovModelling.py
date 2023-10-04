import random
from .exceptions import StateNotFoundException, BlankModelException


class MarkovModel:
    '''
        `MarkovModel`

        Markov model for modelling data in the form of Markov Chains.

        - attributes:
            - `fit_model`: 
                - param `abstract`(`list`): the text that needs to be modelled.
                - param `n_gramss`(`int`): The number of words to be defined as a part of each state.
                - returns None
            - `predict`:
                - param `limit`: The limit of words in the generated story.
                - param `start`: The starting state of the story.
                - returns str

            - `possible_transitions`:
                - param `key`: The state, occuring in the abstract
                - param `key`: The state, occuring in the abstract
                - returns python `dict` with all possible transitions from state `key`
            
        - properties:
            - `model`: Markov model (in the form of a python `dict`)
            - `no_of_states`: Number of states in the model

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        developed by: Pranjal Ghildiyal
        '''
    
    def __init__(self):
        self.markov_model= {}
    
    def fit_model(self, abstract: list, n_grams:int)->'MarkovModel':
        '''
        `fit_model`: 
        - param `abstract`(`list`): the text that needs to be modelled.
        - param `n_gramss`(`int`): The number of words to be defined as a part of each state.
        - returns None
        '''

        for i in range(len(abstract)-n_grams-1):
            curr_state, next_state = "", ""
            for j in range(n_grams):
                curr_state += abstract[i+j] + " "
                next_state += abstract[i+j+n_grams] + " "
            curr_state = curr_state[:-1]
            next_state = next_state[:-1]
            if curr_state not in self.markov_model:
                self.markov_model[curr_state] = {}
                self.markov_model[curr_state][next_state] = 1
            else:
                if next_state in self.markov_model[curr_state]:
                    self.markov_model[curr_state][next_state] += 1
                else:
                    self.markov_model[curr_state][next_state] = 1
        
        # calculating transition probabilities
        for curr_state, transition in self.markov_model.items():
            total = sum(transition.values())
            for state, count in transition.items():
                self.markov_model[curr_state][state] = count/total
        return self

    
    def predict(self, start:str, limit: int)->str:
        '''
        `predict`:
        - param `limit`: The limit of words in the generated story.
        - param `start`: The starting state of the story.
        - returns str
        '''
        n = 0
        curr_state = start
        next_state = None
        story = ""
        story+=curr_state+" "
        while n<limit:
            next_state = random.choices(list(self.markov_model[curr_state].keys()),
                                        list(self.markov_model[curr_state].values()))
            
            curr_state = next_state[0]
            story+=curr_state+" "
            n+=1
        return story
    
    def possible_transitions(self, key):
        if key in self.markov_model.keys():
            return self.markov_model[key]
        else:
            raise StateNotFoundException(key)
    
    @property
    def model(self):
        if self.markov_model != {}:
            return self.markov_model
        raise BlankModelException
    
    @property
    def no_of_states(self):
        if self.markov_model != {}:
            return len(self.markov_model.keys())
        raise BlankModelException
        

    def __str__(self):
        string= '''
                    `MarkovModel`

                    Markov model for modelling data in the form of Markov Chains.

                    - attributes:
                        - `fit_model`: 
                            - param `abstract`(`list`): the text that needs to be modelled.
                            - param `n_gramss`(`int`): The number of words to be defined as a part of each state.
                        - `predict`:
                            - param `limit`: The limit of words in the generated story.
                            - param `start`: The starting state of the story.

                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    developed by: Pranjal Ghildiyal
                    '''
        return string










