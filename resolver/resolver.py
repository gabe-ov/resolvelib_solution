from resolvelib.resolvers import Resolver
from resolvelib.reporters import BaseReporter  # ou PrintingReporter
from resolvelib.resolvers import ResolutionTooDeep, ResolutionError, ResolutionImpossible
from .provider import CaseProvider
from .reporter import Reporter
from .repository import REPOSITORY
from .models import Requirement
import traceback

def resolve_requirements(requirements: list[Requirement], data: dict):
    # acesso aos meus dados
    provider = CaseProvider(data)
    # para report/debug
    reporter = Reporter()

    resolver = Resolver(provider, reporter)

    try:
        result = resolver.resolve(requirements)
        return result
    except ResolutionError as e:
        print(f" Resolution failed: {e}")
        for parent, children in reporter.dependency_graph.items():
            print(f"{parent} -> {children}")
        return None
    except ResolutionTooDeep as e:
        print(f" Resolution failed: {e}")
        for parent, children in reporter.dependency_graph.items():
            print(f"{parent} -> {children}")
        return None
    except ResolutionImpossible as e:
        print(f" Resolution failed: {e}")
        for parent, children in reporter.dependency_graph.items():
            print(f"{parent} -> {children}")
        return None
    except Exception as e:
        print(" [ERRO INTERNO] Algo deu errado durante a resolução.")
        traceback.print_exc()
        return None