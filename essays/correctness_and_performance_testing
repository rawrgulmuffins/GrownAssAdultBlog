# What's The Goal?

So I often run my unit tests. But I've never really set up any kind of
consistent performance testing. Often times when I'm performance testing it's
because there's an issue and we're doing it because of said issue.

I want to be more proactive. I don't want to wait for issues to find me, I want
to find them first. Also, even if we don't find said issues, I want a
systematic method of testing said issues to see if we hit a regression of some
kind.

This essay contains my experiments using pytest and pytest-benchmark at
PyCon2016. I believe that I have a useful system for both correctness testing
of individual functions (unit tests) and performance testing of said functions
in addition to other (probably older) versions of said functions.

## Measuring Is The First Step To Optimization

My other sub thought was that the first step to optimization should always be
measurement. So why not make the measurement automatic in the same way that
we automate our correctness testing?

# Starting Out: Performance and Correctness Together

I wanted to combine performance testing and unit testing. In my mind you want
to have as few separations between your tests as possible. If you have a bunch
of different kinds of tests that humans have to manually start then the
likelihood that they'll run all of them is low.

So with the intent out of the way lets show you the sample problem I picked.
[Previously I've used interview cake to hone my interviewing skills.](https://www.interviewcake.com/)
One of the things that I really like about them is that their problems tend to
be simple to understand and easy to make a brute force solution to but their
optimal solution can take some thinking.

[I picked their product of other numbers problem found here.](https://www.interviewcake.com/question/python/product-of-other-numbers)

Here's several solutions that I came up with to the problem

    """ These are my answers to an interview prep question from interview cake.

    You have a list of integers, and for each index you want to find the product of
    every integer except the integer at that index.

    Write a function get_products_of_all_ints_except_at_index() that takes a list
    of integers and returns a list of the products.

    https://www.interviewcake.com/question/python/product-of-other-numbers

    """
    import operator
    import functools

    def product_not_at_index_n_squared(target_list):

        product_list = []
        for index, item in enumerate(target_list):
            product = 1
            for inner_index, inner_item in enumerate(target_list):
                if index == inner_index:
                    continue
                product = inner_item * product
            product_list.append(product)

        return product_list

    # Balls, this solution is also N^2
    def product_not_at_index_factors_lists_n_squared(target_list):
        # This ugly line is to make sure we don't get python reference copies.
        factors_lists = [list(target_list) for i in range(len(target_list))]

        # runtime = len(n)
        for index, factors_list in enumerate(factors_lists):
            # Just delete the target_list factor for this index.
            del factors_lists[index][index]

        product_list = []
        #runtime = len(facotries_lists)
        for factor_list in factors_lists:
            product = 1
            # Runtime = len(factories_lists) * len(factor_list) 
            # About equal to len(n) * len(n-1)
            # about equal to O(n^2)
            for factor in factor_list:
                product *= factor
            product_list.append(product)

        return product_list

    @functools.lru_cache(maxsize=None)
    def product(factors):
        product = 1
        for value in factors:
                product *= value
        return product

    # So My idea was that adding a LRU cache would minimize the number of runs but
    # This function seems to be slower than the other two. =(

    # Just tried this with a large input set and it's significantly faster.
    # Still not as fast as the reference solution.
    def product_not_at_index_lru(target_list):
        product_list = []
        for index, _ in enumerate(target_list):
            before_product = product(tuple(target_list[:index]))
            after_product = product(tuple(target_list[index + 1:]))
            product_list.append(before_product * after_product)
        return product_list


And here's interview cake's reference solution

    def get_products_of_all_ints_except_at_index(int_list):

        # we make a list with the length of the input list to
        # hold our products
        products_of_all_ints_except_at_index = [None] * len(int_list)

        # for each integer, we find the product of all the integers
        # before it, storing the total product so far each time
        product_so_far = 1
        i = 0
        while i < len(int_list):
            products_of_all_ints_except_at_index[i] = product_so_far
            product_so_far *= int_list[i]
            i += 1

        # for each integer, we find the product of all the integers
        # after it. since each index in products already has the
        # product of all the integers before it, now we're storing
        # the total product of all other integers
        product_so_far = 1
        i = len(int_list) - 1
        while i >= 0:
            products_of_all_ints_except_at_index[i] *= product_so_far
            product_so_far *= int_list[i]
            i -= 1

        return products_of_all_ints_except_at_index

# Let's Talk Parameterized Unit Tests

After writing unit tests for a couple of years now my tests have been taking
the shape, more and more, of this structure.

    import pytest

    import product_not_at_index


    def run_test(function_input, expected_result):
        actual_result = product_not_at_index.product_not_at_index(function_input)
        assert actual_result == expected_result

    def test_empty_list():
        input_data = []
        expected_result = []
        run_test(input_data, expected_result)

    def test_single_item():
        input_data = [1]
        expected_result = [1]
        run_test(input_data, expected_result)

    def test_one_times_one():
        input_data = [1, 1]
        expected_result = [1, 1]
        run_test(input_data, expected_result)

    def test_normal_use_case():
        input_data = [1, 7, 3, 4]
        expected_result = [84, 12, 28, 21]
        run_test(input_data, expected_result)

The idea behind this structure is that I make a `run_test` function and group
tests that can all use the same `run_test` function. This was my first step
to make a more logical test organization. 

But now I have the case where I have multiple versions of the same function
that I want to test the correctness of. So suddenly my `run_test` looked like
this

    def run_test(function_input, expected_result):
        test_functions = [
            product_not_at_index.product_not_at_index(function_input),
            product_not_at_index.product_not_at_index_lru(function_input),
            ...
        ]
        for test_function in test_functions:
            actual_result = test_function(function_input)
            assert actual_result == expected_result

But this caused an interesting issue. When one of my solutions failed with a
specific test (say the empty list condition) I had a much harder time telling
which one would fail because all of the functions got run at the same time.

# Parameterization To The Rescue

`pytest` comes with  this really nifty feature called parameterization. It
looks like

    functions_to_test = [
        product_not_at_index.product_not_at_index_n_squared,
        product_not_at_index.product_not_at_index_factors_lists_n_squared,
        product_not_at_index.product_not_at_index_lru,
        reference_solution.get_products_of_all_ints_except_at_index,
    ]

    @pytest.mark.parameterized("test_func", test_functions)
    def test_normal_use_case():
        input_data = [1, 7, 3, 4]
        expected_result = [84, 12, 28, 21]
        run_test(input_data, expected_result, test_func)

What this nifty piece of code will do is run this test function,
`test_normal_use_case`, once for each parameterized input. So in this case,
four times. This is exactly the behavior I wanted because this means that if
the second function is broken I can immediately see which implementation broke.

But this got me thinking. All of my unit tests set input date, expected
results, and pass both of these and a passed in test function to `run_test`.
That's a lot of code reuse. Why don't I parameterize the different data inputs
as well?

# Parameterizing Test Function and Data

Here's what my final correctness solution looks like

    """
    In order to run this you'll need

    pytest
    pytest-benchmark
    """
    import pytest
    import random

    import product_not_at_index
    import reference_solution


    functions_to_test = [
        product_not_at_index.product_not_at_index_n_squared,
        product_not_at_index.product_not_at_index_factors_lists_n_squared,
        product_not_at_index.product_not_at_index_lru,
        reference_solution.get_products_of_all_ints_except_at_index,
    ]

    test_data = [
        ([], []),
        ([1], [1]),
        ([1, 1], [1, 1]),
        ([1, 7, 3, 4],  [84, 12, 28, 21]),
    ]

    # TODO: turn into a list comprehension.
    test_paramaters = []
    for func in functions_to_test:
        for test_input, expected_result in test_data:
            test_paramaters.append([test_input, expected_result, func])


    @pytest.mark.parametrize("function_input,expected_result,test_func", test_paramaters)
    def test_run(benchmark, function_input, expected_result, test_func):
        actual_result = benchmark(test_func, function_input)
        assert actual_result == expected_result

I personally think this is much cleaner code and it produces very pretty / 
readable test results.

    $py.test test.py -v
    =============================================================================================== test session starts ===============================================================================================
    platform darwin -- Python 3.5.0, pytest-2.9.1, py-1.4.31, pluggy-0.3.1 -- /Users/alexlord/.virtualenvs/interviews/bin/python3.5
    cachedir: .cache
    benchmark: 3.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=5.00us max_time=1.00s calibration_precision=10 warmup=False warmup_iterations=100000)
    rootdir: /Users/alexlord/git/personal/interview_question_implementations/interview_prep/product_not_at_index, inifile:
    plugins: benchmark-3.0.0
    collected 18 items

    test.py::test_run[function_input0-expected_result0-test_func0] PASSED
    test.py::test_run[function_input1-expected_result1-test_func1] PASSED
    test.py::test_run[function_input2-expected_result2-test_func2] PASSED
    test.py::test_run[function_input3-expected_result3-test_func3] PASSED
    test.py::test_run[function_input4-expected_result4-test_func4] PASSED
    test.py::test_run[function_input5-expected_result5-test_func5] PASSED
    test.py::test_run[function_input6-expected_result6-test_func6] PASSED
    test.py::test_run[function_input7-expected_result7-test_func7] PASSED
    test.py::test_run[function_input8-expected_result8-test_func8] PASSED
    test.py::test_run[function_input9-expected_result9-test_func9] PASSED
    test.py::test_run[function_input10-expected_result10-test_func10] PASSED
    test.py::test_run[function_input11-expected_result11-test_func11] PASSED
    test.py::test_run[function_input12-expected_result12-test_func12] PASSED
    test.py::test_run[function_input13-expected_result13-test_func13] PASSED
    test.py::test_run[function_input14-expected_result14-test_func14] PASSED
    test.py::test_run[function_input15-expected_result15-test_func15] PASSED

    ============================================================================================ 18 passed in 0.04 seconds ============================================================================================

I haven't figured out how to make more readable names for my parameterization
but I'm happy with where this is at this moment.

# Meet pytest-benchmark

So there's this nifty little package called `pytest-benchmark` that's a little
challenging to use but produces beautiful data on the performance of the
programs you produce. I had to bash my brain against the learning curve a
little bit but it was well worth the grey matter.

When you add pytest-benchmark to your test cases it looks like

    pytest.mark.parametrize("function_input,expected_result,test_func", test_paramaters)
    def test_run(benchmark, function_input, expected_result, test_func):
        actual_result = benchmark(test_func, function_input)
        assert actual_result == expected_result

And suddenly when you run things with pytest you'll get this gorgeous output

    $py.test test.py
    =============================================================================================== test session starts ===============================================================================================
    platform darwin -- Python 3.5.0, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
    benchmark: 3.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=5.00us max_time=1.00s calibration_precision=10 warmup=False warmup_iterations=100000)
    rootdir: /Users/alexlord/git/personal/interview_question_implementations/interview_prep/product_not_at_index, inifile:
    plugins: benchmark-3.0.0
    collected 16 items

    test.py ................


    -------------------------------------------------------------------------------------------------------- benchmark: 16 tests --------------------------------------------------------------------------------------------------------
    Name (time in ns)                                                   Min                       Max                  Mean                 StdDev                Median                   IQR            Outliers(*)  Rounds  Iterations
    -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    test_run[function_input8-expected_result8-test_func8]          560.0003 (1.0)         16,199.8562 (1.0)        628.6020 (1.0)         170.8109 (1.0)        580.4281 (1.0)         63.0004 (1.0)      14198;16493  200000           7
    test_run[function_input12-expected_result12-test_func12]       865.9990 (1.55)        44,847.7993 (2.77)       995.7465 (1.58)        296.1051 (1.73)       908.9999 (1.57)       197.9992 (3.14)       4296;2310  187266           5
    test_run[function_input0-expected_result0-test_func0]          879.9980 (1.57)        84,887.0040 (5.24)     1,082.4629 (1.72)        731.1406 (4.28)       968.0007 (1.67)       205.0001 (3.25)       1922;2606  116442           1
    test_run[function_input1-expected_result1-test_func1]        1,699.0016 (3.03)       598,309.0014 (36.93)    2,020.7692 (3.21)      1,849.2927 (10.83)    1,825.9962 (3.15)       319.9966 (5.08)       1263;4179  147951           1
    test_run[function_input4-expected_result4-test_func4]        2,016.9973 (3.60)        83,863.0003 (5.18)     2,349.9562 (3.74)        817.8490 (4.79)     2,157.9981 (3.72)       310.9963 (4.94)      1834;12382  149254           1
    test_run[function_input13-expected_result13-test_func13]     2,165.9944 (3.87)        71,061.0038 (4.39)     2,478.9610 (3.94)        801.0768 (4.69)     2,307.9992 (3.98)       230.9898 (3.67)      2682;14841  133352           1
    test_run[function_input9-expected_result9-test_func9]        2,544.9990 (4.54)       563,333.0002 (34.77)    2,944.0097 (4.68)      1,917.3966 (11.23)    2,685.0030 (4.63)       325.9993 (5.17)      1445;11188  113008           1
    test_run[function_input2-expected_result2-test_func2]        2,571.0033 (4.59)       246,006.0059 (15.19)    3,088.5783 (4.91)      1,369.3798 (8.02)     2,807.9958 (4.84)       617.0012 (9.79)       1410;1494  102449           1
    test_run[function_input14-expected_result14-test_func14]     2,674.0017 (4.78)        81,621.0013 (5.04)     3,074.1181 (4.89)        949.2261 (5.56)     2,831.9992 (4.88)       339.9909 (5.40)      2408;10263  120034           1
    test_run[function_input15-expected_result15-test_func15]     3,637.0038 (6.49)       295,559.9994 (18.24)    4,156.6325 (6.61)      1,439.7919 (8.43)     3,827.0009 (6.59)       421.9983 (6.70)      2329;12110  136370           1
    test_run[function_input5-expected_result5-test_func5]        3,822.0023 (6.83)        78,857.0032 (4.87)     4,441.5151 (7.07)      1,230.8019 (7.21)     4,069.9961 (7.01)       630.4981 (10.01)      4629;7351   84984           1
    test_run[function_input10-expected_result10-test_func10]     4,271.0017 (7.63)        91,283.9969 (5.63)     4,936.8990 (7.85)      1,291.4317 (7.56)     4,547.0006 (7.83)       542.9902 (8.62)       7383;8388   94278           1
    test_run[function_input3-expected_result3-test_func3]        4,595.0001 (8.21)       254,519.0000 (15.71)    5,385.4536 (8.57)      2,197.4682 (12.86)    4,845.9988 (8.35)     1,111.9992 (17.65)        978;984   83725           1
    test_run[function_input6-expected_result6-test_func6]        5,068.9996 (9.05)        93,649.0032 (5.78)     5,895.7273 (9.38)      1,573.9056 (9.21)     5,342.0008 (9.20)     1,191.9983 (18.92)      2962;1091   65877           1
    test_run[function_input7-expected_result7-test_func7]        6,461.0067 (11.54)    5,631,620.9957 (347.63)   7,620.4352 (12.12)    22,317.5270 (130.66)   6,938.9935 (11.95)      816.7535 (12.96)        83;5612   64251           1
    test_run[function_input11-expected_result11-test_func11]     7,266.0041 (12.98)       89,729.0010 (5.54)     8,265.7584 (13.15)     2,005.4555 (11.74)    7,601.0037 (13.10)      881.9989 (14.00)      4072;4159   50649           1
    -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    (*) Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
    =========================================================================================== 16 passed in 37.18 seconds ============================================================================================

