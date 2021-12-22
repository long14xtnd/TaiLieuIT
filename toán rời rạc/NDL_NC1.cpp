//Nhanh can 
#include <bits/stdc++.h>
using namespace std;
const char ginp[]="TSP.IN5";

const int maxN=100;
int n;
int c[maxN+1][maxN+1];
int x[maxN],kq[maxN];
bool cx[maxN+1];
long Min,cp, Cmin;
void khoitao()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    freopen(ginp, "r", stdin);
    //Doc du lieu vao
    cin>>n; 
    for (int i=1; i<=n; i++)
   		for (int j=1; j<=n; j++) cin>>c[i][j];
   	//In du lieu
	cout<<"So thanh pho n = "<<n<<endl;
	cout<<"Ma tran chi phi: "<<endl;
    for (int i=1; i<=n; i++)
    	{
    		for (int j=1; j<=n; j++) cout<<c[i][j]<<' ';
    		cout<<endl;
		}
	cout<<endl;
    for (int i=1; i<=n; i++) cx[i]=1;
    x[1]=1; cx[1]=0;
    Min=1000000000;
    cp=0;
    //Tim phan tu nho nhat cua ma tran chi phi c
	Cmin=1000000000;
    for (int i=1; i<=n; i++)
        for (int j=1; j<=n; j++)
            if (c[i][j] != 0 && c[i][j] < Cmin) Cmin=c[i][j];
}

void capnhat()
{
    if (cp + c[x[n]][1] < Min)
    {
        Min= cp + c[x[n]][1];
        for (int i=1; i<=n; i++) kq[i]=x[i];
    }
}
void Try(int i)
{
    for (int j=2; j<=n; j++)
    if (cx[j])
    {
        x[i]=j;
        cp=cp+c[x[i-1]][j];
        cx[j]=0;
        if (i==n) capnhat(); 
		else 
		    if (cp + (n-i+1) * Cmin < Min) 
		      Try(i+1);
        cx[j]=1;
        cp=cp-c[x[i-1]][j];
    }
}
void inkq()
{
    cout<<"Hanh trinh co chi phi nho nhat:"<<Min<<endl;
    cout<<"Thu tu tham cac thanh pho:"<<endl;
    for (int i=1; i<=n; i++) cout<<kq[i]<<" --> ";
    cout<<1<<endl;
}
int main()
{
    khoitao();
    Try(2);
    inkq();
}
