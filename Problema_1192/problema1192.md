# 1192. Critical Connections in a Network

**Difficulty**: Hard  
**Tags**: Graph, DFS, Tarjan’s Algorithm

---

## 🧠 Problem Description

There are `n` servers numbered from `0` to `n - 1` connected by **undirected** server-to-server connections forming a network where:

- `connections[i] = [ai, bi]` represents a connection between servers `ai` and `bi`.

Any server can reach any other server **directly or indirectly** through the network.

A **critical connection** is a connection that, **if removed**, will make **some servers unable to reach some other server**.

Return **all critical connections** in the network in **any order**.

---

## 🖼️ Visual Example

![image](https://github.com/user-attachments/assets/496493e5-2234-4ced-886a-27d28706de11)

---

## 📘 Example 1:

```text
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
