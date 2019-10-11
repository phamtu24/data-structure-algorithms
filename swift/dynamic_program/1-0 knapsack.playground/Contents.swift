import UIKit

func knapsack(_ W: Int, _ wt: [Int], _ val: [Int], _ n: Int) -> Int {
    var A = Array(repeating: Array(repeating: 0, count: W+1), count: n+1)
    for i in 0...n {
        for w in 0...W {
            if i == 0 || w == 0 {
                A[i][w] = 0
            } else if w < wt[i-1] {
                A[i][w] = A[i-1][w]
            } else {
                A[i][w] = max(val[i-1] + A[i-1][w - wt[i-1]], A[i-1][w])
            }
        }
    }

    return A[n][W]
}

let wt = [1, 3, 4, 5];
let val = [1, 4, 5, 7];
let n = val.count;
let W = 7;
print(knapsack(W, wt, val, n));


