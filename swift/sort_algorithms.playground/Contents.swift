import UIKit

func bubbleSort<T: Comparable>(_ array: [T], _ compare: (T,T) -> Bool) -> [T] {
    var array = array
    for i in 0..<array.count {
        for j in 0..<array.count-i-1 {
            if compare(array[j], array[j+1]) {
                array.swapAt(j, j+1)
            }
        }
    }
    return array
}

func selectionSort<T: Comparable>(_ array: [T], _ compare: (T, T) -> Bool) -> [T] {
    var array = array
    for i in 0..<array.count {
        var min = i
        for j in i+1..<array.count {
            if compare(array[min], array[j]) {
                print("min: \(min), j: \(j)" ,compare(array[min], array[j]))
                min = j
                print(min)
            }
        }
        array.swapAt(min, i)
    }
    return array
}

let array = [1 ,100, 5, 34, 6, 2]
print(selectionSort(array, >))
