import torch
tensor = torch.tensor([[[2, 3], [4, 5]], [[6, 7], [8, 9]]], dtype=torch.float32, requires_grad=True)

# print (tensor.dtype)
# print (tensor.ndim)
# print (tensor [0, 0, 0])
# print (type(tensor[0, 0, 0]))
# print(tensor[0, 0, 0].item())
print (type(tensor[0, 0, 0].item()))