The Python package Pandas and sys have been used to do this project. 
Considering the input data is clean, every id is unique, therefore there is no step to remove the repeated id and missing data.
With regard to the same custermer could buy the medicine multiple times but with different id, the number of purchase is sumed to one to this sepcific customer. However, the drug cost were added together. 

The input file for my test was creatd based on the given incont.txt, I added some situations on the my test input files.

Both tests are past. 


I used the following directory structure:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── pharmacy-counting.py
    ├── input
    │   └── itcont.txt
    ├── output
    |   └── top_cost_drug.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── top_cost_drug.txt
            ├── your-own-test_1
                ├── input
                │   └── your-own-input-for-itcont.txt
                |── output
                    └── top_cost_drug.txt
