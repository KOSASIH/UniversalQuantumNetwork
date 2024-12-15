from src.ai_integration.ai_optimizer import AIOptimizer

def main():
    # Demo for AI integration
    def objective_function(x):
        return (x - 2) ** 2

    optimizer = AIOptimizer(objective_function)
    optimal_value = optimizer.optimize(initial_guess=[0])
    print("Demo AI Integration: Optimal Value:", optimal_value)

if __name__ == "__main__":
    main()
