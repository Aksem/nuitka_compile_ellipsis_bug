from dataclasses import dataclass


@dataclass
class Ellipsis:
    ...


if __name__ == '__main__':
    print(Ellipsis.__name__)
