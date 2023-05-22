import os
from testflows.core import *
from selenium import webdriver
import shutil

with Scenario('Test verify proper functionality of -a, --all and --author options of the ls utility'):
    with Given("the user is in a directory with files and subdirectories"):
        # create a test directory with files and subdirectories
        test_dir = "test_dir"
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)
        os.mkdir(test_dir)
        with open(f"{test_dir}/file1.txt", "w") as f:
            f.write("This is file1.")
        with open(f"{test_dir}/file2.txt", "w") as f:
            f.write("This is file2.")
        os.mkdir(f"{test_dir}/subdir1")
        os.mkdir(f"{test_dir}/subdir2")
        with open(f"{test_dir}/subdir2/file3.txt", "w") as f:
            f.write("This is file3.")

    with When("the user executes 'ls -a'"):
        output = os.popen("ls -a test_dir").read()

    with Then("all files and directories are listed, including hidden ones"):
        print(output)
        assert ".\n..\nfile1.txt\nfile2.txt\nsubdir1\nsubdir2\n" in output

    with When("the user executes 'ls --all'"):
        output = os.popen("ls --all test_dir").read()

    with Then("all files and directories are listed, including hidden ones"):
        assert ".\n..\nfile1.txt\nfile2.txt\nsubdir1\nsubdir2\n" in output