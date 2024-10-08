import enum


class LeadControlTag(enum.Enum):
    LC1 = "[LC1]"
    LC2 = "[LC2]"
    LC3 = "[LC3]"
    LC4 = "[LC4]"
    LC5 = "[LC5]"

    @staticmethod
    def from_value(value: str):
        for tag in LeadControlTag:
            if tag.value == value:
                return tag
        raise ValueError(f"Invalid value {value}")

    def __str__(self):
        return self.value
