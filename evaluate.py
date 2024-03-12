from metrics import *
import torch

# meter to millimeter
M2MM = 1000
# index of the root joint
ROOT_INDEX = 0

def mpjpe(pred_j3ds, target_j3ds):
    """
    Computes MPJPE.
    Args:
        pred_j3ds (NxJx3).
        target_j3ds (NxJx3).
    Returns:
        MPJPE (1).
    """
    # pelvis is the root joint
    pred_pelvis = pred_j3ds[:,[ROOT_INDEX],:]
    target_pelvis = target_j3ds[:,[ROOT_INDEX],:]

    # root align
    pred_j3ds_norm = pred_j3ds - pred_pelvis
    target_j3ds_norm = target_j3ds - target_pelvis

    errors = torch.sqrt(((pred_j3ds_norm - target_j3ds_norm) ** 2).sum(dim=-1)).mean(dim=-1).cpu().numpy()
    return np.mean(errors) * M2MM

def pmpjpe(pred_j3ds, target_j3ds):
    """
    Computes P-MPJPE.
    Args:
        pred_j3ds (NxJx3).
        target_j3ds (NxJx3).
    Returns:
        P-MPJPE (1).
    """
    # pelvis is the root joint
    pred_pelvis = pred_j3ds[:,[ROOT_INDEX],:]
    target_pelvis = target_j3ds[:,[ROOT_INDEX],:]

    # root align
    pred_j3ds_norm = pred_j3ds - pred_pelvis
    target_j3ds_norm = target_j3ds - target_pelvis

    S1_hat = batch_compute_similarity_transform_torch(pred_j3ds_norm, target_j3ds_norm)
    errors_pa = torch.sqrt(((S1_hat - target_j3ds_norm) ** 2).sum(dim=-1)).mean(dim=-1).cpu().numpy()
    return np.mean(errors_pa) * M2MM

def pve(pred_verts, target_verts, pred_j3ds, target_j3ds):
    """
    Computes PVE over 6890 surface vertices.
    Args:
        pred_verts (Nx6890x3).
        target_verts (Nx6890x3).
    Returns:
        PVE (1).
    """
    # pelvis is the root joint
    pred_pelvis = pred_j3ds[:,[ROOT_INDEX],:]
    target_pelvis = target_j3ds[:,[ROOT_INDEX],:]

    # root align
    pred_verts_norm = pred_verts - pred_pelvis
    target_verts_norm = target_verts - target_pelvis

    errors_pve = torch.sqrt(((pred_verts_norm - target_verts_norm) ** 2).sum(dim=-1)).mean(dim=-1).cpu().numpy()
    return np.mean(errors_pve) * M2MM