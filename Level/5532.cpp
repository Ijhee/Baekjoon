#include <iostream>

using namespace std;

int main()
{
	int L, A, B, C, D; 
	int hwDay = 0; 

	bool kor = false, math = false;

	cin >> L >> A >> B >> C >> D;
	

	while (1)
	{
		if (A > 0)
		{
			A -= C;
			kor = true;
		}
		if (B > 0)
		{
			B -= D;
			math = true;
		}
		if (kor || math) hwDay++;
		else break;
		kor = false;
		math = false; 
	}

	cout << L - hwDay;
}
