# Python program to calculate average height from a list of heights 

heights = input("Enter heights: separated by a space ") #.split()
height_list = heights.split()
# sum = 0
# for i in range(0, len(heights)):
#     sum += int(heights[i])
# print("average height = ", sum / len(heights))

count = 0
sum = 0
for height in height_list:
    count += 1
    sum += int(height)
# print(count) 
# for item in range(count):
#     height_list[item] = int(height_list[item])   


print("average height = ", sum / count).round(2)