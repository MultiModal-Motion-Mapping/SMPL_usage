import smplx
import torch
import trimesh

# Load SMPL model (A body model)
smpl_model = smplx.create('data\SMPL_NEUTRAL.pkl', 'smpl')

# Create a batch of parameters
batch_size = 1

# Create a batch of parameters
result = smpl_model(betas=torch.zeros(batch_size, 10), # shape parameters
                    body_pose=torch.zeros(batch_size, 23, 3), # pose parameters
                    global_orient=torch.zeros(batch_size, 1, 3), # global orientation
                    transl=torch.zeros(batch_size, 3)) # global translation

# joint names are shown in SMPL_joint_names.json
print(result.joints.shape) # (1, 45, 3)
print(result.vertices.shape) # (1, 6890, 3)

# Create a mesh from the vertices and faces
mesh = trimesh.Trimesh(vertices=result.vertices[0].cpu().numpy(), 
                       faces=smpl_model.faces)
mesh.export('smpl_mesh.obj')

# Visualization using blender
# Please refer to doc\Blender OBJ Sequence.md
# Also, available in the following link:
# https://blog.csdn.net/wjrzm2001/article/details/136676240