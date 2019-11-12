import UIKit

struct Graph {
    var list: [String: [[String: Int]]]
    init() {
        self.list = [String: [[String: Int]]]()
    }
    
    mutating func addVertex(_ v: String) {
        self.list[v] = [[String: Int]]()
    }
    
    mutating func addEdge(_ a: String, _ b: String, _ distance: Int ) {
        self.list[a]?.append([b: distance])
        self.list[b]?.append([a: distance])
    }
    
    mutating func dijkstra() {
        
    }
}
var a = Graph()
a.addVertex("A")
a.addVertex("B")
a.addVertex("C")
a.addEdge("A", "B", 3)
a.addEdge("B", "C", 4)
a.addEdge("A", "C", 5)
