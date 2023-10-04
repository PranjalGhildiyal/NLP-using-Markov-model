class BlankModelException(Exception):
    def __init__(self):
        message= 'Model has not been trained/trained on null data'
        super().__init__(message)

class StateNotFoundException(Exception):
    def __init__(self, state):
        message= 'State: {} not found in the model. Try with states present in the abstract.'.format(state)
        super.__init__(message)