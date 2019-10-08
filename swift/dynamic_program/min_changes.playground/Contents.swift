import UIKit

func minChange(str1: String, str2: String) -> Int {
    let a = Array(str1)
    let b = Array(str2)
    
    var A = Array(repeating: Array(repeating: 0, count: b.count+1), count: a.count+1)
    
    for i in 0...a.count {
        for j in 0...b.count {
            if i == 0 {
                A[i][j] = j
            } else if j == 0 {
                A[i][j] = i
            } else if (a[i-1] == b[j-1]) {
                A[i][j] = A[i-1][j-1]
            } else {
                A[i][j] = 1 + min(A[i][j-1], A[i-1][j], A[i-1][j-1])
            }
        }
    }
    
    return A[a.count][b.count]
}

let str1 = "ATGC"
let str2 = "ARG"
minChange(str1: str1, str2: str2)
