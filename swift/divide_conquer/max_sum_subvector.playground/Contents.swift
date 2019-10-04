import UIKit


func maxCrossSubVector(array: [Int], low: Int, high: Int, mid: Int) -> Int {
    var sum = 0
    let inf = 1000000
    var leftSum = -inf
    for i in stride(from: mid, through: low, by: -1) {
        sum += array[i]

        if sum > leftSum {
            leftSum = sum
        }
    }
    
    sum = 0
    var rightSum = -inf
    for i in stride(from: mid+1, through: high, by: 1) {
        sum += array[i]
        
        if sum > rightSum {
            rightSum = sum
        }
    }
    return rightSum + leftSum
}

func maxSumSubVector(array: [Int], low: Int, high: Int) -> Int {
    if low == high {
        return array[high]
    }
    
    var mid = Double((low + high) / 2)
    mid.round()
    
    let leftSum = maxSumSubVector(array: array, low: low, high: Int(mid))
    let rightSum = maxSumSubVector(array: array, low: Int(mid+1), high: high)
    let crossSum = maxCrossSubVector(array: array, low: low, high: high, mid: Int(mid))
    return max(leftSum, rightSum, crossSum)
}

let array = [2, 3, 4, 5, 7]
print(maxSumSubVector(array: array, low: 0, high: array.count - 1))

