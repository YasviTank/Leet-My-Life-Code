class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = [[p,s] for p, s in zip(position, speed)]
        st = []
        
        for p, s in sorted(cars)[::-1]:
            time_taken = float((target - p)) / s
            if not st or time_taken > st[-1]:
                st.append(time_taken)
        
        return len(st)


        # Time complexity = O(n log n)
            # Time complexity of just the logic without including the time for sorting is O(n)
        # Space complexity = O(n)
        