That is **92 times slower** than a non-benchmarked piece of code. Holy shit 0.o

# Even more surprising

We'll get back to how long it took to run the code in just a second. An even
more interesting thing that took me by surprise is that function runs 12-15
aren't the consistent fastest in the bunch. Run 15, the normal case, is
decidedly middle of the pack which really took me by surprise.

Part of me wondered if this was just an overhead problem so to test this I add
a "large input" benchmark.

    # Found at
    # https://stackoverflow.com/questions/4172131/create-random-list-of-integers-in-python
    # This is done at the module level so that each implementation gets the
    # same input. 
    large_input_list = [int(1000*random.random()) for i in range(10000)]

    @pytest.mark.parametrize("test_func", functions_to_test)
    def test_large_input_speed(benchmark, test_func):
        benchmark(test_func, large_input_list)

Which, when run, produced this output.

test_large_input_speed[test_func3]                                6,092,073.9998 (>1000.0)       9,215,803.0020 (>1000.0)       6,815,266.4239 (>1000.0)      728,120.9603 (>1000.0)       6,501,765.0049 (>1000.0)    1,070,624.2520 (>1000.0)         28;2     151           1
test_large_input_speed[test_func2]                            1,680,199,910.9957 (>1000.0)   1,702,819,657.9995 (>1000.0)   1,691,921,799.1992 (>1000.0)    8,479,934.4638 (>1000.0)   1,689,919,190.9979 (>1000.0)   10,792,933.2462 (>1000.0)          2;0       5           1
test_large_input_speed[test_func1]                           12,934,396,921.9990 (>1000.0)  13,668,151,101.9997 (>1000.0)  13,305,998,574.3996 (>1000.0)  274,037,337.0935 (>1000.0)  13,316,970,378.9972 (>1000.0)  370,253,495.7483 (>1000.0)          2;0       5           1
test_large_input_speed[test_func0]                           19,585,742,333.0017 (>1000.0)  19,765,584,692.9993 (>1000.0)  19,698,525,190.2021 (>1000.0)   72,823,859.1132 (>1000.0)  19,713,395,115.0026 (>1000.0)  105,883,734.9992 (>1000.0)          1;0       5           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

