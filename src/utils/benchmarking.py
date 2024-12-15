import time

class Benchmarking:
    @staticmethod
    def time_function(func, *args, **kwargs):
        """Time the execution of a function."""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds.")
        return result

if __name__ == "__main__":
    def sample_function(n):
        """Sample function to demonstrate benchmarking."""
        return sum(range(n))

    result = Benchmarking.time_function(sample_function, 1000000)
    print("Result of sample function:", result)
