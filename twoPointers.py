def twoPointers(nums1, nums2):
    combined = []
    i = 0
    j = 0
    while i < len(nums1) or j < len(nums2):
        if i == len(nums1):
            combined.append(nums2[j])
            j += 1
            continue
        elif j == len(nums2):
            combined.append(nums1[i])
            i+=1
            continue
        if nums1[i] <= nums2[j]:
            combined.append(nums1[i])
            i += 1
        else:
            combined.append(nums2[j])
            j += 1
    return combined
in1 = [1, 6, 6, 13, 18, 18]
in2 = [2, 3, 8, 13, 15, 21, 25]
print(twoPointers(in1, in2))