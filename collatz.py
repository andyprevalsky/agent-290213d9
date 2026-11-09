#!/usr/bin/env python3
"""Print the Collatz sequence starting at 27 and its total number of steps."""


def collatz(n):
    """Return the Collatz sequence from n through the first 1."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz(27)
    for value in sequence:
        print(value)
    total_steps = len(sequence) - 1
    print(f"Total steps: {total_steps}")


if __name__ == "__main__":
    main()
