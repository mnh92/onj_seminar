import DatasetParser as dp

# example file
with open('example_data/0a9e35fd6f123137d585a482f2484d8e.xml', 'r') as file:
    instances = dp.parse_file(file)

