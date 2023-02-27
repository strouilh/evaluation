import pathlib, sys
print(sys.path)
print("--------------------")
sys.path.append(str(pathlib.Path(__file__).parent))
sys.path.append('.')


print(str(pathlib.Path(__file__).parent)+"\app")
#print(sys.path)