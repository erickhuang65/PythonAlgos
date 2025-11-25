class Solution:
    def largestAltitude(self, gain):
        max_altitude = 0  # To store the maximum altitude encountered
        # TODO: Write your code here
        current_altitude = 0

        # for i in range(len(gain)):
        #     current_altitude = gain[i] + current_altitude
        #     if current_altitude > max_altitude:
        #         max_altitude = current_altitude

        for i in gain:
            current_altitude += i
            max_altitude = max(current_altitude, max_altitude)
            
        return max_altitude
    
    