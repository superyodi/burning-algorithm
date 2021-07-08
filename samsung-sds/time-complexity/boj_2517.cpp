#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

typedef pair<int, int> pii;

int n;
pii player[500000]; 
int tr[1<<20]; // 1 * 2^20


int seg_sum(int node, int s, int e, int l, int r) {
    if (r <s || e < l) return 0;
    
    if (l <= s && e <= r) return tr[node];
    else return seg_sum(node*2,s,(s+e)/2,l,r) + seg_sum(node*2+1,(s+e)/2+1,e, l,r);
}

void update(int node, int s, int e, int idx, int v) {
    if(idx < s || e < idx) return;
    if (s==e) {
        tr[node] = v;

    }
    else {
        update(node *2, s, (s+e)/2, idx, v);
        update(node *2+1, (s+e)/2+1, e, idx, v);
        tr[node] = tr[node*2] + tr[node*2+1];
        

    }
}
bool comp(pii p1, pii p2) {
    return p1.second < p2.second;
}
int main() {
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        int power;
        scanf("%d", &power);
        player[i].first = i;
        player[i].second = power;
    }

    // sort power --> re-labeling
    sort(player, player+n, comp);

    
    // re labeling 
    for(int i=0; i<n; i++) {
        player[i].second = i+1;
    }

    // sort original order
    sort(player, player+n);

    for (int i=0; i < n; i++) {
        int curpower = player[i].second; //지금 등수 
        int cnt = 0;
        if (curpower > 1) {
            cnt = seg_sum(1, 1, n, 1, curpower-1);
        }
        update(1,1,n,curpower, 1); // update(int node, int s, int e, int idx, int v)
        printf("%d\n", i+1-cnt);
    }
}