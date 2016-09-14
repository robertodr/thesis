# How to reproduce the pyridine figures

1. Load pyridine_water_5AA.xyz into PyMOL
2. Stick representation: `show sticks`
3. White background: `bg_color white`
4. Make background transparent: `set ray_opaque_background, off`
5. Rotate until, zoom, fade water cluster until satisfied
6. Save png of cluster: `png pyridine_water_5AA.png, width=1200, height=1200, dpi=300, ray=1`
7. Enable SES: `set surface_solvent, off`
8. Adjust transparency: `set transparency, 0.5`
9. Adjust quality: `set surface_quality, 1`
10. Adjust solvent radius: `set solvent_radius, 1.6`
11. Color surface: `set surface_color, marine`
12. Show surface: `show surface`
13. Show background: `set ray_opaque_background, on`
14. Change background color: `bg_color light_blue`
15. Save png: `png pyridine_water_5AA+cavity.png, width=1200, height=1200, dpi=300, ray=1`
16. Select water molecules: `select water, name O*+H2*+H3*+H4*+H5*`
17. Remove water molecules: `hide water`
18. Re-do steps for surface
19. Save png: `png pyridine_cavity.png, width=1200, height=1200, dpi=300, ray=1`
