from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Combina logicamente os arrays
        nums = nums1 + nums2
        
        # Função auxiliar para achar a mediana de até 5 elementos
        def median_of_five(arr):
            arr.sort()
            return arr[len(arr)//2]
        
        # Implementação da mediana das medianas
        def median_of_medians(arr):
            if len(arr) <= 5:
                return median_of_five(arr)
            # Divide em grupos de 5
            submedians = [median_of_five(arr[i:i+5]) for i in range(0, len(arr), 5)]
            # Recursão para achar a mediana das medianas
            return median_of_medians(submedians)
        
        # Função de seleção determinística (QuickSelect com pivô da mediana das medianas)
        def select(arr, k):
            if len(arr) <= 5:
                arr.sort()
                return arr[k]
            pivot = median_of_medians(arr)
            lows = [x for x in arr if x < pivot]
            highs = [x for x in arr if x > pivot]
            pivots = [x for x in arr if x == pivot]
            
            if k < len(lows):
                return select(lows, k)
            elif k < len(lows) + len(pivots):
                return pivot
            else:
                return select(highs, k - len(lows) - len(pivots))
        
        n = len(nums)
        if n % 2 == 1:
            return float(select(nums, n // 2))
        else:
            left = select(nums, n // 2 - 1)
            right = select(nums, n // 2)
            return (left + right) / 2.0
