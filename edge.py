"""
Edge-Klasse für das Transportproblem.

Die Klasse repräsentiert eine gerichtete Kante zwischen zwei Knoten (source -> target).
Das Attribut `transported` beschreibt, wie viele Ressourcen entlang der Kante transportiert
werden. Initial ist der Wert `-1`, was bedeutet: noch nicht belegt / nicht bestimmt.
"""
from dataclasses import dataclass


@dataclass
class Edge:
    """
    Repräsentiert eine gerichtete Kante.

    Attributes:
        source: Knoten-ID der Quelle (int).
        target: Knoten-ID des Ziels (int).
        transported: Anzahl transportierter Einheiten (int), -1 = unbestimmt.
    """

    source: int
    target: int
    transported: int = -1

    def is_assigned(self) -> bool:
        """True, wenn `transported` einen nicht-negativen Wert hat (zugewiesen)."""
        return self.transported >= 0
