
from fabric.api import local, settings, abort
from fabric.contrib.console import confirm
import sys


# prep
def test():
	with settings(warn_only=True):
		result = local("nosetests -v", capture=True)
	if result.failed and not confirm("Tests failed. Continue?"):
		abort("Aborted at user request.")
	


def commit():
	message = input("Enter a git commit message: ")
	local("git add . && git commit -am '{}'".format(message))


def push():
	local("git push origin master")

def heroku():
	local("git push heroku master")

def heroku_test():
	local("heroku run nosetests -v")

def deploy():
	pull()
	test()
	commit()
	heroku()
	heroku_test()

def prepare():
	test()
	commit()
	push()


def rollback():
	local("heroku rollback")