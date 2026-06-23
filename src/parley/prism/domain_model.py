from typing import List
from dataclasses import dataclass

@dataclass
class Header():
    text: str # "dtmc|ctmc|mdp|pta|pomdp|popta"

@dataclass
class Constant():
    text: str # "const int p=1;"

@dataclass
class LocalVariable():
    text: str # "c : [1..10] init 0;"

@dataclass
class GlobalVariable():
    text: str

@dataclass
class Command():
    text: str # "[action] guard -> prob_1: update_1 + ... + prob_n : update_n ;"

@dataclass
class Module():
    name: str
    local_variables: List[LocalVariable] # list of type variable
    commands: List[Command]

@dataclass
class Item():
    text: str # [action] guard : rewards

@dataclass
class Reward():
    name: str
    items: List[Item]

@dataclass
class Formula():
    text: str # "formula <identifier> = <expression>"

@dataclass
class Label():
    text: str # "label "

@dataclass
class Model():
    header: Header
    constants: List[Constant]
    global_variables: List[GlobalVariable]
    modules: List[Module]
    rewards: List[Reward]
    formulas: List[Formula]
    labels: List[Label]
    init: str | None

# TODO add functionality to turn a Python PRISM Model to a string (for creating files)
def serialize(model: Model) -> str:
    return NotImplementedError