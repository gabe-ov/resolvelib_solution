from resolvelib.reporters import BaseReporter
from collections import defaultdict

class Reporter(BaseReporter):
    def __init__(self):
        self.dependency_graph = defaultdict(list)
        self.visited_stack = []
    def starting(self):
        print("starting()")

    def starting_round(self, index):
        print(f"starting_round({index})")

    def ending_round(self, index, state):
        print(f"ending_round({index}, ...)")

    def ending(self, state):
        print("ending(...)")

    def adding_requirement(self, requirement, parent):
        print(f"  adding_requirement({requirement}, {parent})")
        if parent:
            self.dependency_graph[str(parent)].append(str(requirement))
            print(f"  adding_requirement({requirement}, {parent})")

            if str(requirement) in self.visited_stack:
                print(f" Detected possible cyclical dependence: {' -> '.join(self.visited_stack + [str(requirement)])}")
            else:
                self.visited_stack.append(str(requirement))
        else:
            print(f"  adding_requirement({requirement}, None)")

    def backtracking(self, candidate):
        print(f"  backtracking({candidate})")
        if self.visited_stack:
            print(f"Stack before: {self.visited_stack}")
            self.visited_stack.pop()
            print(f"Stack after: {self.visited_stack}")

    def pinning(self, candidate):
        print(f"  pinning({candidate})")

    def resolving_conflicts(self, causes):
        print("Conflict detected")
        for cause in causes:
            print(f" - {cause}")