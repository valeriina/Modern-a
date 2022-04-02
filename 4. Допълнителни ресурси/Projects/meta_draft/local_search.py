from Other.Projects.meta_draft.utils import generate_random_solution, estimate_solution, mutate_solution


def local_search(target, number_of_iterations):
    solution = generate_random_solution(target)
    estimation = estimate_solution(target, solution)
    print("Initial Solution: {} -> {}".format(solution, estimation))

    for _ in range(number_of_iterations):
        new_solution = mutate_solution(solution)
        new_estimation = estimate_solution(target, new_solution)
        if new_estimation < estimation:
            solution = new_solution
            estimation = new_estimation
        print("Next Solution: {} -> {}".format(solution, estimation))

    print("Best Solution: {} -> {}".format(solution, estimation))