from collections import deque
import time

class RateLimiter:
    def __init__(self, limit_per_minute):
        self.limit = limit_per_minute
        self.user_requests = {}

    def allow_request(self, user):
        current_time = time.time()
        window_start = current_time - 60

        if user not in self.user_requests:
            self.user_requests[user] = deque()

        queue = self.user_requests[user]

        while queue and queue[0] < window_start:
            queue.popleft()

        if len(queue) < self.limit:
            queue.append(current_time)
            print("we did it")
            return True
        return False