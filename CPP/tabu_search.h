#pragma once

#include <iostream>
#include "MatrixGraph.h"
#include <queue>
#include <random>
#include <optional>

struct Conflict
{
    int node[2];
    int colour;
};
std::vector<Conflict> how_many_conflicts(const MatrixGraph &G,const std::vector<std::vector<int>> &solution);
std::vector<std::vector<int>> tabu_search(MatrixGraph G, int k_number_of_colours, std::vector<std::vector<int>> solution, int tabu_size = 7, int number_of_neighbours = 10, int max_iterations = 100000);