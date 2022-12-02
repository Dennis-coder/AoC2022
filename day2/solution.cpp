#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main () {
    ifstream dataFile("indata.txt");
    vector< vector<int> > data;
    vector<int> round;
    char a, b;
    int op, you, res, score;
    
    // Parse input
    while (dataFile >> a >> b) {
        round.push_back((int) a - 65);
        round.push_back((int) b - 88);
        data.push_back(round);
        round.clear();
    }

    // Part 1
    score = 0;
    for (int i = 0; i < data.size(); i++) {
        op = data[i][0];
        you = data[i][1];
        
        score = score + you + 1;
        if ((op + 1) % 3 == you) {
            score = score + 6;
        } else if (op == you) {
            score = score + 3;
        }
    }
    cout << score << endl;

    // Part 2
    score = 0;
    for (int i = 0; i < data.size(); i++) {
        op = data[i][0];
        res = data[i][1];

        score = score + res * 3;
        if (res == 2) {
            score = score + (op + 1) % 3 + 1;
        } else if (res == 1) {
            score = score + op + 1;
        } else {
            score = score + (op + 2) % 3 + 1;
        }
    }
    cout << score << endl;

    return 0;
}