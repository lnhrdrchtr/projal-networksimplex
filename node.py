"""Node-Klasse für das Transportproblem.

Die Klasse repräsentiert einen Knoten mit einer numerischen "supply"-Größe.
Ein positiver Wert bedeutet Produktion, ein negativer Konsum.
"""
from dataclasses import dataclass


@dataclass
class Node:
    """Repräsentiert einen Knoten im gerichteten Graphen.

    Attributes:
        id: Eindeutige Knoten-ID (int).
        supply: Positive Werte = Produktion, negative Werte = Konsum.
    """

    id: int
    supply: int

    def is_producer(self) -> bool:
        """True, wenn der Knoten Ressourcen produziert (supply > 0)."""
        return self.supply > 0

    def is_consumer(self) -> bool:
        """True, wenn der Knoten Ressourcen konsumiert (supply < 0)."""
        return self.supply < 0

    def is_intermediate(self) -> bool:
        """True, wenn der Knoten neutral ist (supply == 0)."""
        return self.supply == 0