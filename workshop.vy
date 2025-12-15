# pragma version ^0.4.1
# @license MIT

my_bool: bool

@deploy
def __init__():
    self.my_bool = True

@external
def set_bool(new_bool: bool):
    self.my_bool = new_bool

@external
def retrieve() -> bool:
    return self.my_bool
    

    
