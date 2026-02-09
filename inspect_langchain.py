import langchain
print(f"File: {langchain.__file__}")
print(f"Path: {langchain.__path__}")
import pkgutil
print("Submodules:")
for importer, modname, ispkg in pkgutil.iter_modules(langchain.__path__):
    print(modname)
