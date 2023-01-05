from dataclasses import dataclass


@dataclass
class Ellipsis:
    ...


print('In nodes: ', Ellipsis.__name__)
