from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Flip the image horizontally.
        flipped_image = [row[::-1] for row in image]
        
        # Invert the image.
        for idx, row in enumerate(flipped_image):
            flipped_image[idx] = [pixel ^ 1 for pixel in row]
        
        return flipped_image
