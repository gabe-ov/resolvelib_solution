from packaging.specifiers import SpecifierSet
from packaging.version import Version

class Requirement:
    def __init__(self, type_: str, slug: str, spec: str):
        self.type = type_
        self.slug = slug
        self.spec = SpecifierSet(spec)

    def __repr__(self):
        return f"{self.type}:{self.slug}{self.spec}"
    
class Candidate:
    def __init__(self, type_: str, slug: str, version: str, dependencies: Requirement):
        self.type = type_
        self.slug = slug
        self.version = version
        self.dependencies = dependencies  # list of Requirement

    def __repr__(self):
        return f"{self.type}:{self.slug}-{self.version}"