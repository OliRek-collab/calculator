#Calculator

A python 3 calculator used from the terminal, built step by step in SCCM4910

## What it will do
It will be able to add, multiply and divide 2 numbers, then displays the result.

## How to run it
First run the SCCM4910 environment, do this by running: source /opt/python-venv/sccm-4910/bin/activate
To run the test dependency, run: ./check.sh
Then you should expect 5 test results, all being passed.
After test use: echo $?
you should get exit status 0 meaning tests have been passed.
Run calculator program: ./run.sh
Enter the first number, operator (such as + - * /), then the second number.
The program prints Result: followed by the answer.
To stop the program, press CTRL + C together.
