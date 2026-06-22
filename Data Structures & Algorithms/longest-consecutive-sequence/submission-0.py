class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences = []
        seen = set()
        longest = 0
        for num in nums:
            if num not in seen:
                seen.add(num)
        for num in nums:
            if (num - 1) not in seen:
                sequence = [num]
                value = num
                runValid = True
                while runValid:
                    if (value + 1) not in seen:
                        runValid = False
                    else:
                        value += 1 
                        sequence.append(value)
                sequences.append(sequence)
        if sequences:
            longest = len(sequences[0])
            for sequence in sequences:
                if len(sequence) > longest:
                    longest = len(sequence)
        return longest
                
                
        