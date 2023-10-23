class InputData:
    def __init__(self):
        self.data_type = None
        self.data = None
        self.num_personas_per_prefix = 5
        self.max_history = 0
        self.tag = False,
        self.long_prefix: bool = False
        self.utterance = None

    
    @property
    def set_data(data_type, data):
        self.data_type = data_type
        self.data = data
    
    @property
    def get_data(data_type):
        if self.data_type == data_type:
            return self.data
        else:
            raise Exception("Data type mismatch.")
    
    def update(args):
        if args is None:
            print("No args provided.")
            return self
        else:
            for key, value in args.items():
                setattr(self, key, value)
            return self
