# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def SiftDown(H,i):
    maxIndex = i
    l = (i*2) + 1
    r = (i*2) + 2
    
    if l <= len(H) - 1:
        if H[l][0] < H[maxIndex][0]:
            maxIndex = l
        elif H[l][0] == H[maxIndex][0] and H[l][1] < H[maxIndex][1]:
            maxIndex = l
            
    if r <= len(H) - 1:
        if H[r][0] < H[maxIndex][0]:
            maxIndex = r
        elif H[r][0] == H[maxIndex][0] and H[r][1] < H[maxIndex][1]:
            maxIndex = r
        
    if i != maxIndex:
        H[i], H[maxIndex] = H[maxIndex],H[i]
        H = SiftDown(H,maxIndex)
    return H

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [[0,i] for i in range(n_workers)]
    for job in jobs:
        next_free_time = SiftDown(next_free_time,0)
        result.append(AssignedJob( next_free_time[0][1],  next_free_time[0][0]))
        next_free_time[0][0] += job

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
