class Distance:
    def __init__(self, meters: int, centimeters: int, millimeters: int) -> None:
        self._meters = meters
        self._centimeters = centimeters
        self._millimeters = millimeters
        self._normalize()

    def _to_millimeters(self):
        """Convert the distance to millimeters."""
        return (self._meters * 1000) + (self._centimeters * 10) + self._millimeters

    def _from_millimeters(self, mm):
        """Convert millimeters to meters, centimeters, and millimeters."""
        meters = mm // 1000
        mm %= 1000
        centimeters = mm // 10
        millimeters = mm % 10
        return meters, centimeters, millimeters

    def _normalize(self):
        """Normalize the distance values."""
        mm = self._to_millimeters()
        self._meters, self._centimeters, self._millimeters = self._from_millimeters(mm)

    @property
    def meters(self):
        return self._meters

    @meters.setter
    def meters(self, value):
        self._meters = value
        self._normalize()

    @property
    def centimeters(self):
        return self._centimeters

    @centimeters.setter
    def centimeters(self, value):
        self._centimeters = value
        self._normalize()

    @property
    def millimeters(self):
        return self._millimeters

    @millimeters.setter
    def millimeters(self, value):
        self._millimeters = value
        self._normalize()

    def __repr__(self) -> str:
        return f"Distance(meters={self._meters}, centimeters={self._centimeters}, millimeters={self._millimeters})"

    def __str__(self) -> str:
        return f"{self._meters}m, {self._centimeters}cm, {self._millimeters}mm"

    def __iadd__(self, other):
        if isinstance(other, Distance):
            total_mm = self._to_millimeters() + other._to_millimeters()
            meters, centimeters, millimeters = self._from_millimeters(total_mm)
            self._meters = meters
            self._centimeters = centimeters
            self._millimeters = millimeters
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, Distance):
            total_mm = self._to_millimeters() - other._to_millimeters()
            if total_mm < 0:
                raise ValueError("Resulting distance cannot be negative.")
            meters, centimeters, millimeters = self._from_millimeters(total_mm)
            self._meters = meters
            self._centimeters = centimeters
            self._millimeters = millimeters
            return self
        return NotImplemented


    def __add__(self, other):
        if isinstance(other, Distance):
            total_mm = self._to_millimeters() + other._to_millimeters()
            meters, centimeters, millimeters = self._from_millimeters(total_mm)
            return Distance(meters, centimeters, millimeters)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Distance):
            total_mm = self._to_millimeters() - other._to_millimeters()
            if total_mm < 0:
                raise ValueError("Resulting distance cannot be negative.")
            meters, centimeters, millimeters = self._from_millimeters(total_mm)
            return Distance(meters, centimeters, millimeters)
        return NotImplemented

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            total_mm = self._to_millimeters() * factor
            meters, centimeters, millimeters = self._from_millimeters(total_mm)
            return Distance(meters, centimeters, millimeters)
        return NotImplemented

    def __truediv__(self, divisor):
        if isinstance(divisor, (int, float)) and divisor != 0:
            total_mm = self._to_millimeters() / divisor
            meters, centimeters, millimeters = self._from_millimeters(total_mm)
            return Distance(meters, centimeters, millimeters)
        return NotImplemented

def main():
    d1 = Distance(10, 0, 1)
    d2 = Distance(1, 2, 3)

    d3 = d1 + d2
    print(f"{d3} => d1 + d2")
    d4 = d1 - d2
    print(f"{d4} => d1 - d2")
    d4 -= d2
    print(f"{d4} => d4 -= d2")
    d3 += d2
    print(f"{d3} => d3 += d2")
    d6 = d1 * 5
    print(f"{d6}  => d1 * 5")
    d6 = d1 / 4
    print(f"{d6}  => d1 / 4")

if __name__ == '__main__':
    main()
