from resolver.models import Requirement
from resolver.resolver import resolve_requirements
from resolver.repository import REPOSITORY

if __name__ == "__main__":
    reqt = [
        Requirement("classe", "guerreiro_berserker", ">=2.0")
    ]
    resolved = resolve_requirements(reqt, REPOSITORY)
    print(f"\n\nMappings:")
    for ident, cand in resolved.mapping.items():
        print(f"{ident} -> {cand}")
    print(f"\n\nCriteria:")
    for identifier, criterion in resolved.criteria.items():
        if identifier not in resolved.mapping:
            continue
        print(f'component: {identifier}')

        for entry in criterion.information:
            if entry.parent is not None:
                print(f'\trequirement: {entry.requirement} - via: {entry.parent}')
            else:
                print(f'\trequirement: {entry.requirement} - via: System')
