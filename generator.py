"""Generator für randomisierte gerichtete Graphen für das Transportproblem.

Funktion:
    generate_random_directed_graph(num_nodes, num_edges, seed, supply_range=10)

Gibt zwei Listen zurück: List[Node], List[Edge]. Die Summe aller `supply`-Werte ist 0
(damit das Transportproblem grundsätzlich ausgeglichen ist). Es werden keine Selbstschleifen
erzeugt und jede gerichtete Kante ist eindeutig (keine Duplikate).

Hinweis: Die Versorgung der letzten Node wird so berechnet, dass die Summe 0 ergibt. Dadurch
kann der Wert dieser Node außerhalb von `supply_range` liegen, wenn die Zufallswerte der
anderen Knoten dies erzwingen.
"""
from typing import List, Tuple
import random
import argparse

from node import Node
from edge import Edge


def generate_random_directed_graph(num_nodes: int, num_edges: int, seed: int, supply_range: int = 10, balance_demand: bool = False) -> Tuple[List[Node], List[Edge]]:
    """Generiert einen randomisierten gerichteten Graphen.

    Args:
        num_nodes: Anzahl der Knoten (>=1).
        num_edges: Anzahl der gerichteten Kanten (>=0). Max = num_nodes*(num_nodes-1).
        seed: Seed für den Zufallszahlengenerator (Determinismus).
        supply_range: (optional) Bereich für Zufalls-Supplies für die ersten n-1 Knoten: [-supply_range, supply_range].

    Returns:
        Tuple (nodes, edges) mit Node- und Edge-Objekten.

    Raises:
        ValueError: wenn Eingabewerte ungültig sind oder zu viele Kanten angefragt wurden.
    """

    if num_nodes < 1:
        raise ValueError("num_nodes muss mindestens 1 sein")
    max_edges = num_nodes * (num_nodes - 1)
    if num_edges < 0 or num_edges > max_edges:
        raise ValueError(f"num_edges muss zwischen 0 und {max_edges} liegen (ohne Selbstschleifen)")

    rng = random.Random(seed)

    # Erzeuge supplies so, dass die Gesamtsumme 0 ist.
    nodes: List[Node] = []
    for i in range(num_nodes - 1):
        s = rng.randint(-supply_range, supply_range)
        nodes.append(Node(id=i, supply=s))

    # Balanciere die Summe durch den letzten Knoten aus
    sum_so_far = sum(n.supply for n in nodes)
    if balance_demand:
        last_supply = -sum_so_far
        nodes.append(Node(id=num_nodes - 1, supply=last_supply))
    else:
        print(f"Info: Die Summe der supplies ist {sum_so_far}")

    # Erzeuge alle möglichen gerichteten Kanten (ohne Selbstschleifen)
    possible_edges = [(i, j) for i in range(num_nodes) for j in range(num_nodes) if i != j]
    rng.shuffle(possible_edges)
    chosen = possible_edges[:num_edges] # slicing
    edges: List[Edge] = [Edge(source=s, target=t, transported=-1) for (s, t) in chosen]

    return nodes, edges


def _print_graph(nodes: List[Node], edges: List[Edge]) -> None:
    print("Nodes:")
    for n in nodes:
        kind = "Producer" if n.is_producer() else ("Consumer" if n.is_consumer() else "Neutral")
        print(f"  id={n.id:2d} supply={n.supply:4d} ({kind})")
    print("\nEdges:")
    for e in edges:
        assigned = e.transported if e.is_assigned() else "unassigned"
        print(f"  {e.source} -> {e.target} transported={assigned}")


def _cli():
    parser = argparse.ArgumentParser(description="Generiere einen randomisierten gerichteten Graphen (Transportproblem)")
    parser.add_argument("num_nodes", type=int, help="Anzahl Knoten")
    parser.add_argument("num_edges", type=int, help="Anzahl Kanten")
    parser.add_argument("seed", type=int, help="Seed für RNG")
    parser.add_argument("--supply-range", type=int, default=10, help="Bereich für zufällige Supplies (default 10)")
    args = parser.parse_args()

    nodes, edges = generate_random_directed_graph(args.num_nodes, args.num_edges, args.seed, args.supply_range)
    _print_graph(nodes, edges)


if __name__ == "__main__":
    _cli()