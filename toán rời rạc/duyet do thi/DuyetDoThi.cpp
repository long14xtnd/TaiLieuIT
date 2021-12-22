#include <bits/stdc++.h>
using namespace std;
const char ginp[]="DT.IN1";
int a[101][101]; 
int n, cx[101], Q[101],v, s;
void init()
{
	freopen(ginp, "r", stdin);
    //Doc du lieu vao
    cin>>n; 
    for (int i=1; i<=n; i++)
   		for (int j=1; j<=n; j++) cin>>a[i][j];
   	//in ma tran ke
   	cout<<"So dinh: "<<n<<"\n";
   	cout<<"Ma tran ke cua do thi:"<<"\n";
   	for (int i=1; i<=n; i++)
   	    { 
		   for (int j=1; j<=n; j++) cout<<a[i][j]<<" ";
   		   cout<<"\n";
   		}
}
void DFS(int u)
{
    cout << u <<" ";//in ra dinh u
    cx[u] = 1;//danh dau dinh da tham
    for (int v = 1; v <= n; v++)
        if (a[u][v] == 1 && cx[v]==0) DFS(v);
}
 
void BFS(int u)
{
	int v, dau=1, cuoi=1;
	Q[cuoi]=u; cx[u]=1;
	while (dau<=cuoi)
	{
		v=Q[dau]; dau++;
		cout << v <<" ";
		for (int j=1; j<=n; j++)
		    if (a[v][j]==1 && cx[j]==0)
		       {cuoi++; Q[cuoi]=j; cx[j]=1; }
	}
}

int main()
{
    init();
    s=1; //dinh bat dau
    //Khoi tao các dinh deu chua tham	
   	for (int i = 1; i <= n; i++) cx[i] = 0;
    cout<<"Duyet theo chieu sau bat dau tu dinh "<<s<<": \n";
    DFS(s);
    cout<<"\n";
    
    //Khoi tao các dinh deu chua tham	
   	for (int i = 1; i <= n; i++) cx[i] = 0;
    cout<<"Duyet theo chieu rong bat dau tu dinh "<<s<<": \n";
    BFS(s);
    
    return 0;
}
