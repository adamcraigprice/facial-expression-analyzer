from typing import List, Tuple

Landmark = Tuple[float, float]

def normalize_landmarks(landmarks: List[Landmark], width: int, height: int):
    """Convert pixel coordinates to normalized [0,1] coordinates.

    landmarks: list of (x, y) in pixel coordinates
    width, height: image dimensions
    """
    return [(x / width, y / height) for x, y in landmarks]