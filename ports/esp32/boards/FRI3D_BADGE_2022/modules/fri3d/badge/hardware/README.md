# FRI3D_BADGE_2024 Hardware Definition

This module contains the hardware definition of the badge. It should not contain any initializing code or force any
driver selection. The default drivers and initialization provided by Fri3d go into either
* the `fri3d.badge` module in `FRI3D_BADGE_COMMON`
* a `fri3d.badge.implementation` module in this board definition which then gets imported into the `fri3d.badge` module as a
  part of the common SDK
