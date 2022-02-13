class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dup_files = defaultdict(list)

        for path in paths:
            parts = path.split(' ')
            dir_path = parts[0]

            for i in range(1, len(parts)):
                file_name = parts[i][0:parts[i].index('(')]
                file_content = parts[i][parts[i].index('(') + 1:parts[i].index(')')]
                dup_files[file_content].append(dir_path + '/' + file_name)

        return [value for value in dup_files.values() if len(value) > 1]

# Follow-up Qs:
# 1. BFS vs DFS
# DFS. In this case the directory path could be large. DFS can reuse the shared parent directory
# before leaving that directory. But BFS cannot.
#
# 2. Content file is very large.
# In this case, it is not applicable to match the whole string of the content. So we use file
# signature to judge if two files are identical. Signature can include file size, as well as
# sampled contents on the same positions. They can have different file names and time stamps
# though. Hashmaps are necessary to store the previous scanned file info. S = O(|keys| + |list(directory)|)
# The key and the directory strings are the main space consumption.
#
# a. Smaple to obtain the sliced indices in the strings stored in the RAM only once and used for the
# scanned files. Accessing the strings is on-the-fly. But transforming them to hashcode use look up in
# hashmap and stroing the keys and the directories in the hashmap can be time consuming. The directory
# string can be compressed to directory id. The keys are hard to compress.
#
# b. Use fast hashing algorithm e.g. MD5 or use SHA-256 (no collisions found yet). If no worry about
# the collision, meaning the hashcode is 1-1. Thus in the hashmap, the storage consumption on key
# string can be replaced by key_hashcode, space usage compressed.
#
# algorithm:
# i. compare sizes, if not equal, bail early.
# ii. hash them with a fast algorithm e.g. MD5 or use SHA-256 (no collisions found yet), if not equal, bail early.
# iii. compare byte to byte to avoid false positives due to collisions.
#
# 3. You can only read 1KB each time, how will you modify your solution.
# Thus, the file cannot fit the whole RAM. Use a buffer to read controlled by a loop; read until not
# needed or to the end. The sampled slices are offset by the times the buffer is called.
#
# 4. Time complexity of the modified solution. What's the most time consuming and space consuming part? How to optimize?
# T = O(|num_files||sample||directory_depth|) + O(|hashmap.keys()|)
#
# 5. How to make sure the duplicate files you find are not false positive?
# Add a round of final check which checks the whole string of the content. T = O(|num_output_list||max_list_size||file_size|)
