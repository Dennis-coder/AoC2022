#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

vector< vector<int> > parse() {
    ifstream dataFile("indata.txt");
    vector< vector<int> > data;
    vector<int> round;
    char a, b;

    while (dataFile >> a >> b) {
        round.push_back((int) a - 65);
        round.push_back((int) b - 88);
        data.push_back(round);
        round.clear();
    }
    return data;
}

int part1(vector< vector<int> > data) {
    int op, you, score = 0;
    for (int i = 0; i < data.size(); i++) {
        op = data[i][0];
        you = data[i][1];
        
        score += you + 1;
        if ((op + 1) % 3 == you) {
            score += 6;
        } else if (op == you) {
            score += 3;
        }
    }
    return score;
}

int part2(vector< vector<int> > data) {
    int op, res, score = 0;
    for (int i = 0; i < data.size(); i++) {
        op = data[i][0];
        res = data[i][1];

        score += res * 3;
        if (res == 2) {
            score += (op + 1) % 3 + 1;
        } else if (res == 1) {
            score += op + 1;
        } else {
            score += (op + 2) % 3 + 1;
        }
    }
    return score;
}

int main () {
    vector< vector<int> > data = parse();
    int part1_res = part1(data);
    int part2_res = part2(data);

    cout << part1_res << endl << part2_res << endl;

    return 0;
}