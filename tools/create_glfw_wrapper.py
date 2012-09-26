# this creates a wrapper using ctypes for glfw from the header
# it's not fully automatic, but it does a good deal of work

import re

with open("../glfw/include/GL/glfw3.h") as header_file:
    data = header_file.read()

# normalize whitespace
data = re.sub(r"[ \t]+", " ", data)

# delete beginning
data = data[data.index("*/", data.index("Input handling definitions")) + 2:]
    
# delete end
data = data[:data.rindex("/*", 0, data.index("Global definition cleanup"))]

# delete deprecated aliases
data = data[:data.rindex("/* GLFW 2.x key name aliases (deprecated) */")] + data[data.index("/* Mouse button definitions */"):]

# delete GLFWAPI and const
data = re.sub(r" *\bGLFWAPI\b *", "", data)
data = re.sub(r" *\bconst\b *", "", data)

# remove GLFW prefix
data = data.replace("GLFW_", "")
data = data.replace("GLFW", "")

# remove semicolon
data = data.replace(";", "")

# convert defines
data = re.sub(r"#define (\w+) (\w+)", r"\1 = \2", data)

# convert one-liner comments
data = re.sub(r"/\* *((?:[^/\n]|(?:[^*\n]/))+) *\*/", r"# \1", data)

# convert multiline comments
data = re.sub(r"/\*((?:[^/]|[^*]/)+)\*/", lambda r: "\"\"\"\n" + r.group(1).replace("*", "").strip() + "\n\"\"\"\n", data)

# convert function typedefs
data = re.sub(r"typedef +(\w+) *\( *\* *(\w+) *\) *\(([^)\n]+)\)", r"\2 = CFUNCTYPE(\1, \3)", data)

# rest of the typedefs are manual

def func_decl_helper(res):
    arguments = res.group(3)
    
    if arguments != "void":
        arguments = ",".join(" ".join(arg.split()[:-1]) for arg in res.group(3).split(","))
    
    return "{1} = glfwdll.glfw{1}\n{1}.restype = {0}\n{1}.argtypes = [{2}]".format(res.group(1), res.group(2), arguments)

# make empty argument lists empty
data = data.replace("(void)", "()")
    
# convert function declarations
data = re.sub(r"([^ \n]+) +glfw(\w+)\(([^)\n]*)\)", func_decl_helper, data)

# convert pointer types
data = data.replace("unsigned char*", "POINTER(c_ubyte)")
data = data.replace("char*", "c_char_p")
data = re.sub(r"(\w[\w ]+)\*", r"POINTER(\1)", data)

# convert void
data = re.sub(r"\bvoid\b", "None", data)

# convert other types
data = re.sub(r"\bint\b", "c_int", data)
data = re.sub(r"\bfloat\b", "c_float", data)
data = re.sub(r"\bdouble\b", "c_float", data)
data = re.sub(r"\bunsigned long\b", "c_ulong", data)

# normalize whitespace
data = re.sub(r" +", " ", data)
data = re.sub(r"\n\n+", "\n\n", data)
data = re.sub(r"\s*,\s*", ", ", data)
data = data.strip() + "\n"

with open("glfw_wrapper.py", "w") as output_file:
    output_file.write(data)
