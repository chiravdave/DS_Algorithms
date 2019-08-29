"""
Given the string representing of a file system in the form 'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext', 
return the length of the longest absolute path to a file in the abstracted file system. If there is 
no file in the system, return 0. Ex:

dir
	subdir1
	subdir2
		file.ext

the longest absolute path is "dir/subdir2/file.ext", and its length is 20 (not including the double quotes).

Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""

class DirStructure:

	def longest_absolute_file_path(self, dir_struct: str) -> int:
		"""
		This method will return the length of the longest absolute path to a file in the abstracted file system.

		:param dir_struct: string representation of the directory
		:rtype: length of the longest absolute path to a file
		"""

		last_n_tabs, longest_path, cur_highest, cur_folders = 0, 0, 0, []
		# Getting list of files and folders in the correct order
		n_files = dir_struct.split("\n")
		if len(n_files) < 0:
			return "Empty directory"
		# Adding root directory
		cur_folders.append(n_files[0])
		# Will access each file individually
		for token in n_files[1:]:
			# Finding no. of tabs
			n_tabs = token.rfind("\t") + 1
			if n_tabs < 0 or abs(n_tabs-last_n_tabs) > 1:
				raise Exception("Invalid format for the directory structure")

			# Getting file name which can be a folder as well
			file_name = token[n_tabs:]
			# Checking if it is a file
			if "." in file_name:
				# Checking if this file is deeper than the deepest file we found till now
				if n_tabs > cur_highest:
					 longest_path = self._file_path_length(cur_folders, file_name)
					 cur_highest = n_tabs
			else:
				# Checking if we are at the same level
				if n_tabs == last_n_tabs:
					cur_folders[-1] = file_name
				# Checking if we are going one level down
				elif n_tabs > last_n_tabs:
					cur_folders.append(file_name)
				# We are moving one level up
				else:
					cur_folders.pop()
				last_n_tabs = n_tabs

		return longest_path

	def _file_path_length(self, cur_path, file_name) -> int:
		"""
		This method will return the path length of a file.

		:param cur_path: list of folders
		:param file_name: name of the file
		:rtype: path length of a file
		"""

		path_length = 0
		for folder in cur_path:
			path_length += len(folder)
			path_length += 1

		return path_length + len(file_name)

if __name__ == "__main__":
	dir_struc = DirStructure()
	print(dir_struc.longest_absolute_file_path("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))