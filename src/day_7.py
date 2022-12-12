"""
https://adventofcode.com/2022/day/7
"""
import re


class TerminalParser:
    def __init__(self):
        # self.mode = None
        self.folders = self.current_folder = {"/": {}}
        self.current_folder_path = []

    def __repr__(self):
        return f"TerminalParser({self.folders=})"

    def parse_line(self, string) -> dict[str, int]:
        print(string)
        if match := re.search("\\$ cd (.+)\n?", string):
            # self.mode = "cd"
            (folder_name,) = match.groups()
            if folder_name == "..":
                self.current_folder = self.current_folder_path.pop()
            else:
                self.current_folder = self.current_folder[folder_name]
                self.current_folder_path.append(self.current_folder)
        elif string == "$ ls\n":
            # self.mode = "ls"
            pass
        elif match := re.search("dir (.+)\n?", string):
            (folder_name,) = match.groups()
            self.current_folder[folder_name] = {}
        elif match := re.search("(\\d+) (.+)\n?", string):
            file_size, file_name = match.groups()
            self.current_folder.update(
                {"__file_name": file_name, "__file_size": int(file_size)}
            )
        else:
            raise ValueError
