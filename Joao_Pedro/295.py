class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        n = len(self.data)
        if n == 0:
            return 0.0
        if n % 2 == 1:
            return float(self._select(self.data, n // 2))
        else:
            left = self._select(self.data, n // 2 - 1)
            right = self._select(self.data, n // 2)
            return (left + right) / 2.0

    # -------- Mediana das Medianas (seleção linear determinística) --------
    def _select(self, arr, k):
        if len(arr) <= 5:
            return sorted(arr)[k]

        # Divide em grupos de 5 e pega a mediana de cada grupo
        groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
        medians = [sorted(group)[len(group) // 2] for group in groups]

        # Recursivamente encontra a mediana das medianas
        pivot = self._select(medians, len(medians) // 2)

        # Particiona o array em torno do pivô
        lows = [x for x in arr if x < pivot]
        highs = [x for x in arr if x > pivot]
        pivots = [x for x in arr if x == pivot]

        if k < len(lows):
            return self._select(lows, k)
        elif k < len(lows) + len(pivots):
            return pivot
        else:
            return self._select(highs, k - len(lows) - len(pivots))
