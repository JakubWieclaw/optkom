#include "MatrixGraph.h"
#include "tabu_search.h"

#include <cstdlib>
#include <algorithm>
#include <numeric>
std::vector<std::vector<int>> propose_solution(MatrixGraph G, int k)
{
    std::vector<std::vector<int>> r(k);
    for (int i = 0; i < k - 1; i++)
    {
        r[i].push_back(i);
    }
    for (int i = k - 1; i < G.get_size(); i++)
    {
        r[k - 1].push_back(i);
    }
    return r;
}

std::vector<std::vector<int>> greedy_coloring(MatrixGraph &G)
{
    auto g_size = G.get_size();
    std::vector<std::vector<int>> colours(g_size);
    std::vector<unsigned int> nodes_degrees(g_size);
    std::vector<int> nodes(g_size);
    std::iota(nodes.begin(), nodes.end(), 0);
    for (int i = 0; i < g_size; i++)
    {
        nodes_degrees[i] = G.get_neighbours(i).size();
    }
    std::sort(nodes_degrees.begin(), nodes_degrees.end(), std::greater<int>());
    std::sort(nodes.begin(), nodes.end(), [&nodes_degrees](int a, int b) { return nodes_degrees[a] > nodes_degrees[b]; });
    int greedy_coloring_count = 0;
    for (int i: nodes)
    {
        for (int j = 0; j < g_size; j++)
        {
            bool cant_assign_colour = false;
            if (colours[j].empty()) // No node has that colour
            {
                greedy_coloring_count++; // Increasing size of result vector
                cant_assign_colour = false;
                colours[j].push_back(i);
                break;
            }
            else // There are nodes with the same colour so we check if we can assign j-th colour
            {
                for (int k = 0; k < colours[j].size(); k++)
                {
                    if (G.edge_exists(i, colours[j][k]))
                    {
                        cant_assign_colour = true;
                        break;
                    }
                }
                if (!cant_assign_colour)
                {
                    colours[j].push_back(i); // We can assign j-th colour
                    cant_assign_colour = false;
                }
            }
            if (cant_assign_colour)
            {
                continue;
            }
            else
            {
                break;
            }
        }
    }
    return std::vector<std::vector<int>> (colours.begin(), colours.begin() + greedy_coloring_count);
}

int main(int argc, char *argv[])
{
    // int k = 5;
    // if (argc > 1)
    // {
    //     k = std::atoi(argv[1]);
    // }
    std::string file_path = "gc1000.txt";
    if (argc == 2)
    {
        file_path = argv[1];
    }
    MatrixGraph G = MatrixGraph::get_graph_from_instance_file(file_path, false);
    G.print_graph_to_file();

    std::vector<std::vector<int>> r;
    std::vector<std::vector<int>> sol = greedy_coloring(G);

    //auto start = std::chrono::high_resolution_clock::now();
    for(int greedy_count = sol.size()-1; greedy_count > 1; greedy_count--)
    {
        auto min = std::min_element(sol.begin(), sol.end(), [](const auto &a, const auto &b){return a.size() < b.size();});
        std::iter_swap(min, sol.end()-1);
        for(int i = 0; i < sol[sol.size() - 1].size(); i++)
        {
            sol[i%(sol.size() - 1)].push_back(sol[sol.size() - 1][i]);
        }
        sol.pop_back();
        r = tabu_search(G, greedy_count, sol, 7, 50, 1000000);
        if (!r.empty())
        {
            sol = r;
            std::cout << greedy_count << std::endl;
        }
        else
        {
            break;
        }
    }

    for (int i = 0; i < sol.size(); i++)
    {
        std::cout << i << ": ";
        for (auto v : sol.at(i))
        {
            std::cout << v << " ";
        }
        std::cout << std::endl;
    }
    std::cout << "Best solution found for k = " << sol.size() << std::endl;

    // }
    // else
    // {
    //     std::cout << "No solution found" << std::endl;
    // }
    return 0;
}

    // for (int i = G.get_size() - 1; i >= k; i--)
    // {
    //     std::cout << i << std::endl;
    //     r = tabu_search(G, i, propose_solution(G, i), 7, 50, 20000);
    //     if (!r.empty())
    //     {
    //         best_solution_size = r.size();
    //         sol = r;
    //     }
    //     else
    //     {
    //         break;
    //     }
    // }

    // if (!sol.empty())
    // {