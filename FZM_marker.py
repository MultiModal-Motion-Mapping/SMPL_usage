import smplx
import torch
import trimesh

FZM_MARKER_OLD = {
    "Skeleton1ChestHFront": "CLAV",
    "Skeleton1ChestLFront": "STRN",
    "Skeleton1ChestHBack": "C7",
    "Skeleton1ChestLBack": "T10",

    "Skeleton1HeadRFront": "RFHD",
    "Skeleton1HeadRBack": "RBHD",
    "Skeleton1HeadTop": "ARIEL",
    "Skeleton1HeadLFront": "LFHD",
    "Skeleton1HeadLBack": "LBHD",

    "Skeleton1WaistRFront": "RFWT",
    "Skeleton1WaistLFront": "LFWT",
    "Skeleton1WaistMFront": "MFWT",
    "Skeleton1WaistRBack": "RBWT",
    "Skeleton1WaistLBack": "LBWT",
    "Skeleton1WaistMBack": "MBWT",
    
    "Skeleton1RShoulderFront": "RFSH",
    "Skeleton1RShoulderBack": "RBSH",
    "Skeleton1LShoulderFront": "LFSH",
    "Skeleton1LShoulderBack": "LBSH",
    "Skeleton1RArm": "RUPA",
    "Skeleton1LArm": "LUPA",
    "Skeleton1RForeArm": "RFRM",
    "Skeleton1LForeArm": "LFRM",
    "Skeleton1RElbowHigh": "RELB",
    "Skeleton1RElbowLow": "RELBIN",
    "Skeleton1LElbowHigh": "LELB",
    "Skeleton1LElbowLow": "LELBIN",
    "Skeleton1RWristIn": "RIWR",
    "Skeleton1RWristOut": "ROWR",
    "Skeleton1LWristIn": "LIWR",
    "Skeleton1LWristOut": "LOWR",

    "Skeleton1RHandIn": "RTHMB",
    "Skeleton1RHandOut": "RFIN",
    "Skeleton1LHandIn": "LTHMB",
    "Skeleton1LHandOut": "LFIN",
    "Skeleton1LThigh": "LTHI",
    "Skeleton1RThigh": "RTHI",
    "Skeleton1LShin": "LSHN",
    "Skeleton1RShin": "RSHN",
    "Skeleton1LKneeOut": "LKNE",
    "Skeleton1LKneeIn": "LKNI",
    "Skeleton1RKneeOut": "RKNE",
    "Skeleton1RKneeIn": "RKNI",
    "Skeleton1LAnkleOut": "LANK",
    "Skeleton1RAnkleOut": "RANK",
    "Skeleton1RHeel": "RHEE",
    "Skeleton1LHeel": "LHEE",
    "Skeleton1LToeTip": "LTOE",
    "Skeleton1LToeIn": "LMT1",
    "Skeleton1LToeOut": "LMT5",
    "Skeleton1RToeTip": "RTOE",
    "Skeleton1RToeIn": "RMT1",
    "Skeleton1RToeOut": "RMT5",
}

FZM_MARKER = {
    'SkeletonChestLow': 3506,
    'SkeletonChestTop': 3171,
    'SkeletonWaistRFront': 4343,
    'SkeletonWaistLFront': 857,
    'SkeletonWaistLBack': 3122,
    'SkeletonWaistRBack': 6544,
    'SkeletonWaistCBack': 3022,
    'SkeletonBackLeft': 1252,
    'SkeletonBackRight': 4735,
    'SkeletonLShoulderBack': 2940,
    'SkeletonRShoulderBack': 6399,
    'SkeletonBackTop': 3471,

    'SkeletonHeadFront': 335,
    'SkeletonHeadTop': 411,
    'SkeletonHeadRight':3709,
    'SkeletonHeadLeft': 166,

    'SkeletonRShoulderTop': 5322,
    'SkeletonRUArmHigh': 4794,
    'SkeletonRElbowOut': 5127,
    'SkeletonRFArm': 5210,
    'SkeletonRWristIn': 5573,
    'SkeletonRWristOut': 5568,
    'SkeletonRHandIn': 5531,
    'SkeletonRHandOut': 5525,
    'SkeletonLShoulderTop': 1861,
    'SkeletonLUArmHigh': 1315,
    'SkeletonLElbowOut': 1660,
    'SkeletonLFArm': 1741,
    'SkeletonLWristIn': 2112,
    'SkeletonLWristOut': 2108,
    'SkeletonLHandIn': 2070,
    'SkeletonLHandOut': 2176,

    'SkeletonRThighFront': 4360,
    'SkeletonRThighSide': 4334,
    'SkeletonRKneeOut': 4538,
    'SkeletonRShin': 4589,
    'SkeletonRAnkleOut': 6728,
    'SkeletonRToeTip': 6699,
    'SkeletonRToeIn': 6736,
    'SkeletonRToeOut': 6747,
    'SkeletonRHeel': 6786,
    'SkeletonLThighFront': 874,
    'SkeletonLThighSide': 850,
    'SkeletonLKneeOut': 1053,
    'SkeletonLShin': 1103,
    'SkeletonLAnkleOut': 3327,
    'SkeletonLToeTip': 3299,
    'SkeletonLToeIn': 3336,
    'SkeletonLToeOut': 3346,
    'SkeletonLHeel': 3387,
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
