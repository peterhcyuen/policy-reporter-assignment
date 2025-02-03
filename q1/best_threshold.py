from typing import Dict


def best_threshold(data: Dict):
    """
    Return the best threshold which can achieve recall >= 0.9

    Parameters:
        data (list of dict): Each dict contains:
            - 'threshold': float, the threshold value.
            - 'TP': int, number of true positive
            - 'TN': int, number of true negative
            - 'FP': int, number of false positive
            - 'FN': int, number of false negatives
    """

    # List to store candidate thresholds meeting the recall requirement.
    thresholds = []

    # Loop over each record in the data
    for record in data:
        TP = record.get('TP', 0)
        FN = record.get('FN', 0)

        # Avoid division by zero. If there are no positive cases, skip this record.
        if TP + FN == 0:
            continue

        recall = TP / (TP + FN)

        # If the recall >= 0.9, add this threshold to the candidate list.
        if recall >= 0.9:
            thresholds.append(record['threshold'])

    # If no threshold meets the recall requirement, return None
    if not thresholds:
        return None

    # Among the candidates, choose the highest threshold.
    # A higher threshold usually implies higher precision by reducing false positive
    best = max(thresholds)
    return best


if __name__ == "__main__":
    example_data = [
        {"threshold": 0.1, "TP": 95, "TN": 40, "FP": 60, "FN": 5},
        {"threshold": 0.2, "TP": 92, "TN": 45, "FP": 55, "FN": 8},
        {"threshold": 0.3, "TP": 90, "TN": 50, "FP": 50, "FN": 10},
        {"threshold": 0.4, "TP": 85, "TN": 55, "FP": 45, "FN": 15},
        {"threshold": 0.5, "TP": 80, "TN": 60, "FP": 40, "FN": 20},
        {"threshold": 0.6, "TP": 75, "TN": 65, "FP": 35, "FN": 25},
        {"threshold": 0.7, "TP": 70, "TN": 70, "FP": 30, "FN": 30},
        {"threshold": 0.8, "TP": 65, "TN": 75, "FP": 25, "FN": 35},
        {"threshold": 0.9, "TP": 60, "TN": 80, "FP": 20, "FN": 40},
    ]

    result = best_threshold(example_data)
    if result is not None:
        print(f"The best threshold with recall >= 0.9 is: {result}")
    else:
        print("No threshold yields a recall >= 0.9")
