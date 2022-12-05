#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <chrono>

using namespace std;
using namespace std::chrono;

vector<string> parse() {
    ifstream dataFile("indata.txt");
    vector<string> data;
    string line;
    while (getline(dataFile, line)) {
        data.push_back(line);
    }
    return data;
}

int part1(vector<string> data) {
    int prio_sum = 0;
    for (int i = 0; i < data.size(); i++) {
        string comp1 = data[i].substr(0, data[i].size() / 2);
        string comp2 = data[i].substr(data[i].size() / 2);
        sort(comp1.begin(), comp1.end());
        sort(comp2.begin(), comp2.end());
        string intersection;
        set_intersection(comp1.begin(), comp1.end(), comp2.begin(), comp2.end(), back_inserter(intersection));
        prio_sum += (int) intersection[0] - ((int) intersection[0] <= 90 ? 38 : 96);
    }
    return prio_sum;
}

int part2(vector<string> data) {
    int prio_sum = 0;
    for (int i = 0; i < data.size(); i += 3) {
        string bag1 = data[i];
        string bag2 = data[i + 1];
        string bag3 = data[i + 2];
        sort(bag1.begin(), bag1.end());
        sort(bag2.begin(), bag2.end());
        sort(bag3.begin(), bag3.end());
        string intersection1;
        set_intersection(bag1.begin(), bag1.end(), bag2.begin(), bag2.end(), back_inserter(intersection1));
        string intersection2;
        set_intersection(intersection1.begin(), intersection1.end(), bag3.begin(), bag3.end(), back_inserter(intersection2));
        prio_sum += (int) intersection2[0] - ((int) intersection2[0] <= 90 ? 38 : 96);
    }
    return prio_sum;
}

int main () {
    auto start = high_resolution_clock::now();
    vector<string> data = parse();
    auto stop = high_resolution_clock::now();
    auto parse_time = duration_cast<microseconds>(stop - start).count();

    start = high_resolution_clock::now();
    int part1_res = part1(data);
    stop = high_resolution_clock::now();
    auto part1_time = duration_cast<microseconds>(stop - start).count();

    start = high_resolution_clock::now();
    int part2_res = part2(data);
    stop = high_resolution_clock::now();
    auto part2_time = duration_cast<microseconds>(stop - start).count();

    cout << "Part 1 res:  " << part1_res << endl;
    cout << "Part 2 res:  " << part2_res << endl;
    cout << "Parse time:  " << parse_time << "us" << endl;
    cout << "Part 1 time: " << part1_time << "us" << endl;
    cout << "Part 2 time: " << part2_time << "us" << endl;
    cout << "Total time:  " << parse_time + part1_time + part2_time << "us" << endl;
    
    return 0;
}