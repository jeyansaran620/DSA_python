# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        self.rank = [1] * len(row_counts)
        n_tables = len(row_counts)
        self.parents = list(range(n_tables))
        
    def get_parent(self, table):
        while self.parents[table] != table:
            table = self.parents[table]
        return table

    def merge(self, src, dst):
        if src == dst:
            return False
        
        src_parent = self.get_parent(src)
        
        dst_parent = self.get_parent(dst)
        
        if src_parent == dst_parent:
            return False
        

        if self.rank[dst_parent] > self.rank[src_parent]:
            self.parents[src_parent] = dst_parent
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            self.max_row_count = max(self.max_row_count,self.row_counts[dst_parent])
            self.row_counts[src_parent] = 0
        
        elif self.rank[dst_parent] == self.rank[src_parent]:
            self.parents[src_parent] = dst_parent
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            self.max_row_count = max(self.max_row_count,self.row_counts[dst_parent])
            self.row_counts[src_parent] = 0
            self.rank[dst_parent] += 1
        else:
            self.parents[dst_parent] = src_parent
            self.row_counts[src_parent] += self.row_counts[dst_parent]
            self.max_row_count = max(self.max_row_count,self.row_counts[src_parent])
            self.row_counts[dst_parent] = 0
            
        
        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        return True

    
    


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
