'''
Given a list of packages and their dependencies for a project, determine if there is an possible order of execution to complete the project. Ex

I/P : {'A':[], 'B':[], 'C':['A', 'B', 'D'], 'D': 'A'}
O/P : ['A', 'B', 'D', 'C'] or ['B', 'A', 'D', 'C'] or ['A', 'D', 'B', 'C'] or ['B', 'A', 'D', 'C']
'''

class PackageDependency:

	def get_package_order(self, dependencies):
		'''
		This method will find a possible execution of packages for the given project
		'''
		
		packages_done = []
		for package in dependencies.keys():
			if package not in packages_done:
				self._check_package_execution(package, dependencies, packages_done, set())
				if len(packages_done) == 0:
					return []
		return packages_done

	def _check_package_execution(self, package, dependencies, packages_done, packages_in_execution):
		'''
		This method will be adding packages in topological ordering
		'''

		packages_in_execution.add(package)
		for dependency in dependencies[package]:
			if dependency in packages_in_execution:
				packages_done = []
				return 
			if dependency not in packages_done:
				self._check_package_execution(dependency, dependencies, packages_done, packages_in_execution)
			if len(packages_done) == 0:
				return
		packages_in_execution.remove(package)
		packages_done.append(package)

if __name__ == "__main__":
	package_dependency = PackageDependency()
	dependencies = {'A':['B'], 'B':['C'], 'C':['D'], 'D': []}
	print('Possible order of execution of packages is = {}'.format(package_dependency.get_package_order(dependencies)))