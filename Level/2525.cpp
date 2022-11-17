#include <iostream>
using namespace std;

int main() {
	int h = 0, m = 0, new_m = 0;
	int end_h = 0, end_m = 0;
	cin >> h >> m;
	cin >> minutes;

	end_h = h;
	end_m = m + new_m;

	if (end_m > 59) {
		end_h += end_m / 60;
		end_m %= 60;
	}

	end_h %= 24;

	cout << end_h << " " << end_m;
	return 0;
}
