# Facial Expression Analyzer

A small reusable Python package that provides a simple interface to analyze facial expressions from facial landmarks. This repo contains a lightweight analyzer implementation (landmark-based heuristics), a demo script, unit tests, and a basic CI workflow.

Features
- analyze expression from landmark coordinates
- small, dependency-light implementation for unit testing and extension

Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Usage

```python
from facial_expression_analyzer import Analyzer

an = Analyzer()
# landmarks is a list of (x, y) tuples representing normalized facial landmarks
expr = an.analyze_from_landmarks(landmarks)
print(expr)
```

Running tests

```bash
pip install -r requirements.txt
pytest
```