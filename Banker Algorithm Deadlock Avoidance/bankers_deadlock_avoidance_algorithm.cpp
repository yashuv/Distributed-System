#include <iostream>
#include <cstdlib>
#define n 3
#define m 4
using namespace std;

void computeNeed(int need[n][m], int maximum[n][m], int allocated[n][m]);

bool isSystemSafe(int process[n], int available[m], int maximum[n][m], int allocated[n][m]);

int main()
{
  // Total number of processes
  int process[n] = {0, 1, 2};

  // Available units of resources
  int available[m] = {3, 1, 1, 2};

  // Maximum units of resources that can be allocated to processes
  int maximum[n][m] = {{3, 3, 2, 2},
                       {1, 2, 3, 4},
                       {1, 3, 5, 0}};

  // Resources currently allocated to processes
  int allocated[n][m] = {{1, 2, 2, 1},
                         {1, 0, 3, 3},
                         {1, 2, 1, 0}};

  // Check whether the system is in safe state or not
  isSystemSafe(process, available, maximum, allocated);

  return 0;
}

void computeNeed(int need[n][m], int maximum[n][m], int allocated[n][m])
{

  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      need[i][j] = maximum[i][j] - allocated[i][j];
}

bool isSystemSafe(int process[n], int available[m], int maximum[n][m], int allocated[n][m])
{
  int i, j, k;
  bool flag;

  int need[n][m];

  // First we compute need
  computeNeed(need, maximum, allocated);

  // Initially all processes are marked as unfinished
  bool finished[n] = {false};

  // Array to store the safe sequence of execution
  int safeSequence[n];

  // Since we will be mutating available array,
  // we make its copy and work on that copy
  int copyAvailable[m];
  for (i = 0; i < m; i++)
    copyAvailable[i] = available[i];

  int count = 0;
  while (count < n)
  {
    // Find a process which is unfinished and whose need can be
    // satisfied from current available resources
    flag = false;
    for (i = 0; i < n; i++)
    {
      if (!finished[i])
      {
        // Check if all of the process need
        // is less than available
        for (j = 0; j < m; j++)
          if (need[i][j] > copyAvailable[j])
            break;
        // If all of the process need are less
        // than what is available
        if (j == m)
        {
          // This means that the process can finish
          // its execution and when it finishes then
          // we can free the resources it was using
          for (k = 0; k < m; k++)
            copyAvailable[k] += allocated[i][k];

          // This process can be executed safely
          safeSequence[count++] = i;

          // This process is finished
          finished[i] = true;

          flag = true;
        }
      }
    }
    if (flag == false)
    {
      cout << "System is not in a safe state " << endl;
      return false;
    }
  }
  cout << "System is in safe state.\nSafe sequence is: ";
  for (int i = 0; i < n; i++)
    cout <<'P' << safeSequence[i] << "\t";
  return true;
}
