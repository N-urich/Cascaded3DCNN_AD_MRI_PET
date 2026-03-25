import torch
import torch.nn as nn

class Cascaded3DCNN(nn.Module):
    def __init__(self):
        super().__init__()
        # Your MRI branch
        self.mri_branch = nn.Sequential(
            nn.Conv3d(1, 16, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool3d(2),
            # Add more layers as in your paper
        )
        # Your PET branch
        self.pet_branch = nn.Sequential(
            nn.Conv3d(1, 16, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool3d(2),
        )
        # Fusion layer
        self.fusion = nn.Linear(1024, 3)

    def forward(self, x_mri, x_pet):
        f_mri = self.mri_branch(x_mri)
        f_pet = self.pet_branch(x_pet)
        out = self.fusion(torch.cat([f_mri, f_pet], dim=1))
        return out
