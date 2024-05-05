workspace(name = "pip_example")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "c68bdc4fbec25de5b5493b8819cfc877c4ea299c0dcb15c244c5a00208cde311",
    strip_prefix = "rules_python-0.31.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.31.0/rules_python-0.31.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_toolchains")

py_repositories()


python_register_toolchains(
    name = "python_3_9",
    # Available versions are listed in @rules_python//python:versions.bzl.
    # We recommend using the same version your team is already standardized on.
    python_version = "3.9",
)

load("@python_3_9//:defs.bzl", "interpreter")

load("@rules_python//python:pip.bzl", "pip_parse")


pip_parse(
    name = "exdeps",
    python_interpreter_target = interpreter,
    requirements_lock = "//pypi:requirements_lock.txt",
)

load("@exdeps//:requirements.bzl", "install_deps")

install_deps()

