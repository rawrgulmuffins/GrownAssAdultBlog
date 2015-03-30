Title: Python Module Scope
Date: 2015-03-29
Category: Programming
Tags: python,scope,language_design,mutability
Authors: Alex Lord
Summary: You mean a constant was modified?

Scope in Python can be weird. More importantly, scope combined with mutability can lead to some interesting bugs. My unit tests were failing in a way that truly baffled me and I couldn’t figure out why.


    import IndexRecord
       
    class TestRecords(unittest.TestCase):

        def setUp(self):
        # This Calls create_record_file() which is 
        # defined later on.
        self.index_record = IndexRecord(“Record_path”)


        def test_add_duplicate_entry_to(self):
            hash_to_add = 'test'
            file_size = "9"
            self.index_record.add_to_ignore(
                file_size=file_size,
                hash_to_add=hash_to_add)
            hash_to_add = 'test'
            with self.assertRaises(ValueError):
                self.index_record.add_to_ignore(
                    file_size=file_size,
                    hash_to_add=hash_to_add)

        def test_add_first_entry_to_ignore(self):
            hash_to_add = "Test"
            file_size = "9"
            self.index_record.add_to_ignore(
                file_size=file_size,
                hash_to_add=hash_to_add)
            actual_data = \
                      self.index_record.files_to_ignore["9"]
            expected_data = ["Test"]
            self.assertEqual(
                expected_data,
                actual_data)


The  `test_add_first_entry_to_ignore` test was failing because it was raising a ValueError from the combination `”9”` : `Test` already being present in the ignored dictionary. This baffled my mind. When I debugged the code I made sure that the record was deleted between the tests so I wasn’t pulling up previous test data. If I set the value of `.files_to_ignore` to an empty dictionary at the start of the test, the test would pass. I was so confused that you could have balanced a shoe on my head and I wouldn’t have noticed.

At this point, some of you are going to be face palming. For everyone who's like me let’s walk through a code example to better dissect my shame.

    EMPTY_INDEX_RECORD = {"dates":[], 
        "files_to_ignore":{}}
    EMPTY_INSTANCE_RECORD = {"include":[], "ignore":[]}

    def create_record_file(file_path, record_type):
        """
        Given a valid file path, create a empty record 
        of the indicated record type. For more 
        information on what records are and what they 
        do please read either record.py or README.md.

        This is inherently a destructive call and 
        should not be made on a record that already 
        exists.
        """
        if os.path.isfile(file_path):
            #Die screaming. About to cause corruption.
            raise ValueError("Attempting to create a" 
                "record where one already exists." 
                "Exiting before corruption occurs.")

        if record_type == INDEX_RECORD:
            empty_record = EMPTY_INDEX_RECORD
        elif record_type == INSTANCE_RECORD:
            empty_record = EMPTY_INSTANCE_RECORD

        with open(file_path, "w+") as record_file:
            json.dump(empty_record, record_file)
            print(empty_record)
        return empty_record

Can you spot what’s wrong with this code?

I’ll give you a hint

      empty_record = EMPTY_INDEX_RECORD
      Print(EMPTY_INDEX_RECORD)
      # prints {"dates":[], "files_to_ignore":{}} on 
      # the first function call.

      empty_record = EMPTY_INDEX_RECORD
      Print(EMPTY_INDEX_RECORD)
      # prints {"dates":[], "files_to_ignore":{“9”: 
      # “test”}} on the second function call.


I’ve made the really easy mistake of forgetting that module level code is only called once, during the first import, and that Python’s default assignment behavior for mutable objects is by reference instead of value.

![Pass by reference vs pass by value]({filename}/images/pass_by_reference.png)


[I found this image and corresponding SO post to be immensely helpful.](http://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference)

Let’s have a look at the code again. First, my unit tests are importing the records.py module. This means that the top level code 

    EMPTY_INDEX_RECORD = {"dates":[], 
        "files_to_ignore":{}}
    EMPTY_INSTANCE_RECORD = {"include":[], "ignore":[]}

and 

    def create_record_file(file_path, record_type):

is called once. Notice that none of the code inside of the function definition is parsed (beyond some very basic syntax checks), but the function text is loaded into memory to be passed into the python read evaluate print (REP) loop once the function is called. If certain code paths are rarely traversed, this can lead to some hilarious errors, but that’s a different blog post.

The important part of this particular bug is that the module level expressions that define `EMPTY_INDEX_RECORD` is called once and only once. [This variable doesn’t get reassigned when you call any of the classes or functions defined in records.py.](http://pyvideo.org/video/2567/import-ant-decisions)

Also notice that I’m returning a variable that was assigned an empty index record. 

      empty_record = EMPTY_INDEX_RECORD
      return empty_record

Because an empty index record is a dictionary this means that I’m passing a reference (shallow copy) and, because I’ve defined the original dictionary at the module scope, that’s only called once. Then all modifications made to the dictionary persist as long as the module import stays in scope. 

Python’s way of dealing with scope can be really counter intuitive (at least if you’re coming from C, C++, or Java land). Mutable data structures act in seemingly broken ways because of it. I'm sure this is very intentional on Python's part but it's hard to tell what's dressed up or not.

![Bug vs Feature]({filename}/images/bug_vs_feature.png)

[Image found at](https://xinrongding.wordpress.com/)

The solution I chose was to move the empty declarations inside the function definition. This is probably how things should have been declared to start, but we’re not all perfect.



    def create_record_file(file_path, record_type):
        """
        Given a valid file path, create a empty record 
        of the indicated record type. For more 
        information on what records are and what they 
        do please read either record.py or README.md.

        This is inherently a destructive call and 
        should not be made on a record that already 
        exists.
        """
        EMPTY_INDEX_RECORD = {"dates":[], 
            "files_to_ignore":{}}
        EMPTY_INSTANCE_RECORD = {"include":[], 
            "ignore":[]}
            
        if os.path.isfile(file_path):
            #Die screaming. About to cause corruption.
            raise ValueError("Attempting to create a" 
                "record where one already exists." 
                "Exiting before corruption occurs.")

        if record_type == INDEX_RECORD:
            empty_record = EMPTY_INDEX_RECORD
        elif record_type == INSTANCE_RECORD:
            empty_record = EMPTY_INSTANCE_RECORD

        with open(file_path, "w+") as record_file:
            json.dump(empty_record, record_file)
            print(empty_record)
        return empty_record
        
In short, don’t be dumb like me. Learn how scoping in Python works.
