from collections import deque

def topological_sort(courses, prerequisites):
    # Step 1: Build the graph (adjacency list) and in-degree counter
    graph = {course: [] for course in courses}
    in_degree = {course: 0 for course in courses}
    
    for course, prereqs in prerequisites.items():
        for prereq in prereqs:
            graph[prereq].append(course)
            in_degree[course] += 1

    # Step 2: Initialize queue with courses having 0 in-degree (no prerequisites)
    queue = deque([course for course in courses if in_degree[course] == 0])
    order = []

    # Step 3: Process courses using BFS
    while queue:
        course = queue.popleft()
        order.append(course)

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: If order contains all courses, return it; otherwise, there's a cycle
    return order if len(order) == len(courses) else "Cycle detected, cannot complete all courses."

# Define courses and prerequisites
courses = [
    "CS250", "CS256", "CS257", "CS258", "CS259", "CS310", "CS314", "CS336",
    "CS360", "CS411", "CS418", "CS452", "CS459", "CS469", "CS470", "CS471",
    "MTH111", "MTH112", "MTH251", "MTH252"
]

prerequisites = {
    "CS250": ["MTH112"],
    "CS256": ["MTH111"],
    "CS257": ["MTH112", "CS256"],
    "CS258": ["MTH251", "CS257"],
    "CS259": ["CS257"],
    "CS314": ["CS257"],
    "CS336": ["CS257"],
    "CS360": ["CS257"],
    "CS411": ["CS258", "MTH252", "CS250"],
    "CS418": ["CS258", "CS250"],
    "CS452": ["CS418", "CS259"],
    "CS459": ["CS258", "CS314"],
    "CS469": ["CS411"],
    "CS470": ["CS469"],
    "CS471": ["CS470"]
}

if __name__ == "__main__":
    sorted_courses = topological_sort(courses, prerequisites)
    print(sorted_courses)  # Ensure output is printed
