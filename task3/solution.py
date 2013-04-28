class Person:
    """Model of a family tree."""

    def __init__(self, **kwargs):
        for attribute in kwargs:
            setattr(self, attribute, kwargs[attribute])

        self._kids = []

        for parent in ['mother', 'father']:
            if parent in kwargs:
                kwargs[parent]._kids.append(self)
            else:
                setattr(self, parent, None)

    def children(self, gender=None):
        """
        Return all children of this person,
        optionally filtered by gender.
        """

        if gender:
            return [child for child in self._kids
                    if child.gender == gender]
        else:
            return [child for child in self._kids]

    def is_direct_successor(self, successor):
        """Return if successor is this person's child."""

        for parent in [successor.father, successor.mother]:
            if parent is self:
                return True

        return False

    def __siblings(self, gender=""):
        """
        Return set of this person's siblings from
        both parents, optionally filtered by gender.
        """

        kids_from_parent = []

        for parent in [self.father, self.mother]:
            if parent:
                kids_from_parent += parent.children(gender)

        return set([kid for kid in kids_from_parent if kid is not self])

    def get_sisters(self):
        """Return list of this person's sisters."""

        return list(self.__siblings("F"))

    def get_brothers(self):
        """Return list of this person's brothers."""

        return list(self.__siblings("M"))
