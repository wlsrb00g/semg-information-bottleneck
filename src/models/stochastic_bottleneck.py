"""Compact reference model for the putEMG stochastic bottleneck study.

Extracted from the CommonNoCondition model in the audited LOSO runner;
kept as a model-only reference. Dataset and training entrypoint are not bundled.
"""
from __future__ import annotations

import torch
from torch import nn


class StochasticBottleneck(nn.Module):
    """528-D feature encoder, diagonal Gaussian bottleneck, 8-class head."""

    def __init__(self, latent_dim: int = 8) -> None:
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(528, 128), nn.GELU(), nn.Linear(128, 32), nn.GELU()
        )
        self.mu = nn.Linear(32, latent_dim)
        self.logvar = nn.Linear(32, latent_dim)
        self.classifier = nn.Sequential(
            nn.Linear(latent_dim, 24), nn.GELU(), nn.Linear(24, 8)
        )

    def encode(
        self, x: torch.Tensor, sample: bool = True
    ) -> tuple[torch.Tensor, torch.Tensor]:
        hidden = self.encoder(x)
        mu = self.mu(hidden)
        logvar = self.logvar(hidden).clamp(-8, 8)
        z = mu + torch.exp(0.5 * logvar) * torch.randn_like(mu) if sample else mu
        kl = -0.5 * (1 + logvar - mu.square() - logvar.exp()).sum(dim=1).mean()
        return z, kl

    def forward(
        self, x: torch.Tensor, sample: bool = True
    ) -> tuple[torch.Tensor, torch.Tensor]:
        z, kl = self.encode(x, sample=sample)
        return self.classifier(z), kl
