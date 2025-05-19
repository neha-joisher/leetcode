class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count character frequencies
        counter = Counter(s)
        max_freq = max(counter.values())

        # Step 2: Early check — if not possible, return ""
        if max_freq > (len(s) + 1) // 2:
            return ""

        # Step 3: Build a max heap based on frequency
        # Use negative freq because Python heapq is a min-heap
        maxHeap = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(maxHeap)

        result = []
        prev_freq, prev_char = 0, ""

        # Step 4: Build the result string
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            result.append(char)

            # If previous char still has remaining count, push it back
            if prev_freq < 0:
                heapq.heappush(maxHeap, (prev_freq, prev_char))

            # Decrease the frequency (we used one occurrence)
            prev_freq = freq + 1
            prev_char = char

        return ''.join(result)