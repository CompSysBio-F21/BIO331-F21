## Bio331 Reference for Generating Figures
import matplotlib.pyplot as plt  # put at the top of file
import math                      # put at the top of file, for the "Log" calculation

def main():
	plot_some_numbers()
	plot_some_numbers_bar()
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

def plot_some_numbers_bar():
	fig = plt.figure(figsize=(4,4))  # make a 4" wide by 4" tall figure.
	width = 0.25

	x = list(range(1,10))             # make a list of [1,2,3,...9]
	y = [xval/1.5+2 for xval in x]    # y is a  function of x
	x2 = [xval+width for xval in x]  # shift x2 by width
	y2 = [xval*2+3 for xval in x] # y2 is a function of x


	plt.bar(x,y,width=width,label='y')
	plt.bar(x2,y2,width=width,label='y2')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Some Numbers')
	plt.legend()
	plt.tight_layout()                # make the labels  "snap" to the grid.
									  # this may emit a warning, which is OK
	plt.savefig('numbers_bar.png')        # save figure as PNG
	print('wrote to numbers_bar.png')
	return

if __name__ == '__main__':
	main()
