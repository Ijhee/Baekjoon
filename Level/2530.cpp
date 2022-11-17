#include <iostream>
using namespace std;

int main(){
	int h, m, s, time;
	cin >> h >> m >> s >> time;
	
	s += time;
	m += s / 60;
	h += m / 60;

	cout << h%24 << " " << m%60 << " " << s%60;
}
