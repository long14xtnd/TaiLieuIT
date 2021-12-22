#include <iostream>
using namespace std;

string _characterString;
int _totalCharacters, _count;

void lietkehoanvi(string a, int l, int r)
{
    // In ra chuoi string
    if (l == r) {
        _count++;
        cout <<_count <<". ";
        cout<<a<<endl;
    }
    else
    {
        // Liet ke hoan vi chuoi string duoc nhap
        for (int i = l; i < r; i++)
        {
            // Hoán đổi giá trị của hai biến a[l] và a [i]
            swap(a[l], a[i]);
            // Goi lai hàm liet ke hoan vi
            lietkehoanvi(a, l+1, r);
            // Trả lại giá trị của hai biến a[l] và a [i]
            swap(a[l], a[i]);
        }
    }
}
void khoitao() {
    cout <<"Nhap chuoi ki tu = ";
    cin >> _characterString;
    _totalCharacters = _characterString.size();
    lietkehoanvi(_characterString, 0, _totalCharacters);
    _count = 0;
}

int main() {
//    khoitao();
//    char i = [""]
    _count = 0;
    for (char letter = 'A'; letter <= 'Z'; letter++)
    {
        for (int j = 0; j < 10; j++) {
            for (int a = 0; a < 10; a++) {
                for (int b = 0; b < 10; b++) {
                    for (int c = 0; c < 10; c++) {
                        for (int d = 0; d < 10; d++) {
                            _count++;
                            cout <<_count <<". ";
                            cout<<"29"<<letter<<j<<"-"<<a<<b<<c<<d<<endl;
                        }
                    }
                }
            }
        }
    }
    
    return 0;
}


//#include <iostream>
//using namespace std; int n, m, dem, a[15];
//void khoitao()
//{ cout <<"Nhap n= "; cin >> n; cout <<"Nhap m= "; cin >> m;
//dem=0; a[0]=0; }
//void xuat()
//{
//dem++; cout <<dem <<". "; for (int j=1; j<=m; j++)
//cout<< a[j]<<" "; cout << endl;
//}
//void Try(int i) {
//for (int j=a[i-1]+1; j<=n-m+i; j++) {
//a[i]=j;
//if (i==m) xuat(); else
//Try(i+1); }
//}
//int main()
//{
//khoitao();
//Try(1); }
