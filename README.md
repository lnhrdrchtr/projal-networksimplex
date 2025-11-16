# Projekt: Ressourcenverteilung — Graph Generator & Visualisierung

Kurzes Repository mit einer einfachen Python-Implementierung für ein Transportproblem (gerichteter Graph).

Inhalt
- `node.py` — Dataclass `Node(id: int, supply: int)` (positive = Produktion, negative = Konsum).
- `edge.py` — Dataclass `Edge(source: int, target: int, transported: int = -1)` (`transported=-1` bedeutet unassigned).
- `generator.py` — Funktion `generate_random_directed_graph(num_nodes, num_edges, seed, supply_range=10, balance_demand=False)` zum Erzeugen eines randomisierten gerichteten Graphen. Enthält auch ein kleines CLI.
- `graph_visualization.ipynb` — Jupyter Notebook mit Beispielvisualisierungen (interactive Plotly + Matplotlib fallback + optionaler `pyvis` Export).
- `requirements.txt` — Liste der benötigten Pakete.

Kurzbeschreibung
Dieses Projekt erzeugt gerichtete Graphen, bei denen Knoten Produktions- oder Konsumwerte (`supply`) haben. Kanten (`Edge`) können später mit einer Transportmenge (`transported`) belegt werden. Das Notebook zeigt, wie man solche Graphen interaktiv visualisiert und die Kanten-Transportwerte in den Plots anzeigt.

Schnellstart (Windows / PowerShell)
1. Python-Umgebung einrichten (empfohlen: `venv`):

```powershell
# Im Projektordner
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Abhängigkeiten installieren:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

3. Notebook starten (JupyterLab oder Notebook):

```powershell
# JupyterLab (falls installiert)
jupyter lab
# oder klassisches Notebook
jupyter notebook
```

4. Alternativ: Generator per CLI ausführen (Beispiel):

```powershell
python .\generator.py 6 8 42
# Gibt Liste von Nodes und Edges aus und druckt eine kompakte Übersicht
```

Notebook Hinweise
- Das Notebook `graph_visualization.ipynb` verwendet `networkx` zur Graph-Repräsentation und `plotly` für die interaktive Darstellung. `pyvis` ist optional für HTML-Export.
- Falls beim Ausführen der Plotly-Zellen die Meldung erscheint "Mime type rendering requires nbformat>=4.2.0", installiere `nbformat` in der Kernel-Umgebung und starte den Kernel neu (Jupyter Menü: Kernel -> Restart). Beispiel:

```python
import sys, subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'nbformat>=4.2.0'])
```

Visualisierung
- Die interaktive Plotly-Ansicht zeigt Knoten (Farbe: grün=Produzent, rot=Konsument, grau=neutral). Größen sind proportional zur Magnitude von `supply`.
- Edge-Labels in Notebook: die Visualisierung zeigt für jede Kante in der Grafik den Wert `transported` (oder `unassigned`).
- Matplotlib-Fallback: ebenfalls Edge-Labels via `nx.draw_networkx_edge_labels`.

Troubleshooting
- Achte darauf, dass die installierten Pakete in der gleichen Python-Umgebung liegen, die der Jupyter-Kernel verwendet. (In VS Code z. B. Kernel/Interpreter oben rechts auswählen.)
- Wenn Plotly nicht inline darstellt: als Workaround `plotly.io.renderers.default = 'browser'` setzen — öffnet die Figur im System-Browser.

Weiteres
- Wenn du möchtest, kann ich die `requirements.txt` auf die aktuell installierten exakten Versionen einfrieren (`pip freeze > requirements.txt`) oder interaktive Widgets (`ipywidgets`) ins Notebook einbauen.

---

Wenn du Änderungen wünschst (z. B. zusätzliche Felder in `Edge` wie `capacity` oder Kosten), sag Bescheid — ich passe die Dateien und das Notebook an.
