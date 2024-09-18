import heapq

# Given a list of webpages and the number of times each webpage has been viewed, 
# return the 5th most viewed webpage.

def fifth_most_viewed(webpages):
    min_heap = []
    for page, views in webpages:
        heapq.heappush(min_heap, (views, page))
        if len(min_heap) > 5:
            heapq.heappop(min_heap)
    print("Min_heap top 5: ", min_heap)
    return heapq.heappop(min_heap)[1]

webpages = [("page1", 100), ("page2", 200), ("page3", 300), ("page4", 400), ("page5", 500), ("page6", 600)]
print(fifth_most_viewed(webpages))
