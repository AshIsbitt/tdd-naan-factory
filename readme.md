# TDD Naan factory exercise

This exercise is going to bring together lots of concepts.

Learning Outcomes:
- git
- github
- python functions
- TDD
- Separation of Concerns
- DRY Code
- Definition of Done
- Others

## Installing and running
To run the naan factory, please do the following:

```python
import naan_factory
run_factory()
```

### TDD - Test Driven Development
1. Write the test
2. Run it and read the error
3. Code and make it pass

This helps with
- Preventing overengineering
- Maintainable code
- Reduce technical debt
- Goes well with Agile and working code
- Can guide you through the errors

#### Unit Tests
Test a single piece of code, such as a function

####Base of a test

Usually has three phases:
- Set up phase (known variables)
- Calling of the function with the known variables
- Running for expected output

### User Stories for Naan Factory

```
#1
As a user, I can use the make_dough with water 
and flour to make dough.

#2
As a user, I can use the bake_dough with dough 
to get naan.

#3
As a user, I can use the run_factory with water 
and flour and get naan.
```

