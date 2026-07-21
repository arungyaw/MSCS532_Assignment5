import csv
import random
import time


def partition(values, low, high):
    # Partition the list using the last element as the pivot.
    pivot = values[high]
    smaller_index = low - 1

    # Move values smaller than or equal to the pivot to the left side.
    for current_index in range(low, high):
        if values[current_index] <= pivot:
            smaller_index += 1
            values[smaller_index], values[current_index] = (
                values[current_index],
                values[smaller_index],
            )

    # Place the pivot in its correct sorted position.
    pivot_index = smaller_index + 1
    values[pivot_index], values[high] = values[high], values[pivot_index]
    return pivot_index


def deterministic_quicksort(values, low, high):
    # Sort a list using deterministic Quicksort.
    if low < high:
        pivot_index = partition(values, low, high)

        # Recursively sort the values before and after the pivot.
        deterministic_quicksort(values, low, pivot_index - 1)
        deterministic_quicksort(values, pivot_index + 1, high)


def randomized_partition(values, low, high):
    # Choose a random pivot and partition the list.
    random_pivot_index = random.randint(low, high)

    # Move the randomly selected pivot to the end.
    values[random_pivot_index], values[high] = (
        values[high],
        values[random_pivot_index],
    )

    return partition(values, low, high)


def randomized_quicksort(values, low, high):
    # Sort a list using randomized Quicksort.
    if low < high:
        pivot_index = randomized_partition(values, low, high)

        # Recursively sort the values before and after the pivot.
        randomized_quicksort(values, low, pivot_index - 1)
        randomized_quicksort(values, pivot_index + 1, high)


def create_dataset(size, distribution):
    # Create a dataset based on the selected distribution.
    if distribution == "random":
        return [random.randint(1, size * 10) for _ in range(size)]

    if distribution == "sorted":
        return list(range(size))

    if distribution == "reverse_sorted":
        return list(range(size, 0, -1))

    raise ValueError("Unsupported dataset distribution.")


def measure_sorting_time(sort_function, data):
    # Measure the execution time of a sorting function.
    values = data.copy()
    start_time = time.perf_counter()

    sort_function(values, 0, len(values) - 1)

    end_time = time.perf_counter()

    # Confirm that the algorithm sorted the values correctly.
    if values != sorted(data):
        raise ValueError("The sorting algorithm produced an incorrect result.")

    return end_time - start_time


def run_experiments():
    # Compare deterministic and randomized Quicksort.
    input_sizes = [100, 250, 500, 750, 900]
    distributions = ["random", "sorted", "reverse_sorted"]
    repetitions = 3
    results = []

    for size in input_sizes:
        for distribution in distributions:
            deterministic_times = []
            randomized_times = []

            for _ in range(repetitions):
                dataset = create_dataset(size, distribution)

                deterministic_times.append(
                    measure_sorting_time(deterministic_quicksort, dataset)
                )
                randomized_times.append(
                    measure_sorting_time(randomized_quicksort, dataset)
                )

            deterministic_average = sum(deterministic_times) / repetitions
            randomized_average = sum(randomized_times) / repetitions

            results.append(
                {
                    "input_size": size,
                    "distribution": distribution,
                    "deterministic_time_seconds": deterministic_average,
                    "randomized_time_seconds": randomized_average,
                }
            )

            print(
                f"Size: {size:>4} | "
                f"Distribution: {distribution:<14} | "
                f"Deterministic: {deterministic_average:.8f} seconds | "
                f"Randomized: {randomized_average:.8f} seconds"
            )

    return results


def save_results(results, filename="quicksort_results.csv"):
    # Save experiment results to a CSV file.
    fieldnames = [
        "input_size",
        "distribution",
        "deterministic_time_seconds",
        "randomized_time_seconds",
    ]

    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to {filename}")


def main():
    # Run the Quicksort empirical analysis.
    random.seed(42)
    results = run_experiments()
    save_results(results)


if __name__ == "__main__":
    main()