import pytest
from facial_expression_analyzer import Analyzer

def test_smile_detected():
    an = Analyzer()
    # synthetic smile: wider mouth
    landmarks_smile = [
        (0.35, 0.4),
        (0.65, 0.4),
        (0.34, 0.68),
        (0.66, 0.68),
        (0.5, 0.69),
        (0.5, 0.71),
        (0.35, 0.33),
        (0.65, 0.33),
    ]
    assert an.analyze_from_landmarks(landmarks_smile) == "smile"

def test_surprise_detected():
    an = Analyzer()
    # synthetic surprise: tall mouth opening
    landmarks_surprise = [
        (0.35, 0.4),
        (0.65, 0.4),
        (0.45, 0.68),
        (0.55, 0.68),
        (0.5, 0.62),
        (0.5, 0.80),
        (0.35, 0.33),
        (0.65, 0.33),
    ]
    assert an.analyze_from_landmarks(landmarks_surprise) == "surprise"

def test_invalid_landmarks():
    an = Analyzer()
    with pytest.raises(ValueError):
        an.analyze_from_landmarks([])