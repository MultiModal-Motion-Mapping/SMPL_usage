import smplx
import torch
import trimesh

FZM_MARKER = {
    'Skeleton2ChestLow': 3506,
    'Skeleton2ChestTop': 3171,
    'Skeleton2WaistRFront': 4343,
    'Skeleton2WaistLFront': 857,
    'Skeleton2WaistLBack': 3122,
    'Skeleton2WaistRBack': 6544,
    'Skeleton2WaistCBack': 3022,
    'Skeleton2BackLeft': 1252,
    'Skeleton2BackRight': 4735,
    'Skeleton2LShoulderBack': 2940,
    'Skeleton2RShoulderBack': 6399,
    'Skeleton2BackTop': 3471,

    'Skeleton2HeadFront': 335,
    'Skeleton2HeadTop': 411,
    'Skeleton2HeadRight':3709,
    'Skeleton2HeadLeft': 166,

    'Skeleton2RShoulderTop': 5322,
    'Skeleton2RUArmHigh': 4794,
    'Skeleton2RElbowOut': 5127,
    'Skeleton2RFArm': 5210,
    'Skeleton2RWristIn': 5573,
    'Skeleton2RWristOut': 5568,
    'Skeleton2RHandIn': 5531,
    'Skeleton2RHandOut': 5525,
    'Skeleton2LShoulderTop': 1861,
    'Skeleton2LUArmHigh': 1315,
    'Skeleton2LElbowOut': 1660,
    'Skeleton2LFArm': 1741,
    'Skeleton2LWristIn': 2112,
    'Skeleton2LWristOut': 2108,
    'Skeleton2LHandIn': 2070,
    'Skeleton2LHandOut': 2176,

    'Skeleton2RThighFront': 4360,
    'Skeleton2RThighSide': 4334,
    'Skeleton2RKneeOut': 4538,
    'Skeleton2RShin': 4589,
    'Skeleton2RAnkleOut': 6728,
    'Skeleton2RToeTip': 6699,
    'Skeleton2RToeIn': 6736,
    'Skeleton2RToeOut': 6747,
    'Skeleton2RHeel': 6786,
    'Skeleton2LThighFront': 874,
    'Skeleton2LThighSide': 850,
    'Skeleton2LKneeOut': 1053,
    'Skeleton2LShin': 1103,
    'Skeleton2LAnkleOut': 3327,
    'Skeleton2LToeTip': 3299,
    'Skeleton2LToeIn': 3336,
    'Skeleton2LToeOut': 3346,
    'Skeleton2LHeel': 3387,
}

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
                       faces=smpl_model.faces,
                       vertex_colors=[[0, 255, 0] if i in FZM_MARKER.values() else [255, 0, 0] for i in range(6890)])
mesh.export('smpl_mesh_FZM.obj')

# Visualization using blender
# Please refer to doc\Blender OBJ Sequence.md
# Also, available in the following link:
# https://blog.csdn.net/wjrzm2001/article/details/136676240