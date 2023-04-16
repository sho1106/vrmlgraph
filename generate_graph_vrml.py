# coding: utf-8
import math

def write_vrml_header(file):
    file.write("#VRML V2.0 utf8\n\n")
    file.write("DEF Viewer Info {\n")
    file.write("\ttype \"Viewpoint\"\n")
    file.write("\tposition 0 0 20\n")
    file.write("\torientation 0 0 1 0\n")
    file.write("\tfieldOfView 0.785\n")
    file.write("\tdescription \"Viewpoint for the Scene\"\n")
    file.write("}\n\n")

def write_sphere(file, position, color, radius):
    file.write("Transform {\n")
    file.write("\ttranslation %f %f %f\n" % (position[0], position[1], position[2]))
    file.write("\tchildren [\n")
    file.write("\t\tShape {\n")
    file.write("\t\t\tgeometry Sphere { radius %f }\n" % (radius))
    file.write("\t\t\tappearance Appearance { material Material { diffuseColor %f %f %f } }\n" % (color[0], color[1], color[2]))
    file.write("\t\t}\n")
    file.write("\t]\n")
    file.write("}\n\n")

def write_line(file, start, end, color):
    file.write("Transform {\n")
    file.write("\tchildren [\n")
    file.write("\t\tShape {\n")
    file.write("\t\t\tgeometry IndexedLineSet {\n")
    file.write("\t\t\t\tcoord Coordinate { point [\n")
    file.write("\t\t\t\t\t%f %f %f,\n" % (start[0], start[1], start[2]))
    file.write("\t\t\t\t\t%f %f %f\n" % (end[0], end[1], end[2]))
    file.write("\t\t\t\t] }\n")
    file.write("\t\t\t\tcoordIndex [ 0, 1 ]\n")
    file.write("\t\t\t}\n")
    file.write("\t\t\tappearance Appearance { material Material { diffuseColor %f %f %f } }\n" % (color[0], color[1], color[2]))
    file.write("\t\t}\n")
    file.write("\t]\n")
    file.write("}\n\n")

def generate_vrml(graph, filename):

    with open(filename, "w") as file:
        write_vrml_header(file)

        for i, node in enumerate(graph["nodes"]):
            color = [1, 0, 0]
            write_sphere(file, node, color, 0.01)

        for link in graph["links"]:
            start = graph["nodes"][link[0]]
            end = graph["nodes"][link[1]]
            color = [1.0, 1.0, 1.0]
            write_line(file, start, end, color)

if __name__=="__main__":

    import random_graph
    generate_vrml(random_graph.graph, "output.wrl")