// 백준 - 트리 순회

import java.io.BufferedReader
import java.io.InputStreamReader


var N = 0

lateinit var root : Node

class Node(val node: String){
    var leftNode : Node? = null
    var rightNode : Node? = null
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    N = readLine().toInt()
    root = Node("A")
    var parent = "A"

    for(i in 0 until N) {
        val line = readLine().split(' ')
        val name = line[0]; val left = line[1]; val right = line[2]
        val node = Node(name)
        node.leftNode = Node(left)
        node.rightNode = Node(right)

        insertNode(root, node)
    }

    preOrder(root)
    println()
    inOrder(root)
    println()
    postOrder(root)
}


private fun insertNode(parent : Node?, child: Node) {
    if(parent == null) return

    if(parent.node == child.node) {
        if(child.leftNode?.node != ".") {
            parent.leftNode = child.leftNode
        }
        if(child.rightNode?.node != ".") {
            parent.rightNode = child.rightNode
        }
        return
    }

    insertNode(parent.rightNode, child)
    insertNode(parent.leftNode, child)
}

// 전위 순회
private fun preOrder(node : Node) {
    print(node.node)
    node.leftNode?.let { preOrder(it) }
    node.rightNode?.let { preOrder(it) }
}

// 중위 순회
private fun inOrder(node : Node) {

    node.leftNode?.let { inOrder(it) }
    print(node.node)
    node.rightNode?.let { inOrder(it) }
}

// 후위 순회
private fun postOrder(node : Node) {

    node.leftNode?.let { postOrder(it) }
    node.rightNode?.let { postOrder(it) }
    print(node.node)
}