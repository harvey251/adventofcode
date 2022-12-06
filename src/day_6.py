"""
https://adventofcode.com/2022/day/6
"""
from queue import Queue


class PacketFinder(Queue):
    """FIFO Queue with all_unique method"""

    def all_unique(self):
        """
        determines whether all the items in the queue are unique
        """
        seen = set()
        for item in self.queue:
            if item in seen:
                return False
            seen.add(item)
        return True


def find_start_of_packet(string) -> int:
    """
    your subroutine needs to identify the first position
    where the four most recently received characters were all different.
    Specifically, it needs to report the number of characters
    from the beginning of the buffer to the end of the first such four-character marker.
    """
    queue = PacketFinder(maxsize=4)

    for idx, char in enumerate(string, 1):
        queue.put_nowait(char)
        if queue.full():
            if queue.all_unique():
                return idx
            queue.get()

    raise ValueError("unique 4 chars not found")
