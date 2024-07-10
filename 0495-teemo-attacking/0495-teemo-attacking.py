class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        poisoned_duration = 0
        for i in range(len(timeSeries) - 1):
            poisoned_duration += min(duration, timeSeries[i + 1] - timeSeries[i])
        
        # Add the duration for the last attack
        poisoned_duration += duration
        
        return poisoned_duration