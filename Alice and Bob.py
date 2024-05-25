import numpy as np
import math

class Vector:
    def __init__(self, scale_factor, x_angle, y_angle, z_angle, x_offset, y_offset, z_offset, size_factor=None):
        self.scale_factor = scale_factor
        self.x_angle = x_angle
        self.y_angle = y_angle
        self.z_angle = z_angle
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.z_offset = z_offset
        self.size_factor = size_factor

class Alice:
    def __init__(self, grid_type=1, dimensions=3, point_directionality=1):
        self.grid_type = grid_type
        self.dimensions = dimensions
        self.point_directionality = point_directionality
        self.vectors = []

    def add_vector(self, vector):
        self.vectors.append(vector)

    def share_info(self):
        return {
            'grid_type': self.grid_type,
            'dimensions': self.dimensions,
            'point_directionality': self.point_directionality,
            'vectors': self.vectors
        }

class Bob:
    def __init__(self):
        self.current_position = np.zeros(3)
        self.circular_buffer = []
        self.buffer_size = 100

    def apply_vector(self, vector):
        # Convert angles to radians
        x_rad = math.radians(vector.x_angle)
        y_rad = math.radians(vector.y_angle)
        z_rad = math.radians(vector.z_angle)
        
        # Calculate the new position based on vector
        new_position = np.array([
            vector.scale_factor * math.cos(x_rad) + vector.x_offset,
            vector.scale_factor * math.cos(y_rad) + vector.y_offset,
            vector.scale_factor * math.cos(z_rad) + vector.z_offset
        ])
        
        # Update current position
        self.current_position += new_position

        # Add to circular buffer
        if len(self.circular_buffer) >= self.buffer_size:
            self.circular_buffer.pop(0)
        self.circular_buffer.append(new_position)
    
    def sample_grid(self):
        # For simplicity, we'll assume a small grid and a basic Hilbert curve implementation
        # This is a placeholder for the actual logic you described
        pass

def main():
    # Alice's setup
    alice = Alice()
    alice.add_vector(Vector(1, 45, 45, 45, 0, 0, 0))
    alice.add_vector(Vector(2, 90, 90, 90, 1, 1, 1))
    shared_info = alice.share_info()

    # Bob's processing
    bob = Bob()
    for vector in shared_info['vectors']:
        bob.apply_vector(vector)
    
    # Sample grid (to be implemented)
    bob.sample_grid()

    # Output current position
    print(f"Bob's current position: {bob.current_position}")
    print(f"Circular buffer: {bob.circular_buffer}")

if __name__ == "__main__":
    main()
