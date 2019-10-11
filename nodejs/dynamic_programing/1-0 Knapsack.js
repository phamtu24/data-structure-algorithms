const knapsack = (W, wt, val, n) => {
    let A = Array.from(Array(n+1), () => Array(W+1));

    for (let i = 0; i <= n; i++) {
        for (let w = 0; w <= W; w++) {
            if (i == 0 || w == 0) {
                A[i][w] = 0;
            } else if (w < wt[i-1]) {
                A[i][w] = A[i-1][w];
            } else {
                A[i][w] = Math.max(val[i-1] + A[i-1][w - wt[i-1]],
                                   A[i-1][w]);
            }
        }
    }
    return A[n][W];
}
let wt = [1, 3, 4, 5];
let val = [1, 4, 5, 7];
let n = val.length;
let W = 7;
console.log(knapsack(W, wt, val, n)); 