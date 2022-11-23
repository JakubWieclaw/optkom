#pragma once

#include <iostream>
#include <vector>
#include <string>
#include <fstream>

class MatrixGraph
{
public:
    void initialize(unsigned int n)
    {
        v = std::vector<std::vector<int>>(n, std::vector<int> (n, 0));
        size = n;
    }
    void add_edge(unsigned int row, unsigned int col)
    {
        if (row == col)
        {
            std::cout << "Row == Col - you probably don't wanna do that" << std::endl;
            return;
        }
        if (v[row][col] != 0)
        {
            std::cout << "Edge already Exists";
            return;
        }
        v[row][col] = 1;
        v[col][row] = 1;
        edge_count++;
    }
    std::vector<int> get_neighbours(unsigned int node)
    {
        std::vector<int> res;
        if (node > size)
        {
            std::cout << "This node does not exist" << std::endl;
            return res;
        }

        for (int i = 0; i < size; i++)
        {
            if (v[node][i])
            {
                res.push_back(i);
            }
        }
        return res;
    }
    unsigned int get_size()
    {
        return size;
    }
    void get_graph_from_instance_file(char* file_name)
    {
        std::ifstream f(file_name);
        std::string line;
        getline(f, line);
        size = stoi(line);
        initialize(size);

        while (getline(f, line))
        {
            int i = 0;
            std::string x_line;
            while(!isspace(line[i]))
            {
                x_line.push_back(line[i]);
                i++;
            }
            i++;
            std::string y_line;
            while (i < line.length())
            {
                y_line.push_back(line[i]);
                i++;
            }
            unsigned int x = stoi(x_line);
            unsigned int y = stoi(y_line);
            add_edge(--x,--y); //Not indexed from 0
        }

    }
    void print_graph_to_file()
    {
        FILE * f = freopen("cpp_graph.txt", "w", stdout);
        for (int i = 0; i< size; i++)
        {
            for (int j = 0; j< size; j++)
            {
                std::cout << v[i][j] << " ";
            }
            std::cout << std::endl;
        }
        fclose(f);
    }

private:
    std::vector<std::vector<int>> v;
    unsigned int edge_count = 0;
    unsigned int size = 0;
};

int main()
{
    MatrixGraph G;
    // G.initialize(20);
    // G.add_edge(0,1);
    G.get_graph_from_instance_file("mycie14.txt");
    G.print_graph_to_file();
    return 0;
}