* %cd: to change the current working directory
* %edit: to open an editor and execute the code you typed in after closing the editor
* %env: to show the current environment variables
* %pip install [pkgs]: to install packages without leaving the interactive shell
* %time and %timeit: to time the execution of Python code


Introspection Using a question mark (?) before or after a variable will display information about the object.
For example, we could get a list of all functions in the top level NumPy namespace containing load:
np.*load*?
	np.load
	np.loads
	np.loadtxt
	np.pkgload


Magic functions can be used by default without the percent sign,
as long as no variable is defined with the same name as the magic
function in question.
This feature is called automagic and can be enabled using %automagic.


ipython qtconsole --pylab=inline

will cause IPython to launch with the default GUI backend integration enabled
so that matplotlib plot windows can be created with no issues.
Secondly, most of NumPy and matplotlib will be imported.


You can start typing a few letters of the %run command then press the <up arrow>.
This will search the command history for the first prior command matching the letters you typed

!cmdExecute cmd in the
	system shelloutput = !cmd
	argsRun cmd and store the
	stdout in output%alias alias_name
	cmdDefine an alias for a system (shell) command%bookmarkUtilize IPython’s directory bookmarking system%cd
	directoryChange system working directory to passed directory%pwdReturn the current system working directory%pushd
	directoryPlace current directory on stack and change to target
	directory%popdChange to directory popped off the top of the stack%dirsReturn a list containing the current directory
	stack%

IPython can also substitute in Python values defined in the current environment when using !.
To do this, preface the variable name by the dollar sign $:In [3]: foo = 'test*'

