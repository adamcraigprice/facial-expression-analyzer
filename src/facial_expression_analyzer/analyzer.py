"""Simple landmark-based facial expression analyzer.

This module provides a small Analyzer class which can classify expressions using
heuristics on facial landmark coordinates. The implementation is intentionally
lightweight so it can be used without heavy native deps for tests and as a
starting point for real detector integration (e.g., MediaPipe / dlib / OpenCV).
"""
from typing import List, Tuple
import math

Landmark = Tuple[float, float]  # normalized (x, y)


def _dist(a: Landmark, b: Landmark) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


class Analyzer:
    """Analyze facial expression from landmarks.

    The analyzer expects landmarks as a list of (x, y) tuples normalized to the
    image dimensions (values in [0, 1]). The landmark indexing is generic: the
    user should pass landmarks for the key points required by the heuristics.

    For the built-in heuristics this implementation expects the following
    landmark indices:
      - left_eye (index 0)
      - right_eye (index 1)
      - left_mouth_corner (index 2)
      - right_mouth_corner (index 3)
      - top_lip (index 4)
      - bottom_lip (index 5)
      - left_eyebrow (index 6)
      - right_eyebrow (index 7)

    These expectations are documented for the demo and tests; any other
    landmark ordering can be used as long as the caller maps points accordingly.
    """

    def __init__(self):
        pass

    def analyze_from_landmarks(self, landmarks: List[Landmark]) -> str:
        """Return a coarse expression label given landmarks.

        Possible return values: 'smile', 'surprise', 'frown', 'neutral'.
        """
        if len(landmarks) < 8:
            raise ValueError("analyze_from_landmarks requires at least 8 landmarks")

        left_eye = landmarks[0]
        right_eye = landmarks[1]
        left_mouth = landmarks[2]
        right_mouth = landmarks[3]
        top_lip = landmarks[4]
        bottom_lip = landmarks[5]
        left_eyebrow = landmarks[6]
        right_eyebrow = landmarks[7]

        # mouth width and height
        mouth_width = _dist(left_mouth, right_mouth)
        mouth_height = _dist(top_lip, bottom_lip)
        eye_distance = _dist(left_eye, right_eye) or 1e-6

        mouth_aspect = mouth_height / eye_distance
        smile_ratio = mouth_width / eye_distance

        # eyebrow distance: average distance between eye and eyebrow vertically
        brow_left_gap = abs(left_eye[1] - left_eyebrow[1])
        brow_right_gap = abs(right_eye[1] - right_eyebrow[1])
        brow_gap = (brow_left_gap + brow_right_gap) / 2.0

        # Heuristic thresholds (tunable)
        if mouth_aspect > 0.35 and mouth_aspect > 1.5 * 0.15:
            return "surprise"
        if smile_ratio > 0.55:
            return "smile"
        if brow_gap < 0.02 and mouth_aspect < 0.08:
            return "frown"
        return "neutral"


# convenience function

def analyze(landmarks: List[Landmark]) -> str:
    return Analyzer().analyze_from_landmarks(landmarks)