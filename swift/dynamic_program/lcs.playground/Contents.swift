import UIKit

func lcs(str1: String, str2: String) -> Int {
    let len1 = Array(str1).count
    let len2 = Array(str2).count

    var A = Array(repeating: Array(repeating: 0, count: len2+1), count: len1+1)

    for i in 0...len1 {
        for j in 0...len2 {
            if i == 0 || j == 0 {
                A[i][j] = 0
            } else if Array(str1)[i-1] == Array(str2)[j-1] {
                A[i][j] = 1 + A[i-1][j-1]
            } else {
                A[i][j] = max(A[i-1][j], A[i][j-1], A[i-1][j-1])
            }
        }
    }

    return A[len1][len2]
}

let str1 = "ATGX"
let str2 = "ARGC"

lcs(str1: str1, str2: str2)

