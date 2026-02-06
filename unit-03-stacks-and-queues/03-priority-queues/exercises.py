"""
File: exercises.py
Purpose: LAB: PRIORITY QUEUE CHALLENGES
Author: GonzaloQu3dena
Date: 2026-02-05
Version: 1.1
"""

from typing import List, Tuple
from priority_queue import PriorityQueue

def exercise_1_hospital_triage(patients: List[Tuple[str, int]]) -> List[str]:
    """
    Exercise 1: ER Triage Simulation
    
    Objective:
    Given a list of (patient_name, urgency_level), return the names in the 
    order they should be treated.
    
    Logic:
    1. Create a `PriorityQueue`.
    2. Enqueue all patients using `pq.enqueue(name, urgency)`.
    3. Dequeue everything into a list and return it.
    """
    # TODO: Implement logic
    pass

def exercise_2_k_largest_elements(nums: List[int], k: int) -> List[int]:
    """
    Exercise 2: Find K Largest Elements
    
    Objective:
    Find the K largest numbers in an unsorted list using a Priority Queue.
    
    Logic:
    1. Enqueue all numbers into a `PriorityQueue`.
    2. For each number, use its value as its priority: `pq.enqueue(num, num)`.
    3. Dequeue exactly `k` times and store results.
    """
    # TODO: Implement logic
    pass

def exercise_3_task_scheduler(tasks: List[Tuple[str, int]]) -> str:
    """
    Exercise 3: Simple OS Scheduler
    
    Objective:
    Simulate an OS that runs tasks based on priority. Return the name 
    of the highest priority task without removing it.
    
    Logic:
    1. Enqueue all tasks using `pq.enqueue(task_name, priority)`.
    2. Use `pq.peek()` to see the next task.
    """
    # TODO: Implement logic
    pass

def exercise_4_merge_sorted_lists(lists: List[List[int]]) -> List[int]:
    """
    Exercise 4: Merge Multiple Sorted Lists
    
    Objective:
    Combine several sorted lists into one single sorted list.
    
    Logic:
    1. This requires picking the smallest element, but our PQ is Max-Priority.
    2. Use the "Negative Priority" trick: `pq.enqueue(val, -val)`.
    3. Always pick the smallest available element from all lists.
    """
    # TODO: Implement logic
    pass

def exercise_5_min_priority_queue_logic() -> None:
    """
    Exercise 5: Min-Priority Logic
    
    Objective:
    Explain how to turn your Max-Priority Queue into a Min-Priority Queue 
    without changing the class code.
    
    Logic:
    If priority A < priority B, then -A > -B. 
    By enqueuing with `priority * -1`, the Max-Priority Queue will serve 
    the smallest numbers first.
    """
    # TODO: Implement logic
    pass

def exercise_6_is_priority_sorted(pq: PriorityQueue) -> bool:
    """
    Exercise 6: Consistency Check
    
    Objective:
    Verify that the internal elements of the PQ are correctly sorted 
    by priority during traversal.
    
    Logic:
    Iterate through the queue and check if `current.priority >= next.priority`.
    """
    # TODO: Implement logic
    pass

def exercise_7_cpu_load_balancer(processes: List[Tuple[int, int]]) -> int:
    """
    Exercise 7: CPU Load Balancer
    
    Objective:
    Given processes with (id, burst_time), always serve the one with the 
    shortest burst time first (Shortest Job First).
    
    Logic:
    Use the "Negative Priority" trick: `pq.enqueue(process_id, -burst_time)`.
    """
    # TODO: Implement logic
    pass

def exercise_8_top_k_frequent_words(words: List[str], k: int) -> List[str]:
    """
    Exercise 8: Most Frequent Words
    
    Objective:
    Find the top `k` most frequent words in a list.
    
    Logic:
    1. Use a dictionary to count frequencies: `{word: count}`.
    2. For each word, `pq.enqueue(word, count)`.
    3. Dequeue `k` times.
    """
    # TODO: Implement logic
    pass

def exercise_9_connect_ropes_min_cost(ropes: List[int]) -> int:
    """
    Exercise 9: Connect Ropes with Minimum Cost
    
    Objective:
    Given lengths of ropes, connect them into one rope with minimum cost. 
    
    Logic:
    1. Use a Min-Priority approach (`-length` as priority).
    2. Always pop the two smallest ropes, sum them, add to total cost, 
       and push the sum back into the PQ.
    """
    # TODO: Implement logic
    pass

def exercise_10_emergency_dispatch_simulation() -> None:
    """
    Exercise 10: 911 Emergency Dispatch
    
    Objective:
    Simulate a dispatch system where:
    - 'Police' (Priority 3)
    - 'Fire' (Priority 2)
    - 'Ambulance' (Priority 1)
    
    Logic:
    Use `pq.enqueue(incident_description, priority_value)`.
    """
    # TODO: Implement logic
    pass