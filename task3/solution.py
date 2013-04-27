class Person:
    def __init__(self, **kwargs):
        for attribute in kwargs:
            setattr(self, attribute, kwargs[attribute])

        self.kids = []

        if 'mother' in kwargs:
            self.mother.kids.append(self)
        else:
            self.mother = None

        if 'father' in kwargs:
            self.father.kids.append(self)
        else:
            self.father = None

    def children(self, **kwargs):
        if kwargs:
            return [child for child in self.kids
                    if child.gender == kwargs['gender']]
        else:
            return [child for child in self.kids]

    def is_direct_successor(self, successor):
        if successor.mother is self:
            return True
        if successor.father is self:
            return True

        return False

    def get_sisters(self):
        siblings = []
        if self.mother:
            from_mother = self.mother.children(gender='F')
            siblings += from_mother
        if self.father:
            from_father = self.father.children(gender='F')
            siblings += from_father

        return [sister for sister in set(siblings)
                if sister is not self]

    def get_brothers(self):
        siblings = []
        if self.mother:
            from_mother = self.mother.children(gender='M')
            siblings += from_mother
        if self.father:
            from_father = self.father.children(gender='M')
            siblings += from_father

        return [brother for brother in set(siblings)
                if brother is not self]