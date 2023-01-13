import onnx 
from onnx.helper import make_graph, make_model 
 
def createGraphMemberList(graph_member_list): 
    member_list=[]; 
    for n in graph_member_list: 
        member_list.append(n) 
    return member_list 
 
model = onnx.load("nyu_256x256.onnx") 
#onnx.checker.check_model(model) 
graph = model.graph 
 
input_list = createGraphMemberList(graph.input) 
output_list = createGraphMemberList(graph.output) 
initializer_list = createGraphMemberList(graph.initializer)     
 
for input in input_list: 
    if input.name == "input_1": 
        dim1 = input.type.tensor_type.shape.dim[0] 
        dim2 = input.type.tensor_type.shape.dim[1] 
        dim3 = input.type.tensor_type.shape.dim[2] 
        dim4 = input.type.tensor_type.shape.dim[3] 
        dim1.dim_value = 1 
        dim2.dim_value = 640 
        dim3.dim_value = 480
        dim4.dim_value = 3 
 
Gnodes = graph.node 
name = "XYZ"    
modGraph = make_graph( 
    Gnodes,
    name, 
    input_list, 
    output_list, 
    initializer=initializer_list) 
 
onnx_model = make_model(modGraph) 
onnx.save(onnx_model,"nyu_480x640.onnx")