# provider.py
from resolvelib.structs import RequirementInformation
from resolvelib.providers import AbstractProvider
from packaging.version import Version
from .models import Requirement, Candidate
from .repository import REPOSITORY

class CaseProvider(AbstractProvider):

    def __init__(self, index: dict):
        self.candidates = index

    def identify(self, requirement_or_candidate: Requirement | Candidate)-> str:
        return f"{requirement_or_candidate.type}:{requirement_or_candidate.slug}"

    def get_preference(
        self,
        identifier: any,
        resolutions: any,
        candidates: any,
        information: any,
        backtrack_causes: any
    ):
        return 0  # todas as dependencias iguais

    def find_matches(self, identifier: str, requirements: Requirement, incompatibilities)-> Candidate:
        print(f'identifier: {identifier}')
        print(f'requirements: {list(requirements[identifier])}')
        all_requirements = list(requirements[identifier])
        slug_type = all_requirements[0].type, all_requirements[0].slug
        all_specs = [r.spec for r in all_requirements]

        versions = self.candidates.get(slug_type, {})
        print(f'versions: {versions}')
        candidates = []
        for version in versions:
            version_obj = Version(version)
            if all(version_obj in spec for spec in all_specs):
                deps = versions[version]
                dep_objs = [
                    Requirement(d["type"], d["slug"], d["version_spec"])
                    for d in deps
                ]
                candidates.append(Candidate(slug_type[0], slug_type[1], version, dep_objs))

        return sorted(candidates, key=lambda c: Version(c.version), reverse=True)

    def is_satisfied_by(self, requirement: Requirement, candidate: Candidate)-> bool:
        return (requirement.slug == candidate.slug 
                and requirement.type == candidate.type 
                and Version(candidate.version) in requirement.spec)

    def get_dependencies(self, candidate: Candidate)-> Requirement:
        return candidate.dependencies
