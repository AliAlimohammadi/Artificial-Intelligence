/*
	  Author:	Ali Alimohammadi
	    Date:	11/11/2020
	    Task:	Solving N-Queen using Genetic Algorithm
	Comments:	Hard-coded for 8x8 chess, can be modified for arbitrary size.
*/

#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <map>
#include <vector>
#include <ctime>

using namespace std;

// An arrengement of Queens on the chess board
typedef struct
{
	string arrangement;
	int cost;
} individual;

typedef vector<individual*> population_type;

population_type population;
int N;

// Set how many initial chromosomes are generated
int initialPopulationCount = 10;

int fitnessValue(string arrangement)
{
	// Initialize to a solution
	int fitness = (N * (N - 1)) / 2;
	
	// Removing pairs that lie on the same row and on the same diagonal
	for (int i = 0; i < N; i++)
		for (int j = i + 1; j < N; j++)
			if ((arrangement[i] == arrangement[j])
				|| (i - arrangement[i] == j - arrangement[j])
				|| (i + arrangement[i] == j + arrangement[j]))
				fitness--;
	return fitness;
}

individual* createNode()
{
	individual *newNode = new individual;
	return newNode;
}

void populate()
{
	string sampleArrangement = "";
	individual *temp;
	for (int i = 1; i <= N; i++)
	{
		ostringstream ostr;
		ostr << i;
		sampleArrangement += ostr.str();
	}
	// Adds entries to population list
	for (int i = 0; i < initialPopulationCount; i++)
	{
		random_shuffle(sampleArrangement.begin(), sampleArrangement.end());
		temp = createNode();
		temp->arrangement = sampleArrangement;
		temp->cost = fitnessValue(sampleArrangement);
		population.push_back(temp);
	}
}

individual* reproduce(individual *x, individual *y)
{
	individual *child = createNode();
	// Pick a random spliting point
	int crossOver = rand() % N;
	// Sequence the genome
	child->arrangement = (x->arrangement).substr(0, crossOver) +
						 (y->arrangement).substr(crossOver, N - crossOver + 1);
	child->cost = fitnessValue(child->arrangement);
	return child;
}

individual* mutate(individual *child)
{
	int randomQueen = rand() % N + 1;
	int randomPosition = rand() % N + 1;
	// Put a random Queen in a random position
	// Add 48 to random postion to get ascii code
	child->arrangement[randomQueen] = randomPosition + 48;
	return child;
}

int randomSelection()
{
	// Extra randomness
	int randomPos = rand() % population.size() % 2;
	return randomPos;
}

bool isFit(individual *test)
{
	// Check if it acquired maximum fitness point
	if (fitnessValue(test->arrangement) == ((N * (N - 1)) / 2))
		return true;
	return false;
}

bool compareCost(individual *x, individual *y)
{
	return x->cost > y->cost;
}

individual* GeneticAlgorithm()
{
	int randomNum1, randomNum2;
	individual *individualX, *individualY, *child;
	bool found = false;
	child = NULL;
	while (!found)
	{
		population_type new_population;
		for (unsigned int i = 0; i < population.size(); i++)
		{
			sort(population.begin(), population.end(), compareCost);

			randomNum1 = randomSelection();
			individualX = population[randomNum1];

			randomNum2 = randomSelection();
			individualY = population[randomNum2];

			child = reproduce(individualX, individualY);

			// Random probability of mutation
			if (!(rand() % 2))
				child = mutate(child);

			if (isFit(child))
			{
				found = true;
				return child;
			}
			new_population.push_back(child);
		}
		population = new_population;
	}
	return child;
}

void initialize()
{
	// Initialize randomness
	srand((unsigned int)time(NULL));
	// Set 'N'
	N = 8;
}

int main()
{
	initialize();

	// Declare timestamp variables to keep a track of the time spent for computing
	clock_t start_time, end_time;

	// Keep track of soultions to check their uniqueness
	map<string, bool> solutions;

	// We already know that there are exactly 92 solutions for 8-Queens Problem.
	const int maxSolutions = 92;
	int found = 0;
	
	// Start the timer
	start_time = clock();
	while (found != maxSolutions)
	{
		populate();
		individual *solution = GeneticAlgorithm();
		
		// Check if solution is already found
		if (!solutions[solution->arrangement])
		{
			// Mark it as "FOUND"
			solutions[solution->arrangement] = true;

			// Print the solution
			cout << "Solution #" << ++found << ":\t" << solution->arrangement << endl;
			cout << "\n # ";
			// Print column indices
			for (int i = 0; i < N; i++)
				cout << ' ' << i + 1 << ' ';
			cout << endl;

			for (int i = 0; i < N; i++)
			{
				// Print row index
				cout << ' ' << i + 1 << ' ';

				for (int j = 0; j < solution->arrangement[i] - '0' - 1; j++)
					cout << " - ";
				cout << " Q ";
				for (int j = solution->arrangement[i] - '0'; j < N; j++)
					cout << " - ";
				cout << endl;
			}
			cout << endl;
		}
	}
	// Stop the timer
	end_time = clock();

	// Report the execution time
	cout << "\nExecution Time:\t" << 1000 * ((double)(end_time - start_time) / CLOCKS_PER_SEC) << " milliseconds" << endl;

	return 0;
}