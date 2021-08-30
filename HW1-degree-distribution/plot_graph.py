import matplotlib.pyplot as plt  # put at the top of file
import math                      # put at the top of file, for the "Log" calculation

def main():
	plot_some_numbers()
	return

def plot_some_numbers():
	fig = plt.figure(figsize=(6.5,4))  # make a 6.5" wide by 4" tall figure.
	x = list(range(1,10))             # make a list of [1,2,3,...9]
	y = [xval/1.5+2 for xval in x]    # y is a  function of x
	logx = [math.log(a) for a in x]   # compute the log of x
	logy = [math.log(b) for b in y]   # compute the log of y

	plt.subplot(1,2,1)                # in a 1-by-2 grid, 1st subplot
	plt.plot(x,y,'o-r')               # plot a red line with circles
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Some Numbers')

	plt.subplot(1,2,2)                # in a 1-by-2 grid, 2nd subplot
	plt.plot(logx,logy,'s-b',label='example legend')         # plot a blue line with squares
	plt.legend()
	plt.xlabel('log x')
	plt.ylabel('log y')
	plt.title('Some Numbers (log)')

	plt.tight_layout()                # make the labels  "snap" to the grid.
									  # this may emit a warning, which is OK
	plt.savefig('numbers.png')        # save figure as PNG
	print('wrote to numbers.png')
	return

if __name__ == '__main__':
	main()
