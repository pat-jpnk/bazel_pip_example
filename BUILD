load("@exdeps//:requirements.bzl", "requirement")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")


compile_pip_requirements(
    name = "requirements",                          
    src = "//pypi:requirements.in",
    requirements_txt = "//pypi:requirements_lock.txt"    
)


py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [requirement("requests")]
)