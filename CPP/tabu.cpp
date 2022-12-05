#include "tabu_search.h"
#include <algorithm>
std::vector<Conflict> how_many_conflicts(const MatrixGraph &G, const std::vector<std::vector<int>> &solution)
{
    int result = 0;
    std::vector<Conflict> conflicts;
    for (int i = 0; i < solution.size(); i++)
    {
        const auto &x = solution[i];
        for (int y : x)
        {
            for (int z : x)
            {
                if (z > y) // Don't count conflicts twice
                {
                    if (G.edge_exists(y, z))
                    {
                        conflicts.push_back(
                            {{y, z},
                             i});
                    }
                }
            }
        }
    }
    return conflicts;
}

std::vector<std::vector<int>> tabu_search(MatrixGraph G, int k_number_of_colours, std::vector<std::vector<int>> solution, int tabu_size, int number_of_neighbours, int max_iterations)
{
    int current_iteration = 0;
    std::deque<std::pair<int, int>> tabu;
    bool solution_found = false;

    std::random_device rd;
    std::mt19937 gen(rd());
    while (current_iteration < max_iterations)
    {
        auto conflitcs = how_many_conflicts(G, solution);
        if (conflitcs.size() == 0)
        {
            solution_found = true;
            break;
        }
        current_iteration++;
        bool so_far_best_solution_found = false;
        if (tabu.size() > tabu_size)
        {
            //tabu.erase(std::remove(tabu.begin(), tabu.end(), tabu[0]), tabu.end());
            tabu.pop_back();
        }

        
        

        std::vector<std::vector<int>> best_proposed_solution;
        int best_conflicts = 0;
        std::pair<int, int> move{0, 0};
        bool is_any_solution_found = false;
        bool in_tabu = false;
        int vertex, colour;
        Conflict conflict;
        for (int i = 0; i < number_of_neighbours; i++)
        {
            // Choose random conflict
            do
            {
                std::uniform_int_distribution<> distr(0, conflitcs.size() - 1);
                int id = distr(gen);
                conflict = conflitcs[id];

                // Chose random element from conflict
                std::uniform_int_distribution<> pair_id_distr(0, 1);
                int pair_id = pair_id_distr(gen);
                vertex = conflict.node[pair_id]; // This is node that we have ultimately chosen

                std::uniform_int_distribution<> colour_distr(0, k_number_of_colours - 2); // Choosing new colour
                colour = colour_distr(gen);
                if (colour == conflict.colour)
                {
                    colour = k_number_of_colours - 1; // Other than we already have
                }

                std::pair<int, int> m{vertex, colour};
                for (auto el:tabu)
                {
                    if (el == m)
                    {
                        in_tabu = true;
                        break;
                    }
                }
            }
            while (in_tabu);
            

            std::vector<std::vector<int>> proposed_solution = solution;
            proposed_solution[colour].push_back(vertex); // Add vertex to its new colour
            proposed_solution[conflict.colour].erase(std::remove(proposed_solution[conflict.colour].begin(), proposed_solution[conflict.colour].end(), vertex), proposed_solution[conflict.colour].end());
            // Aaaaaaand we remove this vertex from its previous colour - don't ask how it works

            auto proposed_solution_conflicts = how_many_conflicts(G, proposed_solution);

            if (proposed_solution_conflicts.size() < conflitcs.size())
            {
                solution = proposed_solution;
                tabu.push_front({vertex, conflict.colour});
                so_far_best_solution_found = true;
                break;
            }

            if (!is_any_solution_found)
            {
                best_proposed_solution = proposed_solution;
                best_conflicts = proposed_solution_conflicts.size();
                move = {vertex, conflict.colour};
                is_any_solution_found = true;
            }
            else if (proposed_solution_conflicts.size() < best_conflicts)
            {
                best_proposed_solution = proposed_solution;
                best_conflicts = proposed_solution_conflicts.size();
                move = {vertex, conflict.colour};
            }
        }
        if (!so_far_best_solution_found)
        {
            tabu.push_front(move);
            solution = best_proposed_solution; // Todo - best proposed solutions conflicts, optymalizacja
        }
    }


    if (solution_found)
    {
        return solution;
    }
    else
    {
        return {};
    }
}