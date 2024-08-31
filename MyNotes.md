## Test Driven Development

**It consists of writing the tests before writing the actual code to insure that code does not produce any unexpected errors in the production environment**

### The 3 laws of TDD

1. **Write a failing test before writing production code**
   The purpose of this particular rule is to create a failing test first and only after it's ensured that the test fails as intended.
   This case make sures that any code that does that is not tied to the test will fail by default
2. **Write only enough test code as is sufficient enough to fail**
   It consits of only writing the minimum amout of code which is enough for the test case to be failed.
   this rule works in incremental manner. like we would be improving the code step by step
   In this rule compilation error also consists as a failed case
3. **Only implement a minimal code that makes the failing test pass.**
   Now the 3rd rule says that only write the minimum amout of code which is enough for the test case to pass

---

### Red-Green-Refactor Cycle:

**Test driven development follows a repetitive cycle to ensure that the final code will be error free and tested from start to end.**

1. **RED - Write a Failing Test**
   It consists of defining the functionality you want to implement by writing a test that fails.
2. **Green - Write Just Enough Code to Pass the Tes**
   It consists of Implementing the minimum amount of code required to make the failing test pass.
3. **Refactor - Improve the Code**
   Review the code you wrote to pass the test and look for opportunities to simplify the code and reduce redudancy
