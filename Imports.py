# Mechanism that makes code in one file available to another file.

# import <module>            # Imports a built-in or '<module>.py'.
# import <package>           # Imports a built-in or '<package>/__init__.py'.
# import <package>.<module>  # Imports a built-in or '<package>/<module>.py'.

# Package is a collection of modules, but it can also define its own objects.
# On a filesystem this corresponds to a directory of Python files with an optional __init__.py script.
# Running 'import <package>' does not automatically provide access to the package's modules unless they are explicitly imported in its __init__.py script.
# Directory of the file that is passed to python command serves as a root of local imports.
# For relative imports use 'from .[<pkg/module>[...]] import <obj>'.