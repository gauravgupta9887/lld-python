# In the classic implementation of the Singleton Design pattern,
#  we simply use the static method for creating the getInstance method which has the ability to
#  return the shared resource. We also make use of so-called Virtual private Constructor 
#  to raise the exception against it although which is not much required.

# classic implementation of Singleton Design pattern
class Singleton:

	__shared_instance = None

	@staticmethod
	def getInstance():

		"""Static Access Method"""
		if Singleton.__shared_instance == None:
			Singleton()
		return Singleton.__shared_instance

	def __init__(self):

		"""virtual private constructor"""
		if Singleton.__shared_instance != None:
			raise Exception ("This class is a singleton class !")
		else:
			Singleton.__shared_instance = self

# main method
if __name__ == "__main__":

	# create object of Singleton Class
	obj = Singleton()
	print(obj)

	# pick the instance of the class
	obj = Singleton.getInstance()
	print(obj)
