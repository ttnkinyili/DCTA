import copy
from itertools import combinations

class MassFunction:
    """
    A class to represent a Dempster-Shafer Mass Function (Basic Probability Assignment).
    """

    def __init__(self, source=None):
        """
        Initialize the MassFunction.
        
        Args:
            source: Can be a dict {hypothesis: mass} where hypothesis is a frozenset,
                    or a list of tuples [(hypothesis, mass)].
        """
        self.masses = {}
        if source:
            if isinstance(source, dict):
                for h, m in source.items():
                    self.masses[frozenset(h)] = m
            elif isinstance(source, list):
                for h, m in source:
                    self.masses[frozenset(h)] = m
        
        # Ensure 'frozenset()' (empty set) mass is 0 (Closed World Assumption)
        # unless explicitly handling open world, but for this demo we stick to standard DS.
        if frozenset() in self.masses:
            del self.masses[frozenset()]

    def normalize(self):
        """
        Normalize the mass function so that the sum of masses is 1.
        """
        total = sum(self.masses.values())
        if total == 0:
            return # Should not happen in valid BPA
        if abs(total - 1.0) > 1e-9:
            for h in self.masses:
                self.masses[h] /= total
        return self

    def __repr__(self):
        # Format for readability
        items = []
        for h, m in sorted(self.masses.items(), key=lambda x: -x[1]):
            # Convert frozenset back to set str for display
            h_str = "{" + ", ".join(sorted(list(h))) + "}"
            items.append(f"{h_str}: {m:.4f}")
        return "<MassFunction " + ", ".join(items) + ">"

    def combine(self, other):
        """
        Combine this MassFunction with another using Dempster's Rule of Combination.
        m12(A) = (1/K) * sum(m1(B)*m2(C)) where B intersection C = A
        K = 1 - sum(m1(B)*m2(C)) where B intersection C = empty
        """
        combined = {}
        conflict = 0.0

        for h1, m1 in self.masses.items():
            for h2, m2 in other.masses.items():
                intersection = h1.intersection(h2)
                if not intersection:
                    conflict += m1 * m2
                else:
                    combined[intersection] = combined.get(intersection, 0.0) + (m1 * m2)

        normalization_factor = 1.0 - conflict
        if normalization_factor <= 1e-9:
            # Total conflict
            raise ValueError("MassFunctions are totally conflicting, cannot combine.")

        # Normalize
        for h in combined:
            combined[h] /= normalization_factor

        return MassFunction(combined)

    def belief(self, hypothesis):
        """
        Calculate the Belief of a hypothesis (sum of masses of subsets).
        Bel(A) = sum(m(B)) where B is subset of A
        """
        if not isinstance(hypothesis, frozenset):
             hypothesis = frozenset(hypothesis)
             
        bel = 0.0
        for h, m in self.masses.items():
            if h.issubset(hypothesis):
                bel += m
        return bel

    def plausibility(self, hypothesis):
        """
        Calculate the Plausibility of a hypothesis.
        Pl(A) = sum(m(B)) where B intersects A
        """
        if not isinstance(hypothesis, frozenset):
             hypothesis = frozenset(hypothesis)
             
        pl = 0.0
        for h, m in self.masses.items():
            if not h.isdisjoint(hypothesis):
                pl += m
        return pl

    def pignistic(self):
        """
        Convert to Pignistic Probability (BetP) for decision making.
        BetP(x) = sum(m(A) / |A|) for all x in A
        """
        betp = {}
        for h, m in self.masses.items():
            cardinality = len(h)
            if cardinality == 0: continue
            dist_mass = m / cardinality
            for element in h:
                betp[element] = betp.get(element, 0.0) + dist_mass
        return betp
