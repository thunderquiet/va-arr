


## How to run:

`python3 ./main.py`



## Questions:

#### 1 - What is the time complexity of your implementation?

O(m) - linear

#### 2 - In general (considering other problems), what is a possible disadvantage of a best-time time complexity implementation?

The implementation can not be parallelized. Using a less-efficient implementation with a double for-loop, we can calculate sums in parallel and then take the smallest one. This is the map-reduce model. The current solution, while being faster, is limited to a single thread.


