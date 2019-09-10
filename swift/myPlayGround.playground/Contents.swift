import UIKit

func selectionSort<T: Comparable>(_ array: [T], _ isOrderBefore: (T, T) -> Bool) -> [Int] {
    guard array.count > 1 else { return array as! [Int] }
    var array = array
    for x in 0..<array.count - 1 {
        var lowest = x
        for y in x + 1 ..< array.count {
            if isOrderBefore(array[y], array[lowest]) {
                lowest = y
            }
        }
        
        if x != lowest {
            array.swapAt(x, lowest)
        }
    }
    
    return array as! [Int]
}

var x = [2 , 13, 2, 5, 7, 9]
selectionSort(x, <)

