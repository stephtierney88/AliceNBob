import numpy as np
import math

class Vector:
    def __init__(self, scale_factor, x_angle, y_angle, z_angle, x_offset, y_offset, z_offset):
        self.scale_factor = scale_factor
        self.x_angle = x_angle
        self.y_angle = y_angle
        self.z_angle = z_angle
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.z_offset = z_offset

class Alice:
    def __init__(self):
        self.vectors = []

    def add_vector(self, vector):
        self.vectors.append(vector)

    def share_info(self):
        return self.vectors

class Bob:
    def __init__(self):
        self.current_position = np.zeros(3)
        self.circular_buffer = []
        self.buffer_size = 100

    def apply_vector(self, vector):
        x_rad = math.radians(vector.x_angle)
        y_rad = math.radians(vector.y_angle)
        z_rad = math.radians(vector.z_angle)
        
        new_position = np.array([
            vector.scale_factor * math.cos(x_rad) + vector.x_offset,
            vector.scale_factor * math.cos(y_rad) + vector.y_offset,
            vector.scale_factor * math.cos(z_rad) + vector.z_offset
        ])
        
        self.current_position += new_position

        if len(self.circular_buffer) >= self.buffer_size:
            self.circular_buffer.pop(0)
        self.circular_buffer.append(new_position)

    def sample_grid(self):
        pass

def main():
    alice = Alice()
    
    initial_scale_factor = 1000000  # Large initial scale factor
    for i in range(3):
        vector = Vector(initial_scale_factor, 45, 45, 45, 0, 0, 0)
        alice.add_vector(vector)
        initial_scale_factor /= 2  # Decrease scale factor for subsequent vectors

    shared_vectors = alice.share_info()

    bob = Bob()
    for vector in shared_vectors:
        bob.apply_vector(vector)

    print(f"Bob's current position: {bob.current_position}")
    print(f"Circular buffer: {bob.circular_buffer}")

if __name__ == "__main__":
    main()
