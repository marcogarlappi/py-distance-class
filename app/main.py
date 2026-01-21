from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other_distance: Any) -> "Distance":
        if isinstance(other_distance, Distance):
            return Distance(self.km + other_distance.km)
        else:
            return Distance(self.km + other_distance)

    def __iadd__(self, other_distance: Any) -> "Distance":
        if isinstance(other_distance, Distance):
            self.km += other_distance.km
            return self
        else:
            self.km += other_distance
            return self

    def __mul__(self, other: Any) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: Any) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other
