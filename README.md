# My Math Projects

## Description

This project is a compilation of many math thing like algo to search the prime numbers, or solving geometric problems. All the formulas, notably the formula for calculating the unknown point, are formulas that I made

## Installation

No specific installation is required. Simply download or clone the repository and run the Python scripts.

## Usage

### Vector Class

The `Vector` class represents a 2D vector with `x` and `y` coordinates. It can be initialized with optional initial coordinates.

### Orthonormal Class

The `Orthonormal` class is used to solve geometric problems involving 3 points in an orthonormal coordinate system. It provides methods to find the position of an unknown point given the distances from it to the known points.

### AlgoToSearch Class

The `AlgoToSearch` class contains algorithms created for recreational purposes. It provides basic math algorithms such as finding prime numbers, pairs of prime numbers, and generating Fibonacci sequences.

## Example

```python
# Example usage of Orthonormal class
unknown_point = Orthonormal((0, 0), (4, 2), (1, 4)).search_z_point_square_arguments(5, 5, 10)
print(unknown_point)  # Output: (2, 1)
