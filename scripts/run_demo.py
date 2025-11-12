#!/usr/bin/env python3
"""Small demo that shows how to call the Analyzer with synthetic landmarks."""
import sys
from facial_expression_analyzer import Analyzer

def main():
    # Example synthetic landmarks: x, y normalized
    # left_eye, right_eye, left_mouth, right_mouth, top_lip, bottom_lip, left_eyebrow, right_eyebrow
    landmarks_neutral = [
        (0.35, 0.4),
        (0.65, 0.4),
        (0.42, 0.7),
        (0.58, 0.7),
        (0.5, 0.68),
        (0.5, 0.72),
        (0.35, 0.33),
        (0.65, 0.33),
    ]

    an = Analyzer()
    print("Neutral example ->", an.analyze_from_landmarks(landmarks_neutral))

    landmarks_smile = [
        (0.35, 0.4),
        (0.65, 0.4),
        (0.38, 0.68),
        (0.62, 0.68),
        (0.5, 0.69),
        (0.5, 0.71),
        (0.35, 0.33),
        (0.65, 0.33),
    ]
    print("Smile example ->", an.analyze_from_landmarks(landmarks_smile))

    return 0


if __name__ == '__main__':
    sys.exit(main())