(*) Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
=========================================================================================== 22 passed in 293.13 seconds ===========================================================================================

These benchmarks confirmed what I believed to be true (The reference solution
is significantly superior to all others, the LRU solution second best) but now
our tests are **732 times slower** than just our correctness tests.

# Suggested Project Structure

This brings me to a suggestion of how to add benchmark tests to your project
in a sane fashion. My suggestions is that performance tests and correctness
tests end up in two separate folders

project 
├── project
│   ├── product_not_at_index.py # This contains normal unit tests
├── correctness_tests
│   ├── tests.py # This contains normal unit tests
├── performance_tests
    # This contains previous implementations to act as controls to run against the current solution.
│   ├── previous_product_not_at_index_solutions.py 
    # this file contains the actual benchmark tests with specific input cases.
│   ├── tests.py

The other potential solution is to to have correctness_tests and
performance_tests live in the same test files and use the `--benchmark-skip` 
command line argument but then you get output like this

    py.test test.py --benchmark-skip
    =============================================================================================== test session starts ===============================================================================================
    platform darwin -- Python 3.5.0, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
    benchmark: 3.0.0 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=5.00us max_time=1.00s calibration_precision=10 warmup=False warmup_iterations=100000)
    rootdir: /Users/alexlord/git/personal/interview_question_implementations/interview_prep/product_not_at_index, inifile:
    plugins: benchmark-3.0.0
    collected 38 items

    test.py ................ssssssssssssssssssss..

    ====================================================================================== 18 passed, 20 skipped in 0.06 seconds ======================================================================================

and I personally think that it's harder to tell if you actually passed all of
your tests with this output. The skips muddle things for me.

# Conclusions

* Parameterized Testing lets you stop repeating yourself
* pytest-benchmark produces beautiful and readable output
* Adding benchmark tests to your test suit means that you can automatically
  measure the performance of your programs.
* Adding controls to your benchmark tests let you make meaningful comparisons
* Adding benchmarks significantly slows test cases down
* My suggestion is to split performance tests and correctness tests into separate
  directories.
* Make sure to test your solutions with "large" inputs.
* Think about adopting a "test required" project policy for performance fixes
  similar to a "test required" policy for bug fixes.
