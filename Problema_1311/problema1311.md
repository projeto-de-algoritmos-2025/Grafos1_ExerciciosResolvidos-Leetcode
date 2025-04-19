# 1311. Get Watched Videos by Your Friends

**Difficulty**: Medium  
**Tags**: Graph, BFS, HashMap, Sorting

---

## 🧠 Problem Description

There are `n` people, each person has a unique id between `0` and `n - 1`. Given the arrays `watchedVideos` and `friends`, where:

- `watchedVideos[i]` contains the list of watched videos for the person with `id = i`.
- `friends[i]` contains the list of friends for the person with `id = i`.

---

### 📊 Levels

- **Level 1** of videos are all watched videos by your **direct friends**.
- **Level 2** of videos are all watched by **friends of friends**, and so on.
- In general, **level k** of videos are all watched by people with the **shortest path exactly equal to k** from you.

---

### 🎯 Task

Given:
- Your `id`
- A level `k`

Return the **list of videos** watched at that level, ordered by:
1. Frequency (ascending)
2. Alphabetically (if frequencies are equal)

---

## 📘 Example 1

![image](https://github.com/user-attachments/assets/4d3307e1-b4b2-4ac9-a404-48cef1efccc2)

Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
Output: ["B","C"] 
Explanation: 
You have id = 0 (green color in the figure) and your friends are (yellow color in the figure):
Person with id = 1 -> watchedVideos = ["C"] 
Person with id = 2 -> watchedVideos = ["B","C"] 
The frequencies of watchedVideos by your friends are: 
B -> 1 
C -> 2

## 📘 Example 2

![image](https://github.com/user-attachments/assets/27398f88-6a9a-400d-ab6b-c03aa5c6f52b)

Input: 
watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 2

Output: ["D"]


```text
Input: 
watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 1

Output: ["B","C"]
