from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Flip the image horizontally.
        image = [row[::-1] for row in image]
        
        # Invert the image.
        for idx, row in enumerate(image):
            image[idx] = [pixel ^ 1 for pixel in row]
        
        return image        
