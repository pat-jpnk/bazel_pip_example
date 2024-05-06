### bazel pip example

- this example is based on bazel version 7.1.1 and rules_python 0.31.0 
- it is a simple example project where the requests module is imported from pypi and used in the main function 

### commands 
> in this example I invoke bazel using the **bazelisk** command, if you are not using it or renamed the binary, you invoke it with **bazel**

- to generate pip dependencies in the *pypi/requirements_lock.txt* file:
```bash
bazelisk run requirements.update 
```
here, "requirements" is used because that is the name attribute that is set in the [pip_compile_requirements]("https://rules-python.readthedocs.io/en/stable/api/pip.html#compile-pip-requirements") rule located in *./BUILD*  <br><br>if the [pip_compile_requirements]("https://rules-python.readthedocs.io/en/stable/api/pip.html#compile-pip-requirements") rule is not used to generate the *requirements_lock.txt* file, the dependencies of the module *requests* will have to be added manually

- to run the application (which implies building it as well):
```bash
bazelisk run //:main
```

### .gitignore caveats
if not the functionality is not [disabled]("https://bazel.build/reference/command-line-reference#flag--symlink_prefix"), bazel will create symbolic links to directories during the build process - because git treats these as *files* and not *directories* , one needs to use the approriate syntax in the *.gitignore* file
