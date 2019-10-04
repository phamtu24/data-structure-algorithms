import UIKit

var array = [3, 5, -1, 4, -6]

func maxSumSubvector(array: [Int]) -> Int {
    var maxSum = array[0]
    var sumSoFar = array[0]
    
    for i in 1..<array.count {
        sumSoFar = max(array[i], sumSoFar + array[i])
        maxSum = max(sumSoFar, maxSum)
    }
    return maxSum
}

print(maxSumSubvector(array: array))

