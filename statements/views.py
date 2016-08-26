import random
from django.shortcuts import render
from django.http import	HttpResponse

from .models import Statement

def random_statement(request):
	statement = get_random_statement()
	return render(request, 'statements/random_statement.html', {'statement' : statement})

def get_random_statement():
	'''
	Gets random statement from DB where already_used == False
	'''
	statements = Statement.objects.filter(already_used=False)
	
	if statements.count() == 0:
		mark_all_statements_as_unused()
		get_random_statement()

	random_statement = random.choice(statements)
	mark_statement_as_used(random_statement)

	return random_statement

def mark_statement_as_used(statement):
	'''
	Sets already_used flag of a statment to True
	'''
	statement.already_used = True
	statement.save()

def mark_all_statements_as_unused():
	'''
	Sets all statments in database as already_used == False)
	'''
	Statement.objects.update(already_used=False)
