#include "MatrixGraph.h"
#include "tabu_search.h"

#include <cstdlib>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <string>
#include <iostream>
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

void print_sol_to_file(std::vector<std::vector<int>> &sol, std::ostream &f)
{
    for (int i = 0; i < sol.size(); i++)
    {
        f << i << ": ";
        for (auto v : sol.at(i))
        {
            f << v << " ";
        }
        f << "\n";
    }
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
   // printf("%d\n", argc);
    std::string file_path = "gc1000.txt";
    int number_of_neighbours = 50;
    int number_of_iterations = 500000;
    if (argc == 2)
    {
        file_path = argv[1];
        //printf("%d\n", argc);
    }
    else if (argc == 4)
    {
        file_path = argv[1];
        number_of_neighbours = std::atoi(argv[2]);
        number_of_iterations = std::atoi(argv[3]);
        //printf("%d\n", argc);
    }
    
   // printf("%d\n", argc);
    MatrixGraph G = MatrixGraph::get_graph_from_instance_file(file_path, false);
    //G.print_graph_to_file();

    std::string f_out;
    bool double_dot_found = false;
    for (int i = 0; i < file_path.length() - 1; i++)
    {
        if (file_path[i] != '.')
        {
            f_out += file_path[i];
            double_dot_found = false;
        }
        else if (file_path[i+1] == '.')
        {
            f_out += file_path[i];
            double_dot_found = true;
        }
        else
        {
            if (double_dot_found)
            {
                f_out += file_path[i];
                continue;
            }
            break;
        }
    }
    f_out += "_out.txt";
    std::ofstream f(f_out);

    std::vector<std::vector<int>> r;
    std::vector<std::vector<int>> sol = greedy_coloring(G);

    //f.open(f_out);                  // Print greedy solution
    print_sol_to_file(sol, f);
    f.close();

    //auto start = std::chrono::high_resolution_clock::now();
    for(int greedy_count = sol.size()-1; greedy_count > 1; greedy_count--)
    {
        auto temp = sol;
        auto min = std::min_element(temp.begin(), temp.end(), [](const auto &a, const auto &b){return a.size() < b.size();});
        std::iter_swap(min, temp.end()-1);
        for(int i = 0; i < temp[temp.size() - 1].size(); i++)
        {
            temp[i%(temp.size() - 1)].push_back(temp[temp.size() - 1][i]);
        }
        temp.pop_back();
        r = tabu_search(G, greedy_count, temp, 7, number_of_neighbours, number_of_iterations);
        if (!r.empty())
        {
            sol = r;
            f.open(f_out);
            print_sol_to_file(sol, f);
            f.close();
            std::cout << greedy_count << std::endl;
        }
        else
        {
            break;
        }
    }




    //f << "Best solution found for k = " << sol.size() << "\n";

    // for (int i = 0; i < sol.size(); i++)
    // {
    //     std::cout << i << ": ";
    //     for (auto v : sol.at(i))
    //     {
    //         std::cout << v << " ";
    //     }
    //     std::cout << std::endl;
    // }
    // std::cout << "Best solution found for k = " << sol.size() << std::endl;

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
